#!/usr/bin/env python3
"""Fetch a date-bounded cs.SD corpus and build reproducible category indexes.

Only public arXiv metadata is stored. Classification is conservative and keyword
based: a paper may appear in multiple indexes, while unmatched papers remain in
the complete monthly corpus and the review queue.
"""
from __future__ import annotations

import argparse
import csv
import html
import json
import re
import subprocess
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "resources" / "arxiv-cs-sd"
ATOM = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/", "x": "http://arxiv.org/schemas/atom"}
UA = {"User-Agent": "awesome-sound-detection/1.0 (public literature indexing)"}

MAIN = {
    "acoustic-anomaly": {
        "title": "声学异常检测（ASD）", "path": "papers/acoustic-anomaly/arxiv-cs-sd-2025-2026.md",
        "terms": ["acoustic anomaly", "anomalous sound", "machine anomaly", "machine condition", "fault diagnosis", "fault detection", "predictive maintenance", "condition monitoring", "out-of-distribution audio", "out of distribution audio"],
    },
    "sound-event": {
        "title": "声音事件检测与分类（SED）", "path": "papers/sound-event/arxiv-cs-sd-2025-2026.md",
        "terms": ["sound event", "audio event", "acoustic event", "environmental sound", "sound classification", "audio classification", "sound recognition", "acoustic scene", "audio tagging", "sound source localization", "acoustic source localization"],
    },
    "das": {
        "title": "分布式声学传感（DAS）", "path": "domains/das/arxiv-cs-sd-2025-2026.md",
        "terms": ["distributed acoustic sensing", "distributed fiber optic", "distributed fibre optic", "fiber-optic acoustic", "fibre-optic acoustic", "phase-sensitive optical time domain", "phi-otdr", "φ-otdr"],
    },
    "leakage": {
        "title": "泄漏与听漏", "path": "domains/leakage/arxiv-cs-sd-2025-2026.md",
        "terms": ["acoustic leak", "leak detection", "leak localization", "leakage detection", "pipeline leak", "water leak", "gas leak"],
    },
    "speaker": {
        "title": "声纹识别", "path": "related/speaker-recognition/arxiv-cs-sd-2025-2026.md",
        "terms": ["speaker recognition", "speaker verification", "speaker identification", "speaker diarization", "voiceprint", "voice biometrics", "speaker embedding", "speaker detection"],
    },
    "foundation": {
        "title": "音频基础模型", "path": "related/foundation-models/arxiv-cs-sd-2025-2026.md",
        "terms": ["audio foundation model", "audio-language model", "audio language model", "large audio model", "audio large language", "speech foundation model", "acoustic foundation model", "clap", "beats", "audio-text pretraining", "audio text pretraining"],
    },
}

TOPICS = {
    "security/gunshot": ["gunshot", "gunfire", "firearm"],
    "security/explosion": ["explosion sound", "blast sound", "explosive sound"],
    "security/glass-breaking": ["glass break", "glass-breaking", "breaking glass"],
    "security/alarm": ["alarm sound", "siren detection", "alarm detection"],
    "human/baby-crying": ["baby cry", "infant cry", "neonatal cry"],
    "human/crying": ["crying sound", "human cry"],
    "human/screaming": ["scream detection", "screaming", "distress call"],
    "human/coughing": ["cough detection", "cough sound", "cough classification"],
    "human/snoring": ["snore", "snoring"],
    "animal/bird-sound": ["bird sound", "birdsong", "bird song", "avian vocal", "bioacoustic bird"],
    "animal/dog-barking": ["dog bark", "barking detection"],
    "animal/insect-sound": ["insect sound", "insect acoustic", "mosquito sound", "mosquito wingbeat"],
    "animal/marine-mammal": ["marine mammal", "whale vocal", "dolphin vocal", "cetacean"],
    "industrial/bearing": ["bearing fault", "bearing acoustic", "rotating machinery"],
    "industrial/motor": ["motor fault", "motor sound", "gearbox sound", "gear fault"],
    "industrial/conveyor": ["conveyor sound", "conveyor belt", "idler fault", "belt conveyor"],
    "industrial/mechanical-impact": ["mechanical sound", "machine sound", "mechanical impact", "industrial sound"],
    "transportation/road-vehicle": ["vehicle sound", "traffic sound", "engine sound", "road noise", "tire noise", "tyre noise"],
    "transportation/railway": ["railway sound", "train sound", "rail noise"],
    "transportation/aircraft-drone": ["aircraft sound", "aircraft noise", "drone sound", "uav acoustic", "drone detection"],
    "transportation/vessel": ["vessel classification", "vessel sound", "ship noise", "ship classification"],
    "environmental/rain-wind": ["rain sound", "wind sound", "rainfall acoustic"],
    "environmental/thunder": ["thunder sound", "thunder detection"],
    "environmental/water-flow": ["water sound", "water flow acoustic", "wave sound"],
    "medical/respiratory": ["respiratory sound", "lung sound", "breath sound", "wheeze", "crackle detection"],
    "medical/heart-sound": ["heart sound", "phonocardiogram", "cardiac auscultation"],
    "medical/sleep-sound": ["sleep sound", "sleep audio", "sleep apnea acoustic"],
    "urban/construction": ["construction sound", "construction noise"],
    "urban/public-warning": ["public warning sound", "emergency warning sound"],
    "urban/crowd": ["crowd sound", "crowd noise"],
    "domestic/door-event": ["door sound", "doorbell"],
    "domestic/footstep-fall": ["footstep sound", "fall detection audio", "footstep detection"],
    "domestic/appliance": ["appliance sound", "domestic sound", "home appliance"],
    "infrastructure/water-leakage": ["water leak", "water pipeline leak"],
    "infrastructure/gas-leakage": ["gas leak", "gas pipeline leak"],
    "infrastructure/structure": ["structural acoustic", "structural health monitoring acoustic", "acoustic emission structure"],
    "underwater/underwater-target": ["underwater target", "underwater acoustic classification", "sonar target"],
    "underwater/marine-life": ["underwater bioacoustic", "marine bioacoustic", "fish sound", "marine soundscape"],
    "agriculture/ecoacoustics": ["ecoacoustic", "soundscape ecology", "acoustic biodiversity"],
    "agriculture/livestock": ["livestock sound", "animal vocalization farm", "pig cough", "cattle vocal"],
}


def clean(value: str) -> str:
    return " ".join((value or "").split())


def fetch(start_date: str, end_date: str, batch: int, delay: float) -> list[dict]:
    query = f"cat:cs.SD AND submittedDate:[{start_date.replace('-', '')}0000 TO {end_date.replace('-', '')}2359]"
    rows, offset, total = [], 0, None
    while total is None or offset < total:
        params = urllib.parse.urlencode({"search_query": query, "start": offset, "max_results": batch, "sortBy": "submittedDate", "sortOrder": "ascending"})
        url = "https://export.arxiv.org/api/query?" + params
        last = None
        for attempt in range(5):
            try:
                result = subprocess.run(
                    ["curl", "-L", "--fail", "--silent", "--show-error", "--max-time", "180", "-A", UA["User-Agent"], url],
                    check=True, capture_output=True,
                )
                root = ET.fromstring(result.stdout)
                break
            except Exception as exc:
                last = exc
                time.sleep(5 * (attempt + 1))
        else:
            raise RuntimeError(f"arXiv request failed at offset {offset}: {last}")
        if total is None:
            total = int(root.findtext("o:totalResults", "0", ATOM))
        entries = root.findall("a:entry", ATOM)
        if not entries:
            break
        for entry in entries:
            raw_id = entry.findtext("a:id", "", ATOM).rsplit("/", 1)[-1]
            ident = re.sub(r"v\d+$", "", raw_id)
            cats = [node.attrib.get("term", "") for node in entry.findall("a:category", ATOM)]
            primary = entry.find("x:primary_category", ATOM)
            rows.append({
                "id": ident,
                "version": raw_id,
                "title": clean(entry.findtext("a:title", "", ATOM)),
                "authors": [clean(a.findtext("a:name", "", ATOM)) for a in entry.findall("a:author", ATOM)],
                "abstract": clean(entry.findtext("a:summary", "", ATOM)),
                "published": entry.findtext("a:published", "", ATOM),
                "updated": entry.findtext("a:updated", "", ATOM),
                "primary_category": primary.attrib.get("term", "") if primary is not None else "",
                "categories": cats,
                "abs_url": f"https://arxiv.org/abs/{ident}",
                "pdf_url": f"https://arxiv.org/pdf/{ident}",
            })
        offset += len(entries)
        print(json.dumps({"fetched": offset, "total": total}), flush=True)
        if offset < total:
            time.sleep(delay)
    # API results occasionally contain version duplicates; retain the newest record.
    dedup = {row["id"]: row for row in rows}
    return sorted(dedup.values(), key=lambda r: (r["published"], r["id"]))


def matches(text: str, terms: list[str]) -> list[str]:
    return [term for term in terms if term in text]


def classify(rows: list[dict]) -> tuple[dict, dict]:
    buckets = defaultdict(list)
    topics = defaultdict(list)
    for row in rows:
        text = (row["title"] + " " + row["abstract"]).casefold()
        row["repository_categories"] = []
        row["repository_topics"] = []
        row["classification_evidence"] = {}
        for slug, cfg in MAIN.items():
            evidence = matches(text, cfg["terms"])
            if evidence:
                row["repository_categories"].append(slug)
                row["classification_evidence"][slug] = evidence
                buckets[slug].append(row)
        for topic, terms in TOPICS.items():
            evidence = matches(text, terms)
            if evidence:
                row["repository_topics"].append(topic)
                row["classification_evidence"]["sound-event/" + topic] = evidence
                topics[topic].append(row)
                if "sound-event" not in row["repository_categories"]:
                    row["repository_categories"].append("sound-event")
                    buckets["sound-event"].append(row)
    return buckets, topics


def md_table(rows: list[dict], evidence_key: str | None = None) -> str:
    lines = ["| 日期 | arXiv ID | 论文 | 作者 | 分类依据 |", "|---|---|---|---|---|"]
    for row in rows:
        date = row["published"][:10]
        authors = ", ".join(row["authors"][:3]) + (" 等" if len(row["authors"]) > 3 else "")
        authors = authors.replace("|", "\\|")
        ev = "、".join(row["classification_evidence"].get(evidence_key, [])) if evidence_key else row["primary_category"]
        title = row["title"].replace("|", "\\|")
        lines.append(f"| {date} | [{row['id']}]({row['abs_url']}) | {title} | {authors} | {ev} |")
    return "\n".join(lines) + "\n"


def write_outputs(rows: list[dict], buckets: dict, topics: dict, start: str, end: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    generated = datetime.now(timezone.utc).isoformat()
    payload = {"scope": {"category": "cs.SD", "start": start, "end": end, "date_field": "submittedDate"}, "generated_at": generated, "count": len(rows), "records": rows}
    (OUT / "papers.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fields = ["id", "title", "authors", "published", "updated", "primary_category", "categories", "repository_categories", "repository_topics", "abs_url", "pdf_url", "abstract"]
    with (OUT / "papers.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            item = {k: row[k] for k in fields}
            for key in ("authors", "categories", "repository_categories", "repository_topics"):
                item[key] = "; ".join(item[key])
            writer.writerow(item)
    monthly = defaultdict(list)
    for row in rows:
        monthly[row["published"][:7]].append(row)
    for month, items in monthly.items():
        body = f"# arXiv cs.SD {month} 全量论文\n\n共 {len(items)} 篇；按 arXiv `submittedDate` 统计。\n\n" + md_table(items)
        (OUT / f"{month}.md").write_text(body, encoding="utf-8")
    category_counts = {slug: len(buckets.get(slug, [])) for slug in MAIN}
    topic_counts = {slug: len(topics.get(slug, [])) for slug in TOPICS}
    summary = [
        "# arXiv cs.SD 全量论文索引（2025-01-01—2026-11-03）", "",
        f"- 收录：**{len(rows)}** 篇（按 arXiv ID 去重）", f"- 数据口径：`cat:cs.SD AND submittedDate:[{start} TO {end}]`", "- 数据来源：arXiv 官方 API", "- 分类方法：标题与摘要的保守关键词匹配；可多标签；未命中论文仍保留在全量月表、CSV 和 JSON 中。", "",
        "## 月度目录", "", "| 月份 | 数量 | 索引 |", "|---|---:|---|",
    ]
    for month in sorted(monthly):
        summary.append(f"| {month} | {len(monthly[month])} | [{month}.md]({month}.md) |")
    summary += ["", "## 仓库主类分发", "", "| 类别 | 数量 |", "|---|---:|"]
    for slug, cfg in MAIN.items():
        summary.append(f"| [{cfg['title']}](../../{cfg['path']}) | {category_counts[slug]} |")
    summary += ["", "完整机器可读数据：[CSV](papers.csv) · [JSON](papers.json)", ""]
    (OUT / "README.md").write_text("\n".join(summary), encoding="utf-8")
    for slug, cfg in MAIN.items():
        items = sorted(buckets.get(slug, []), key=lambda r: (r["published"], r["id"]), reverse=True)
        path = ROOT / cfg["path"]
        intro = f"# {cfg['title']}：arXiv cs.SD 相关论文（2025-01-01—2026-11-03）\n\n共 {len(items)} 篇。由标题与摘要关键词自动初筛，可多类别收录；状态统一为 `to-reproduce`，建议在引用或形成趋势结论前人工复核。\n\n"
        path.write_text(intro + md_table(items, slug), encoding="utf-8")
    for topic, items in topics.items():
        path = ROOT / "papers" / "sound-event" / topic / "arxiv-cs-sd-2025-2026.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        title = topic.replace("/", " / ")
        intro = f"# {title}：arXiv cs.SD 相关论文（2025-01-01—2026-11-03）\n\n共 {len(items)} 篇。关键词自动初筛，状态为 `to-reproduce`；使用前请人工复核。\n\n"
        path.write_text(intro + md_table(sorted(items, key=lambda r: (r["published"], r["id"]), reverse=True), "sound-event/" + topic), encoding="utf-8")
    unmatched = [r for r in rows if not r["repository_categories"]]
    review = {
        "generated_at": generated,
        "method": "conservative keyword classification over title and abstract",
        "total": len(rows), "matched": len(rows) - len(unmatched), "unmatched": len(unmatched),
        "category_counts": category_counts, "topic_counts": topic_counts,
        "unmatched_records": [{"id": r["id"], "title": r["title"], "abs_url": r["abs_url"]} for r in unmatched],
    }
    (OUT / "classification-review.json").write_text(json.dumps(review, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"total": len(rows), "matched": len(rows) - len(unmatched), "unmatched": len(unmatched), "categories": category_counts, "topics_with_matches": sum(bool(v) for v in topic_counts.values())}, ensure_ascii=False))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", default="2025-01-01")
    parser.add_argument("--end", default="2026-11-03")
    parser.add_argument("--batch", type=int, default=500)
    parser.add_argument("--delay", type=float, default=3.2)
    parser.add_argument("--input-json", help="Regenerate indexes from an existing papers.json")
    args = parser.parse_args()
    if args.input_json:
        rows = json.loads(Path(args.input_json).read_text(encoding="utf-8"))["records"]
    else:
        rows = fetch(args.start, args.end, args.batch, args.delay)
    buckets, topics = classify(rows)
    write_outputs(rows, buckets, topics, args.start, args.end)


if __name__ == "__main__":
    main()

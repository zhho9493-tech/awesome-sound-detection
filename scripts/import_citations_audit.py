#!/usr/bin/env python3
"""Import missing, audited citation records into the repository master index."""

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "resources/paper-master-index.json"
MASTER_CSV = ROOT / "resources/paper-master-index.csv"
REPORT = ROOT / "resources/citations-csv-review.md"
IMPORT_DIR = ROOT / "papers/imported-citations"


def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", (value or "").casefold()).strip()


def category_for(row):
    text = " ".join((row.get("title", ""), row.get("publication", ""))).casefold()
    if any(term in text for term in ("speaker recognition", "speaker verification", "speaker diarization", "voiceprint")):
        return "speaker-recognition"
    if any(term in text for term in ("anomalous sound", "fault diagnosis", "machine condition", "machine anomaly", "acoustic anomaly")):
        return "acoustic-anomaly"
    if any(term in text for term in ("foundation model", "audio-language", "audio language model", "clap", "large audio model")):
        return "foundation-models"
    if any(term in text for term in ("distributed acoustic sensing", "fiber optic acoustic", "fibre optic acoustic", " das ")):
        return "das"
    if "leak" in text and any(term in text for term in ("acoustic", "sound", "audio", "pipeline", "water")):
        return "leakage"
    if any(term in text for term in ("face recognition", "facial recognition", "arcface")):
        return "face-recognition"
    if any(term in text for term in ("visual anomaly", "image anomaly", "surface defect")):
        return "visual-anomaly"
    if any(term in text for term in ("domain generalization", "domain adaptation", "transfer learning")) and not any(term in text for term in ("sound", "audio", "acoustic", "bioacoustic")):
        return "cross-domain"
    return "sound-event"


def record_id(title):
    return "citation-" + hashlib.sha1(norm(title).encode()).hexdigest()[:12]


def authors(value):
    return [name.strip() for name in (value or "").split(";") if name.strip()]


def export_csv(records):
    fields = [
        "id", "title", "primary_category", "related_categories", "source_sections",
        "public_url", "pdf_url", "doi", "arxiv_id", "drive_file_url",
        "drive_download_url", "download_url", "download_source", "download_access",
        "verification_status",
    ]
    with MASTER_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in records:
            writer.writerow({
                "id": row.get("id"),
                "title": row.get("title"),
                "primary_category": row.get("primary_category"),
                "related_categories": "|".join(row.get("related_categories", [])),
                "source_sections": "|".join(row.get("sources", [])),
                "public_url": row.get("public_url"),
                "pdf_url": row.get("pdf_url"),
                "doi": row.get("doi"),
                "arxiv_id": row.get("arxiv_id"),
                "drive_file_url": row.get("drive_file_url"),
                "drive_download_url": row.get("drive_download_url"),
                "download_url": row.get("download_url"),
                "download_source": row.get("download_source"),
                "download_access": row.get("download_access"),
                "verification_status": row.get("verification_status"),
            })


def link_for(row):
    if row.get("public_url"):
        return f'[{row["title"]}]({row["public_url"]})'
    return row["title"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("audit", type=Path)
    args = parser.parse_args()
    audit = json.loads(args.audit.read_text(encoding="utf-8"))
    data = json.loads(MASTER.read_text(encoding="utf-8"))
    records = [row for row in data["records"] if not str(row.get("id", "")).startswith("citation-")]
    data["records"] = records
    existing_titles = {norm(row.get("title")) for row in records}
    existing_ids = {row.get("id") for row in records}
    added = []
    for source in audit["records"]:
        if not source["status"].startswith("missing") or norm(source["title"]) in existing_titles:
            continue
        rid = record_id(source["title"])
        if rid in existing_ids:
            continue
        category = category_for(source)
        crossref = source.get("crossref") or {}
        year = source.get("year") if re.fullmatch(r"20\d{2}", source.get("year", "")) else crossref.get("year")
        verification = "crossref-verified" if source.get("verification") == "crossref-title-year" else (
            "official-url-verified" if source.get("verification") == "arxiv-id-from-citation" else "citation-metadata-reviewed"
        )
        row = {
            "id": rid,
            "title": source["title"],
            "primary_category": category,
            "related_categories": [],
            "sources": [f'citations.csv row {source["csv_row"]}', "resources/citations-csv-review.md"],
            "authors": authors(source.get("authors")),
            "publication": source.get("publication") or crossref.get("publication"),
            "year": year,
            "published": f"{year}-01-01" if year else None,
            "publisher": source.get("publisher") or crossref.get("publisher"),
            "public_url": source.get("public_url"),
            "pdf_url": source.get("pdf_url"),
            "doi": source.get("doi"),
            "arxiv_id": source.get("arxiv_id"),
            "verification_status": verification,
            "download_url": source.get("pdf_url"),
            "download_source": "arxiv" if source.get("pdf_url") else None,
            "download_access": "public" if source.get("pdf_url") else None,
        }
        records.append(row)
        added.append(row)
        existing_titles.add(norm(row["title"]))
        existing_ids.add(rid)

    data["generated_on"] = "2026-11-14"
    MASTER.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    export_csv(records)

    grouped = defaultdict(list)
    for row in added:
        grouped[row["primary_category"]].append(row)
    IMPORT_DIR.mkdir(parents=True, exist_ok=True)
    for category, rows in grouped.items():
        rows.sort(key=lambda row: (row.get("year") or "", row["title"]), reverse=True)
        lines = [
            f"# citations.csv 新增论文：{category}", "",
            f"共 {len(rows)} 篇。逐条与仓库主索引、arXiv 全量索引比对；公开标识不足的条目仅保存附件引文元数据。", "",
            "| 年份 | 论文 | 作者 | 出处 | 核验状态 |", "|---|---|---|---|---|",
        ]
        for row in rows:
            lines.append(f'| {row.get("year") or "—"} | {link_for(row)} | {", ".join(row.get("authors", [])[:3]) or "—"} | {row.get("publication") or "—"} | {row["verification_status"]} |')
        (IMPORT_DIR / f"{category}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    counts = Counter(row["primary_category"] for row in added)
    status_counts = Counter(row["verification_status"] for row in added)
    report = [
        "# citations.csv 逐篇复核报告", "",
        "- 复核日期：2026-11-14",
        f'- 原始引文：{audit["source_rows"]} 条',
        f'- 去重后论文：{audit["unique_titles"]} 篇',
        f'- 仓库已存在：{audit["status_counts"].get("present", 0)} 篇',
        f"- 本次新增：{len(added)} 篇",
        f'- 附件内重复：{len(audit["duplicate_rows"])} 条', "",
        "## 新增记录的核验层级", "",
    ]
    for status, count in sorted(status_counts.items()):
        report.append(f"- `{status}`：{count} 篇")
    report += ["", "## 新增记录的仓库分类", ""]
    for category, count in sorted(counts.items()):
        report.append(f"- [{category}](../papers/imported-citations/{category}.md)：{count} 篇")
    report += ["", "## 逐篇审计结果", "", "| CSV 行 | 论文 | 年份 | 结论 | 仓库对应 / 核验依据 |", "|---:|---|---:|---|---|"]
    for source in audit["records"]:
        if source["status"] == "present":
            match = source["repository_match"]
            evidence = f'{match["method"]}：{match["title"]}（{match.get("id") or "无 ID"}）'
            conclusion = "已存在"
        else:
            evidence = source.get("verification", "citation-row-only")
            if source.get("doi"):
                evidence += f'；DOI {source["doi"]}'
            if source.get("arxiv_id"):
                evidence += f'；arXiv {source["arxiv_id"]}'
            conclusion = "已新增"
        report.append(f'| {source["csv_row"]} | {source["title"]} | {source.get("year") or "—"} | {conclusion} | {evidence} |')
    REPORT.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(json.dumps({"added": len(added), "categories": counts, "verification": status_counts}, ensure_ascii=False, default=dict))


if __name__ == "__main__":
    main()

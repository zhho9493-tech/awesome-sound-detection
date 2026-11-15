#!/usr/bin/env python3
"""Rebuild the complete, year-grouped paper section in the SED README."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "papers/sound-event/README.md"
PUBLIC_INDEX = ROOT / "portal/data/papers.json"
START = "## 04 · 论文详情"
END = "## 评估与维护约定"


PROBLEMS = [
    ("少样本", ("few-shot", "few shot", "one-shot", "low-resource", "limited label")),
    ("半/弱监督", ("weakly supervised", "weak supervision", "semi-supervised", "pseudo-label", "self-training")),
    ("跨域泛化", ("domain adaptation", "domain generalization", "domain shift", "cross-domain", "cross domain")),
    ("长尾与不平衡", ("long-tail", "long tailed", "long-tailed", "class imbalance", "imbalanced")),
    ("低信噪比", ("low snr", "low-snr", "noise robust", "noise-aware", "denoising", "noisy")),
    ("开放集/OOD", ("open-set", "open set", "open-world", "out-of-distribution", "unknown class", "zero-shot")),
    ("持续学习", ("continual learning", "incremental learning", "class-incremental", "domain-incremental", "lifelong")),
    ("定位与分离", ("localization", "separation", "source separation", "spatial audio", "sound event localization")),
    ("多模态与基础模型", ("audio-language", "audio language", "foundation model", "clap", "multimodal", "large audio")),
    ("可解释与可靠性", ("explain", "uncertainty", "calibration", "trustworthy", "reliability", "confidence")),
    ("轻量化部署", ("lightweight", "edge", "embedded", "efficient", "compression", "distillation")),
]

SCENES = [
    ("生态与动物声音", ("bird", "animal", "bioacoustic", "biodiversity", "wildlife", "insect", "whale", "dolphin")),
    ("医疗与生理声音", ("respiratory", "lung sound", "heart sound", "cough", "snore", "medical", "clinical")),
    ("工业与机械声音", ("machine", "industrial", "fault", "bearing", "gear", "motor", "mechanical")),
    ("交通与水下声音", ("vehicle", "traffic", "vessel", "underwater", "maritime", "aircraft", "drone")),
    ("环境与城市声音", ("environmental sound", "urban", "soundscape", "acoustic scene", "ambient")),
]

METHODS = [
    ("音频语言模型", ("audio-language", "audio language", "clap", "language model")),
    ("自监督表征", ("self-supervised", "self supervised")),
    ("Transformer 表征", ("transformer", "conformer", "attention")),
    ("对比与原型学习", ("contrastive", "prototype", "metric learning")),
    ("层级与多任务学习", ("hierarchical", "multi-task", "multitask")),
    ("数据增强与生成", ("augmentation", "synthetic", "diffusion", "generative")),
]


def clean(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def is_sed(row: dict) -> bool:
    return any(x in {"sound-event", "sed"} for x in row.get("categories", []))


def safe_url(value: object) -> str:
    url = clean(value)
    return url if re.match(r"^https://(?:arxiv\.org|doi\.org|openreview\.net)/", url) else ""


def record_year(row: dict) -> str:
    explicit = clean(row.get("year")) or clean(row.get("published"))[:4]
    if re.fullmatch(r"(?:19|20)\d{2}", explicit):
        return explicit
    arxiv = clean(row.get("arxiv_id"))
    match = re.match(r"(\d{2})(?:0[1-9]|1[0-2])\.\d{4,5}", arxiv)
    if match:
        value = int(match.group(1))
        return str(2000 + value if value < 91 else 1900 + value)
    return "年份待核验"


def problem_tags(row: dict) -> list[str]:
    text = clean(" ".join([row.get("title", ""), row.get("abstract", "")])).lower()
    tags = [name for name, terms in PROBLEMS if any(term in text for term in terms)]
    return tags[:4] or ["通用检测与分类"]


def chinese_summary(row: dict) -> str:
    text = clean(" ".join([row.get("title", ""), row.get("abstract", "")])).lower()
    scene = next((name for name, terms in SCENES if any(term in text for term in terms)), "声音事件")
    method = next((name for name, terms in METHODS if any(term in text for term in terms)), "数据驱动方法")
    tags = problem_tags(row)
    if tags != ["通用检测与分类"]:
        result = f"采用{method}，面向{scene}解决{tags[0]}问题。"
    else:
        result = f"采用{method}开展{scene}检测、分类或表征研究。"
    return result[:39] + ("。" if not result[:39].endswith("。") else "")


def paper_markdown(row: dict) -> str:
    title = clean(row.get("title")) or "题名待核验"
    date = clean(row.get("published") or row.get("year")) or "日期待核验"
    tags = " · ".join(problem_tags(row))
    url = safe_url(row.get("url"))
    pdf = safe_url(row.get("pdf_url"))
    arxiv = clean(row.get("arxiv_id"))
    doi = clean(row.get("doi"))
    identity = f"arXiv {arxiv}" if arxiv else (f"DOI {doi}" if doi else "题名级候选，身份待核验")
    heading = f"#### [{title}]({url})" if url else f"#### {title}"
    links = []
    if url:
        links.append(f"[论文主页]({url})")
    if pdf:
        links.append(f"[PDF]({pdf})")
    links.append(identity)
    return "\n".join([
        heading,
        "",
        f"- **日期：** {date}",
        f"- **问题 / 中文简述：** {tags}；{chinese_summary(row)}",
        f"- **来源：** {' · '.join(links)}",
        "",
    ])


def build_section(rows: list[dict]) -> str:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        year = record_year(row)
        grouped[year].append(row)
    years = sorted(grouped, key=lambda x: (x != "年份待核验", x), reverse=True)
    counts = Counter(tag for row in rows for tag in problem_tags(row))
    lines = [
        START,
        "",
        f"本节收录当前统一索引中归入声音事件检测方向的 **{len(rows):,} 篇论文**。论文按年份分组、年份默认折叠；展开后按日期从最新到最旧排列。",
        "",
        "> 中文简述由论文题目与公开摘要中的方法、场景和问题标签生成，用于快速浏览；题名级候选与自动归类仍需结合原文复核。",
        "",
        "**问题分布：** " + " · ".join(f"{name} {count:,}" for name, count in counts.most_common()),
        "",
    ]
    for year in years:
        items = sorted(grouped[year], key=lambda r: (clean(r.get("published") or r.get("year")), clean(r.get("title"))), reverse=True)
        label = year if year == "年份待核验" else f"{year} 年"
        lines.extend(["<details>", f"<summary><strong>{label}（{len(items):,} 篇）</strong></summary>", ""])
        for row in items:
            lines.append(paper_markdown(row))
        lines.extend(["</details>", ""])
    lines.extend([
        "### 论文索引与筛选入口",
        "",
        "- [交互专题页：按问题、年份和技术趋势筛选](../../portal/topic.html?topic=sed#details)",
        "- [arXiv cs.SD 2025-01-01—2026-11-03 相关论文初筛](arxiv-cs-sd-2025-2026.md)",
        "- [通用 SED 方法与未细分候选](methods/README.md)",
        "",
        "---",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts/build_paper_discovery.py")], cwd=ROOT, check=True)
    payload = json.loads(PUBLIC_INDEX.read_text(encoding="utf-8"))
    rows = [row for row in payload.get("records", []) if is_sed(row)]
    rows.sort(key=lambda r: (clean(r.get("published") or r.get("year")), clean(r.get("title"))), reverse=True)
    source = README.read_text(encoding="utf-8")
    start = source.index(START)
    end = source.index(END, start)
    updated = source[:start] + build_section(rows) + source[end:]
    README.write_text(updated.rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {len(rows):,} SED papers across {len({record_year(r) for r in rows})} year groups to {README}")


if __name__ == "__main__":
    main()

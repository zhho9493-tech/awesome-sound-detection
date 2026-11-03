#!/usr/bin/env python3
"""Audit arXiv-backed paper records and optionally add missing PDF URLs."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT_JSON = ROOT / "resources" / "arxiv-pdf-link-audit.json"
REPORT_MD = ROOT / "resources" / "arxiv-pdf-link-audit.md"
ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/((?:\d{4}\.\d{4,5})(?:v\d+)?)", re.I)


def base_id(value: str) -> str:
    match = ID_RE.search(value or "")
    raw = match.group(1) if match else (value or "")
    return re.sub(r"v\d+$", "", raw)


def verify_pdf(arxiv_id: str) -> dict:
    url = f"https://arxiv.org/pdf/{arxiv_id}"
    result = subprocess.run(
        ["curl", "-L", "--fail", "--silent", "--show-error", "--range", "0-7", "--max-time", "30", url],
        capture_output=True,
    )
    return {
        "url": url,
        "available": result.returncode == 0 and result.stdout.startswith(b"%PDF"),
        "verification": "official-pdf-signature" if result.returncode == 0 and result.stdout.startswith(b"%PDF") else "unavailable",
        "error": result.stderr.decode("utf-8", "replace").strip()[:300] or None,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fix", action="store_true", help="add verified pdf_url fields to resources/catalog.json")
    parser.add_argument("--no-network", action="store_true", help="report candidates without checking remote PDFs")
    args = parser.parse_args()

    master = json.loads((ROOT / "resources/paper-master-index.json").read_text(encoding="utf-8"))["records"]
    cs_sd = json.loads((ROOT / "resources/arxiv-cs-sd/papers.json").read_text(encoding="utf-8"))["records"]
    catalog_path = ROOT / "resources/catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))

    structured = []
    for source, rows in (("paper-master-index", master), ("arxiv-cs-sd", cs_sd)):
        for row in rows:
            ident = base_id(row.get("arxiv_id") or row.get("abs_url") or row.get("public_url") or "")
            if not re.fullmatch(r"\d{4}\.\d{4,5}", ident):
                continue
            structured.append({
                "source": source,
                "id": ident,
                "title": row.get("title"),
                "pdf_url": row.get("pdf_url"),
            })

    missing = []
    for item in catalog["resources"]:
        if item.get("type") != "paper":
            continue
        ident = base_id(item.get("url", ""))
        if not re.fullmatch(r"\d{4}\.\d{4,5}", ident):
            continue
        if not item.get("pdf_url"):
            candidate = {"source": "catalog", "resource_id": item["id"], "id": ident, "title": item["title"]}
            candidate.update({"url": f"https://arxiv.org/pdf/{ident}", "available": None, "verification": "not-checked", "error": None} if args.no_network else verify_pdf(ident))
            missing.append(candidate)
            if args.fix and candidate["available"]:
                item["pdf_url"] = candidate["url"]

    if args.fix:
        catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    structured_missing = [r for r in structured if not r["pdf_url"]]
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scope": "structured arXiv paper records plus catalog paper resources; review candidates are excluded",
        "structured_arxiv_records": len(structured),
        "structured_unique_arxiv_ids": len({r["id"] for r in structured}),
        "structured_missing_pdf_url": len(structured_missing),
        "catalog_missing_before_fix": len(missing),
        "catalog_verified_available": sum(r["available"] is True for r in missing),
        "catalog_unavailable": sum(r["available"] is False for r in missing),
        "fixed": bool(args.fix),
        "structured_missing_records": structured_missing,
        "catalog_candidates": missing,
    }
    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# arXiv PDF 下载链接审计", "",
        f"- 结构化 arXiv 论文记录：{report['structured_arxiv_records']} 条，{report['structured_unique_arxiv_ids']} 个唯一 ID。",
        f"- 结构化记录缺失 PDF 字段：**{report['structured_missing_pdf_url']}** 条。",
        f"- 资源目录此前只有摘要页、缺少 PDF 字段：**{report['catalog_missing_before_fix']}** 条。",
        f"- 经 arXiv 官方 PDF 文件头验证可下载：**{report['catalog_verified_available']}** 条；不可下载：**{report['catalog_unavailable']}** 条。", "",
        "## 已核验条目", "", "| arXiv ID | 论文 | 官方 PDF | 验证结果 |", "|---|---|---|---|",
    ]
    for row in missing:
        status = "可下载，已补齐" if row["available"] and args.fix else ("可下载" if row["available"] else "不可下载")
        lines.append(f"| [{row['id']}](https://arxiv.org/abs/{row['id']}) | {row['title']} | [PDF]({row['url']}) | {status} |")
    lines += ["", "## 口径", "", "仅把正式收录的结构化论文记录和 `catalog.json` 中 `type=paper` 的资源作为论文；`arxiv-match-review.json` 中尚待人工确认的候选不计入缺失。PDF 可用性通过 arXiv 官方地址返回的 `%PDF` 文件签名验证。", ""]
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("structured_arxiv_records", "structured_unique_arxiv_ids", "structured_missing_pdf_url", "catalog_missing_before_fix", "catalog_verified_available", "catalog_unavailable")}, ensure_ascii=False))


if __name__ == "__main__":
    main()

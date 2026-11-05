#!/usr/bin/env python3
"""Find verified, free arXiv PDFs for master-index records missing public links.

Queries are batched to respect arXiv's request interval. Matches require a strong
normalized full-title similarity, and every selected PDF is checked for a PDF
file signature before it can be written to the index.
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import ssl
import subprocess
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

from verify_arxiv_index import export_csv

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "resources/paper-master-index.json"
CACHE = ROOT / "resources/public-pdf-audit-cache.json"
REPORT_JSON = ROOT / "resources/public-pdf-audit.json"
REPORT_MD = ROOT / "resources/public-pdf-audit.md"
ATOM = {"a": "http://www.w3.org/2005/Atom"}
AGENT = "awesome-sound-detection-public-pdf-audit/1.0"


def tls_context() -> ssl.SSLContext:
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


def norm(value: str) -> str:
    value = re.sub(r"^20\d\d[-_/]\d\d[-_/]\d\d[-\s_]*", "", value)
    value = re.sub(r"(?i)(?:[-_ ]rank[-_ ]*\d+|[-_ ]copy|_\d+)+$", "", value)
    value = re.sub(r"(?i)(?:_summary)?\.(?:md|pdf)$", "", value)
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", value.casefold())).strip()


def query_batch(titles: list[str]) -> list[dict]:
    clauses = []
    for title in titles:
        words = norm(title).split()[:9]
        clauses.append('ti:"' + " ".join(words).replace('"', "") + '"')
    params = urllib.parse.urlencode({"search_query": " OR ".join(clauses), "start": 0, "max_results": 50})
    request = urllib.request.Request("https://export.arxiv.org/api/query?" + params, headers={"User-Agent": AGENT})
    with urllib.request.urlopen(request, timeout=60, context=tls_context()) as response:
        root = ET.fromstring(response.read())
    results = []
    for entry in root.findall("a:entry", ATOM):
        title = " ".join(entry.findtext("a:title", default="", namespaces=ATOM).split())
        link = entry.findtext("a:id", default="", namespaces=ATOM)
        match = re.search(r"/(?:abs|pdf)/((?:\d{4}\.\d{4,5}|[a-z.\-]+/\d{7})(?:v\d+)?)", link)
        if match:
            results.append({"title": title, "arxiv_id": re.sub(r"v\d+$", "", match.group(1))})
    return results


def verify_pdf(arxiv_id: str) -> bool:
    result = subprocess.run(
        ["curl", "-L", "--fail", "--silent", "--show-error", "--range", "0-7", "--max-time", "30", f"https://arxiv.org/pdf/{arxiv_id}"],
        capture_output=True,
    )
    return result.returncode == 0 and result.stdout.startswith(b"%PDF")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fix", action="store_true")
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--delay", type=float, default=3.2)
    args = parser.parse_args()

    data = json.loads(DB.read_text(encoding="utf-8"))
    rows = data["records"]
    missing = [row for row in rows if not row.get("pdf_url")]
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {"titles": {}}
    title_cache = cache.setdefault("titles", {})
    representatives: dict[str, str] = {}
    for row in missing:
        representatives.setdefault(norm(row["title"]), row["title"])
    pending = [title for key, title in representatives.items() if key not in title_cache or title_cache[key].get("status") == "retry"]

    for offset in range(0, len(pending), args.batch_size):
        batch = pending[offset : offset + args.batch_size]
        try:
            candidates = query_batch(batch)
            for title in batch:
                scored = sorted(
                    ({**candidate, "similarity": round(difflib.SequenceMatcher(None, norm(title), norm(candidate["title"])).ratio(), 4)} for candidate in candidates),
                    key=lambda item: -item["similarity"],
                )
                top = scored[0] if scored else None
                if top and top["similarity"] >= 0.96 and (len(scored) == 1 or scored[1]["similarity"] < 0.94):
                    title_cache[norm(title)] = {"status": "candidate", **top}
                else:
                    title_cache[norm(title)] = {"status": "not-found", "candidates": scored[:3]}
        except Exception as exc:
            for title in batch:
                title_cache[norm(title)] = {"status": "retry", "error": str(exc)[:300]}
        CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if offset + args.batch_size < len(pending):
            time.sleep(max(3.0, args.delay))

    verified_ids: dict[str, bool] = {}
    matched = []
    for row in missing:
        result = title_cache.get(norm(row["title"]), {})
        if result.get("status") != "candidate":
            continue
        arxiv_id = result["arxiv_id"]
        if arxiv_id not in verified_ids:
            verified_ids[arxiv_id] = verify_pdf(arxiv_id)
        if not verified_ids[arxiv_id]:
            continue
        item = {"record_id": row["id"], "title": row["title"], "arxiv_title": result["title"], "similarity": result["similarity"], "arxiv_id": arxiv_id, "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}"}
        matched.append(item)
        if args.fix:
            row.update({"arxiv_id": arxiv_id, "public_url": f"https://arxiv.org/abs/{arxiv_id}", "pdf_url": item["pdf_url"], "download_url": item["pdf_url"], "download_source": "arxiv", "download_access": "open", "verification_status": "official-url-verified"})

    if args.fix:
        DB.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        export_csv(rows)
    status_counts: dict[str, int] = {}
    for value in title_cache.values():
        status_counts[value.get("status", "unknown")] = status_counts.get(value.get("status", "unknown"), 0) + 1
    report = {"generated_at": datetime.now(timezone.utc).isoformat(), "scope": "paper-master-index records missing public pdf_url", "records_checked": len(missing), "unique_normalized_titles": len(representatives), "source": "arXiv official API and PDF endpoint", "match_rule": "normalized full-title similarity >= 0.96, unambiguous runner-up, PDF signature verified", "status_counts": status_counts, "verified_free_pdf_records": len(matched), "remaining_without_public_pdf": len(missing) - len(matched), "fixed": args.fix, "matches": matched}
    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# 缺失公开 PDF 链接复核", "", f"- 复核记录：**{len(missing)}** 条；标准化后唯一标题：**{len(representatives)}** 个。", f"- 经标题精确匹配及 PDF 文件签名验证，可从 arXiv 免费下载：**{len(matched)}** 条。", f"- 本轮仍未找到可安全自动确认的公开 PDF：**{len(missing)-len(matched)}** 条。", "", "## 已补充", "", "| 仓库论文 | arXiv 论文 | 相似度 | 免费 PDF |", "|---|---|---:|---|"]
    for item in matched:
        lines.append(f"| {item['title']} | [{item['arxiv_title']}](https://arxiv.org/abs/{item['arxiv_id']}) | {item['similarity']:.4f} | [PDF]({item['pdf_url']}) |")
    lines += ["", "## 核验规则", "", "仅自动接受标准化完整标题相似度不低于 0.96、无竞争候选且官方 PDF 返回 `%PDF` 文件签名的结果。未匹配不代表论文不存在，只表示本轮未在 arXiv 找到可安全自动确认的免费全文；私人网盘不作为公开下载来源。", ""]
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("records_checked", "unique_normalized_titles", "verified_free_pdf_records", "remaining_without_public_pdf")}, ensure_ascii=False))


if __name__ == "__main__":
    main()

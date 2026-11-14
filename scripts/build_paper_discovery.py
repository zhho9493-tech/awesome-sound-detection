#!/usr/bin/env python3
"""Build a public, read-only paper discovery index from two existing source indexes.

Never mutates source data. Merge only on exact normalized DOI or arXiv ID.
Title similarity is NOT identity verification. Private Drive URLs are excluded.
"""
import argparse
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "resources/paper-master-index.json"
ARXIV = ROOT / "resources/arxiv-cs-sd/papers.json"
OUTPUT = ROOT / "portal/data/papers.json"

def s(v):
    return " ".join(str(v or "").split())

def aid(value):
    v = s(value)
    m = re.search(r"(?:arxiv\.org/(?:abs|pdf)/|arxiv:)?((?:\d{4}\.\d{4,5}|[a-z-]+(?:\.[A-Z]{2})?/\d{7}))(?:v\d+)?", v, re.I)
    return m.group(1).lower() if m else ""

def doi(value):
    v = s(value).lower().replace("https://doi.org/", "").replace("http://dx.doi.org/", "").replace("doi:", "").strip()
    return v if re.fullmatch(r"10\.\d{4,9}/\S+",v) else ""

def clean_url(value, allowed):
    v = s(value)
    if not v.startswith("https://"):
        return ""
    if any(v.lower().startswith("https://" + host + "/") for host in allowed):
        return v
    return ""

def cat(value):
    if not value:
        return []
    if isinstance(value, str):
        return [x.strip() for x in re.split(r"[;,]", value) if x.strip()]
    return [s(x) for x in value if s(x)] if isinstance(value,list) else []

def main():
    m = json.loads(MASTER.read_text(encoding="utf-8"))
    a = json.loads(ARXIV.read_text(encoding="utf-8"))
    masters = m["records"]
    arxivs = a["records"]
    out = {}
    mapping = {}
    ambiguous = []
    def ingest(row, origin, index):
        title = s(row.get("title"))
        if not title:
            return
        raw_arxiv = aid(row.get("arxiv_id") or (row.get("id") if origin=="arxiv" else "") or row.get("abs_url"))
        raw_doi = doi(row.get("doi"))
        canonical = "doi:"+raw_doi if raw_doi else ("arxiv:"+raw_arxiv if raw_arxiv else origin+":"+s(row.get("id") or index))
        aliases = [x for x in ["doi:"+raw_doi if raw_doi else "", "arxiv:"+raw_arxiv if raw_arxiv else ""] if x]
        existing = {mapping[x] for x in aliases if x in mapping}
        if len(existing)>1:
            ambiguous.append({"source":origin,"source_id":s(row.get("id")),"reason":"conflicting identifiers"})
            return
        key = next(iter(existing)) if existing else canonical
        entry = out.get(key)
        if entry is None:
            entry = {"id":key,"title":title,"year":"","published":"","authors":[],"abstract":"","categories":[],"topics":[],"sources":[],"doi":"","arxiv_id":"","url":"","pdf_url":"","verification_status":"candidate","identity_status":"source-record-only"}
            out[key] = entry
        if not any(src["dataset"] == origin for src in entry["sources"]):
            entry["sources"].append({"dataset":origin})
        if raw_doi: entry["doi"]=raw_doi
        if raw_arxiv: entry["arxiv_id"]=raw_arxiv
        if entry["doi"] or entry["arxiv_id"]: entry["identity_status"]="identifier-present"
        if origin=="arxiv":
            entry["published"]=s(row.get("published"))[:10]
            entry["year"]=entry["published"][:4]
            entry["authors"]=row.get("authors") if isinstance(row.get("authors"), list) else []
            entry["abstract"]=s(row.get("abstract"))[:1600]
            entry["categories"]=sorted(set(entry["categories"]+cat(row.get("repository_categories"))))
            entry["topics"]=sorted(set(entry["topics"]+cat(row.get("repository_topics"))))
            if raw_arxiv:
                entry["url"]="https://arxiv.org/abs/"+raw_arxiv
                entry["pdf_url"]="https://arxiv.org/pdf/"+raw_arxiv
        else:
            entry["categories"]=sorted(set(entry["categories"]+cat(row.get("primary_category"))+cat(row.get("related_categories"))))
            entry["verification_status"]=s(row.get("verification_status")) or "candidate"
            if not entry["url"]:
                entry["url"]=clean_url(row.get("public_url"),("arxiv.org","doi.org","openreview.net"))
            if not entry["pdf_url"]:
                entry["pdf_url"]=clean_url(row.get("pdf_url"),("arxiv.org","openreview.net"))
        for alias in aliases: mapping[alias]=key
    for i,row in enumerate(masters): ingest(row,"master",i)
    for i,row in enumerate(arxivs): ingest(row,"arxiv",i)
    # No private file URLs, IDs, download endpoints, or source directory names exported.
    rows=sorted(out.values(),key=lambda x:(x.get("published",""),x["title"].casefold()),reverse=True)
    stats=Counter(key for r in rows for key in r["categories"])
    payload={"schema_version":"1.0.0","generated_at":datetime.now(timezone.utc).isoformat(),"source_counts":{"master":len(masters),"arxiv":len(arxivs)},"record_count":len(rows),"note":"Exact DOI/arXiv identifiers only. Title-only duplicates are intentionally not merged; identity_status=identifier-present does not imply full bibliographic verification.","category_counts":dict(stats),"conflict_count":len(ambiguous),"records":rows}
    OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    OUTPUT.write_text(json.dumps(payload,ensure_ascii=False,separators=(",",":"))+"\n",encoding="utf-8")
    print(f"Exported {len(rows)} public records, {len(ambiguous)} identifier conflicts to {OUTPUT}")
    if ambiguous:
        raise SystemExit("Identifier conflicts require manual review; existing export generated but CI fails.")

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.parse_args()
    main()

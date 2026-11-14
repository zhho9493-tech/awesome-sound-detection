#!/usr/bin/env python3
"""Audit a citation CSV against the repository and verify missing titles with Crossref."""

import argparse
import concurrent.futures
import csv
import difflib
import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = "awesome-sound-detection-citation-audit/1.0"
TITLE_ALIASES = {
    "fa3 net feature aggregation and augmentation with attention network for sound event localization and detection c wang and q hunag":
        "fa3 net feature aggregation and augmentation with attention network for sound event localization and detection applied intelligence",
    "frequency tracking features for domain robust and data efficient deep siren identification":
        "frequency tracking features for data efficient deep siren identification",
    "adaptive vehicle speed classification via multi feature cnn with reinforcement learning enhanced acoustic processing":
        "adaptive vehicle speed classification via bmcnn with reinforcement learning enhanced acoustic processing",
    "cycleguardian a framework for automatic respiratory sound classification based on improved deep clustering and contrastive learning":
        "cycleguardian a framework for automatic respiratorysound classification based on improved deep clustering and contrastive learning",
    "use of iot with deep learning for classification of environment sounds and detection of gases":
        "use of iot with deep learning for classification of environmental sound and detection of gases",
}


def norm(value):
    value = unicodedata.normalize("NFKD", value or "").casefold()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def year_of_crossref(item):
    for key in ("published-print", "published-online", "published", "issued", "created"):
        parts = item.get(key, {}).get("date-parts", [])
        if parts and parts[0]:
            return str(parts[0][0])
    return ""


def crossref_lookup(title, year):
    params = urllib.parse.urlencode({
        "query.title": title,
        "rows": 5,
        "select": "DOI,title,author,published,published-print,published-online,issued,created,URL,publisher,container-title,type",
    })
    request = urllib.request.Request(
        "https://api.crossref.org/works?" + params,
        headers={"User-Agent": UA, "Accept": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=8) as response:
        items = json.load(response)["message"]["items"]
    wanted = norm(title)
    candidates = []
    for item in items:
        candidate_title = " ".join(item.get("title") or [])
        similarity = difflib.SequenceMatcher(None, wanted, norm(candidate_title)).ratio()
        candidate_year = year_of_crossref(item)
        candidates.append((similarity, candidate_year == str(year), candidate_title, candidate_year, item))
    candidates.sort(key=lambda row: (row[0], row[1]), reverse=True)
    if not candidates:
        return None
    similarity, same_year, candidate_title, candidate_year, item = candidates[0]
    accepted = similarity >= 0.96 or (similarity >= 0.91 and same_year)
    return {
        "accepted": accepted,
        "similarity": round(similarity, 4),
        "title": candidate_title,
        "year": candidate_year,
        "doi": item.get("DOI"),
        "url": item.get("URL"),
        "publisher": item.get("publisher"),
        "publication": " ".join(item.get("container-title") or []),
        "type": item.get("type"),
    }


def repository_titles():
    master = json.loads((ROOT / "resources/paper-master-index.json").read_text(encoding="utf-8"))["records"]
    arxiv = json.loads((ROOT / "resources/arxiv-cs-sd/papers.json").read_text(encoding="utf-8"))["records"]
    rows = []
    for source, records in (("master", master), ("arxiv-cs-sd", arxiv)):
        for row in records:
            if str(row.get("id", "")).startswith("citation-"):
                continue
            title = row.get("title") or ""
            if title:
                rows.append({
                    "normalized": norm(title),
                    "title": title,
                    "id": row.get("arxiv_id") or row.get("id"),
                    "source": source,
                })
    return rows


def existing_match(title, repository):
    wanted = norm(title)
    alias = TITLE_ALIASES.get(wanted)
    if alias:
        matched = next((row for row in repository if row["normalized"] == alias), None)
        if matched:
            return {"method": "manually-reviewed-title-variant", **matched}
    exact = [row for row in repository if row["normalized"] == wanted]
    if exact:
        return {"method": "normalized-title-exact", **exact[0]}
    contained = [
        row for row in repository
        if len(wanted) >= 30 and len(row["normalized"]) >= 30
        and (wanted in row["normalized"] or row["normalized"] in wanted)
    ]
    if contained:
        contained.sort(key=lambda row: abs(len(row["normalized"]) - len(wanted)))
        return {"method": "normalized-title-containment", **contained[0]}
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT / "resources/citations-csv-audit.json")
    parser.add_argument("--cache", type=Path, default=ROOT / "resources/crossref-title-cache.json")
    parser.add_argument("--delay", type=float, default=0.12)
    args = parser.parse_args()

    with args.csv_path.open(encoding="utf-8-sig", newline="") as handle:
        source_rows = list(csv.DictReader(handle))
    unique = {}
    duplicates = []
    for index, row in enumerate(source_rows, 2):
        key = norm(row.get("Title"))
        if key in unique:
            duplicates.append({"row": index, "title": row.get("Title"), "duplicate_of": unique[key][0]})
        else:
            unique[key] = (index, row)

    repository = repository_titles()
    cache = json.loads(args.cache.read_text(encoding="utf-8")) if args.cache.exists() else {}
    pending = []
    for key, (_, row) in unique.items():
        if key in cache or existing_match(row.get("Title"), repository):
            continue
        if re.search(r"arxiv\s*:?\s*\d{4}\.\d{4,5}", row.get("Publication", ""), re.I):
            continue
        pending.append((key, row.get("Title", ""), row.get("Year", "")))

    def fetch(entry):
        key, title, year = entry
        try:
            return key, {"result": crossref_lookup(title, year)}
        except Exception as exc:
            return key, {"error": str(exc)[:300]}

    if pending:
        print(f"crossref pending {len(pending)}")
        with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
            for completed, (key, value) in enumerate(executor.map(fetch, pending), 1):
                cache[key] = value
                if completed % 10 == 0:
                    args.cache.write_text(json.dumps(cache, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                    print(f"crossref verified {completed}/{len(pending)}")
        args.cache.write_text(json.dumps(cache, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    audited = []
    for position, (key, (row_number, row)) in enumerate(unique.items(), 1):
        match = existing_match(row.get("Title"), repository)
        result = {
            "csv_row": row_number,
            "title": row.get("Title", ""),
            "authors": row.get("Authors", ""),
            "publication": row.get("Publication", ""),
            "year": row.get("Year", ""),
            "publisher": row.get("Publisher", ""),
        }
        if match:
            result.update({"status": "present", "repository_match": match})
        else:
            arxiv_match = re.search(r"arxiv\s*:?\s*(\d{4}\.\d{4,5})", row.get("Publication", ""), re.I)
            if arxiv_match:
                aid = arxiv_match.group(1)
                result.update({
                    "status": "missing-verified",
                    "verification": "arxiv-id-from-citation",
                    "arxiv_id": aid,
                    "public_url": f"https://arxiv.org/abs/{aid}",
                    "pdf_url": f"https://arxiv.org/pdf/{aid}",
                })
            else:
                crossref = cache.get(key, {}).get("result")
                if crossref and crossref.get("accepted"):
                    result.update({
                        "status": "missing-verified",
                        "verification": "crossref-title-year",
                        "crossref": crossref,
                        "doi": crossref.get("doi"),
                        "public_url": crossref.get("url"),
                    })
                else:
                    result.update({
                        "status": "missing-citation-reviewed",
                        "verification": "citation-row-only",
                        "crossref_candidate": crossref,
                    })
        audited.append(result)
        if position % 50 == 0:
            print(f"audited {position}/{len(unique)}", flush=True)

    counts = {}
    for row in audited:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    output = {
        "source_file": args.csv_path.name,
        "source_rows": len(source_rows),
        "unique_titles": len(unique),
        "duplicate_rows": duplicates,
        "status_counts": counts,
        "records": audited,
    }
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(counts, ensure_ascii=False))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Conservatively resolve unambiguous, truncated-title arXiv review candidates.
Preserves existing Drive provenance. Does not treat missing arXiv as nonexistence.
"""
import csv,json,re,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DB=ROOT/"resources/paper-master-index.json"
REPORT=ROOT/"resources/arxiv-match-review.json"
def norm(s):
    s=re.sub(r"^20\d\d[-_/]\d\d[-_/]\d\d[-\s]*","",s)
    return re.sub(r"\s+"," ",re.sub(r"[^a-z0-9]+"," ",s.casefold())).strip()
def main():
    db=json.loads(DB.read_text(encoding="utf-8"))
    report=json.loads(REPORT.read_text(encoding="utf-8"))
    rows={r["id"]:r for r in db["records"]}
    changed=[]
    for item in report.get("manual_review",[]):
        if item.get("decision")!="manual-review":continue
        candidates=item.get("candidates",[])
        if len(candidates)!=1:continue # identical-title arXiv duplicates are ambiguous
        candidate=candidates[0]
        title=norm(item["title"]);full=norm(candidate["arxiv_title"])
        # Minimum substantial clean title-prefix match; exclude rankings/suffixes.
        if len(title)<52 or len(title.split())<8:continue
        if not full.startswith(title):continue
        if not re.fullmatch(r"(?:\d{4}\.\d{4,5}|[a-z.\-]+/\d{7})",candidate["id"]):continue
        row=rows.get(item["id"])
        if not row or row.get("arxiv_id"):continue
        aid=candidate["id"]
        row["arxiv_id"]=aid
        row["public_url"]="https://arxiv.org/abs/"+aid
        row["pdf_url"]="https://arxiv.org/pdf/"+aid
        row["download_url"]=row["pdf_url"]
        row["download_source"]="arxiv"
        row["verification_status"]="official-url-verified"
        item["decision"]="resolved-by-unambiguous-prefix"
        item["resolution_rule"]="single arXiv API candidate; normalized full title starts with original >=52 character title prefix"
        changed.append({"id":item["id"],"arxiv_id":aid,"title":row["title"]})
    if changed:
        spec=importlib.util.spec_from_file_location("verify",ROOT/"scripts/verify_arxiv_index.py")
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        DB.write_text(json.dumps(db,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        module.export_csv(db["records"])
    print(json.dumps({"new_matches":len(changed),"records":changed},ensure_ascii=False))
if __name__=="__main__":main()

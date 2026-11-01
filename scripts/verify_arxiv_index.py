#!/usr/bin/env python3
"""Incremental, conservative arXiv title verification for public GitHub paper index.
No private Drive identifiers. Resumes using resources/arxiv-lookup-state.json.
"""
import argparse,csv,difflib,json,re,time,urllib.parse,urllib.request,xml.etree.ElementTree as ET
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DB=ROOT/"resources/paper-master-index.json"
CSV=ROOT/"resources/paper-master-index.csv"
STATE=ROOT/"resources/arxiv-lookup-state.json"
REPORT=ROOT/"resources/arxiv-match-review.json"
AGENTS={"User-Agent":"awesome-sound-detection-literature-index/1.0 (public bibliographic metadata)"}
ATOM={"a":"http://www.w3.org/2005/Atom"}
def norm(s):
    s=re.sub(r"^20\d\d[-_/]\d\d[-_/]\d\d[-\s]*","",s)
    s=re.sub(r"(?i)(?:_summary)?\.(?:md|pdf)$","",s)
    return re.sub(r"\s+"," ",re.sub(r"[^a-z0-9]+"," ",s.casefold())).strip()
def query(title):
    title=norm(title)
    if len(title)<18 or len(title.split())<4:return []
    # Search a distinctive prefix; titles are compared in full below.
    words=title.split()[:9]
    url="https://export.arxiv.org/api/query?"+urllib.parse.urlencode({"search_query":'ti:"'+" ".join(words)+'"',"start":0,"max_results":7})
    req=urllib.request.Request(url,headers=AGENTS)
    with urllib.request.urlopen(req,timeout=30) as response:
        tree=ET.fromstring(response.read())
    out=[]
    for entry in tree.findall("a:entry",ATOM):
        name=" ".join((entry.findtext("a:title",default="",namespaces=ATOM)).split())
        link=entry.findtext("a:id",default="",namespaces=ATOM)
        m=re.search(r"/(?:abs|pdf)/((?:\d{4}\.\d{4,5}|[a-z\-\.]+/\d{7})(?:v\d+)?)",link)
        if not m:continue
        ident=re.sub(r"v\d+$","",m.group(1))
        sim=difflib.SequenceMatcher(None,norm(title),norm(name)).ratio()
        out.append({"id":ident,"arxiv_title":name,"similarity":round(sim,4)})
    return sorted(out,key=lambda x:-x["similarity"])
def export_csv(rows):
    names=["id","title","primary_category","related_categories","source_sections","public_url","pdf_url","doi","arxiv_id","drive_file_url","drive_download_url","download_url","download_source","download_access","verification_status"]
    with CSV.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=names);w.writeheader()
        for v in rows:w.writerow({"id":v["id"],"title":v["title"],"primary_category":v["primary_category"],"related_categories":";".join(v.get("related_categories",[])),"source_sections":";".join(v.get("sources",[])),"public_url":v.get("public_url"),"pdf_url":v.get("pdf_url"),"doi":v.get("doi"),"arxiv_id":v.get("arxiv_id"),"drive_file_url":v.get("drive_file_url"),"drive_download_url":v.get("drive_download_url"),"download_url":v.get("download_url"),"download_source":v.get("download_source"),"download_access":v.get("download_access"),"verification_status":v.get("verification_status")})
def main():
    a=argparse.ArgumentParser();a.add_argument("--batch",type=int,default=60);a.add_argument("--delay",type=float,default=3.2);args=a.parse_args()
    data=json.loads(DB.read_text(encoding="utf-8"));rows=data["records"]
    state=json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {"checked_ids":[],"errors":{}}
    checked=set(state.get("checked_ids",[]));errors=state.setdefault("errors",{})
    report=json.loads(REPORT.read_text(encoding="utf-8")) if REPORT.exists() else {"manual_review":[]}
    review=report.setdefault("manual_review",[])
    attempts=0;matched=0
    for row in rows:
        if attempts>=args.batch:break
        rid=row["id"]
        if rid in checked:continue
        if row.get("arxiv_id") and row.get("pdf_url"):
            checked.add(rid);continue
        attempts+=1
        try:
            cand=query(row["title"]);top=cand[0] if cand else None
            # Strong full-title match only; ambiguous top two require manual review
            if top and top["similarity"]>=0.96 and (len(cand)==1 or cand[1]["similarity"]<0.94):
                ident=top["id"];row["arxiv_id"]=ident
                row["public_url"]="https://arxiv.org/abs/"+ident
                row["pdf_url"]="https://arxiv.org/pdf/"+ident
                row["verification_status"]="official-url-verified"
                row["download_url"]=row["pdf_url"]
                row["download_source"]="arxiv"
                matched+=1
            elif top and top["similarity"]>=0.80:
                review.append({"id":rid,"title":row["title"],"candidates":cand[:3],"decision":"manual-review"})
            checked.add(rid);errors.pop(rid,None)
        except Exception as exc:
            errors[rid]=str(exc)[:300]
            # No false negatives when provider is unreachable; retry next run.
        finally:
            time.sleep(max(3.0,args.delay))
    state["checked_ids"]=sorted(checked)
    state["attempted_in_last_run"]=attempts
    state["matched_in_last_run"]=matched
    state["total_records"]=len(rows)
    state["verified_pdf_count"]=sum(bool(r.get("pdf_url")) for r in rows)
    report["manual_review"]=review
    for path,obj in [(DB,data),(STATE,state),(REPORT,report)]:
        path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    export_csv(rows)
    print(json.dumps({"attempted":attempts,"matched":matched,"checked_total":len(checked),"total":len(rows),"errors":len(errors)}))
if __name__=="__main__":main()

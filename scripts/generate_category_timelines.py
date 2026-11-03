#!/usr/bin/env python3
"""Generate standalone interactive paper timelines for repository categories."""
from __future__ import annotations

import csv
import html
import json
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CATEGORIES = {
    "sound-event": ("声音事件检测", "papers/sound-event/papers-timeline.html"),
    "acoustic-anomaly": ("声学异常检测", "papers/acoustic-anomaly/papers-timeline.html"),
    "das": ("分布式声学传感（DAS）", "domains/das/papers-timeline.html"),
    "leakage": ("泄漏声学检测", "domains/leakage/papers-timeline.html"),
    "speaker-recognition": ("声纹识别", "related/speaker-recognition/papers-timeline.html"),
    "foundation-models": ("音频基础模型", "related/foundation-models/papers-timeline.html"),
    "face-recognition": ("人脸识别", "related/face-recognition/papers-timeline.html"),
    "visual-anomaly": ("图像异常检测", "related/visual-anomaly/papers-timeline.html"),
    "cross-domain": ("跨领域迁移", "cross-domain/papers-timeline.html"),
}

ALIASES = {"speaker": "speaker-recognition", "foundation": "foundation-models"}

CLUSTERS = {
    "sound-event": {
        "弱监督与少标签": ["weakly supervised", "weak supervision", "semi-supervised", "few-shot", "active learning", "pseudo-label"],
        "基础模型与自监督": ["foundation model", "self-supervised", "pretrained", "pre-trained", "audio-language", "large audio"],
        "定位与空间感知": ["localization", "spatial audio", "sound source localization", "doa", "polyphonic"],
        "鲁棒性与跨域": ["domain adaptation", "domain generalization", "noise robust", "robustness", "out-of-distribution", "open-set"],
        "生物与环境声": ["bioacoustic", "bird", "marine", "soundscape", "ecoacoustic", "wildlife"],
        "轻量化与边缘部署": ["lightweight", "edge deployment", "embedded deployment", "on-device", "tinyml", "low-power"],
    },
    "acoustic-anomaly": {
        "无监督与自监督": ["unsupervised", "self-supervised", "autoencoder", "representation learning"],
        "跨域泛化": ["domain generalization", "domain adaptation", "domain shift", "cross-domain"],
        "开放集与异常拒识": ["open-set", "out-of-distribution", "unknown", "novelty detection"],
        "工业状态监测": ["machine condition", "fault diagnosis", "predictive maintenance", "industrial"],
        "噪声与弱标签": ["noise", "noisy label", "weakly supervised", "pseudo-label"],
    },
    "das": {
        "边缘实时处理": ["edge", "real-time", "lightweight", "efficient"],
        "故障与状态识别": ["fault", "anomaly", "condition monitoring", "diagnosis"],
        "交通与基础设施": ["railway", "pipeline", "traffic", "bridge", "conveyor"],
        "信号表征": ["time-frequency", "representation", "denoising", "signal processing"],
    },
    "leakage": {
        "泄漏定位": ["localization", "locating", "time difference", "cross-correlation"],
        "检测与分类": ["detection", "classification", "recognition"],
        "管网与现场鲁棒性": ["pipeline", "water distribution", "noise", "field", "industrial"],
    },
    "speaker-recognition": {
        "说话人验证": ["speaker verification", "voice verification"],
        "说话人分离": ["speaker diarization", "diarization"],
        "自监督表征": ["self-supervised", "pretrained", "pre-trained", "wav2vec", "hubert"],
        "跨语言与域适应": ["cross-lingual", "domain adaptation", "domain generalization", "multilingual"],
        "隐私与反欺骗": ["spoof", "privacy", "deepfake", "anti-spoofing"],
    },
    "foundation-models": {
        "音频语言模型": ["audio-language", "audio language", "large audio", "audio llm", "multimodal language"],
        "自监督预训练": ["self-supervised", "pretraining", "pre-training", "masked modeling"],
        "音频文本对齐": ["audio-text", "contrastive language-audio", "clap", "text-audio"],
        "推理与代理": ["reasoning", "agent", "instruction", "chain-of-thought"],
        "高效适配": ["adapter", "lora", "parameter-efficient", "prompt tuning", "quantization"],
    },
    "face-recognition": {
        "度量与间隔损失": ["arcface", "margin", "metric learning", "cosine"],
        "噪声标签与长尾": ["noisy label", "noise", "long-tail", "sub-center"],
        "跨域与鲁棒性": ["domain adaptation", "domain generalization", "robust", "cross-domain"],
    },
    "visual-anomaly": {
        "特征记忆与检索": ["patchcore", "memory bank", "nearest neighbor", "retrieval"],
        "分布建模": ["padim", "distribution", "gaussian", "density"],
        "基础模型特征": ["foundation model", "dinov2", "clip", "pretrained"],
        "少样本与零样本": ["few-shot", "zero-shot", "one-shot"],
    },
    "cross-domain": {
        "域泛化": ["domain generalization", "domain shift", "cross-domain"],
        "迁移与适配": ["transfer learning", "domain adaptation", "adapter"],
        "多模态迁移": ["multimodal", "cross-modal", "audio-visual"],
        "开放集": ["open-set", "out-of-distribution", "unknown class"],
    },
}


def normalize_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def date_for(row: dict) -> str | None:
    for key in ("published", "updated"):
        if re.match(r"20\d\d-\d\d-\d\d", row.get(key, "")):
            return row[key][:10]
    arxiv = row.get("arxiv_id") or row.get("id", "")
    match = re.fullmatch(r"(\d{2})(\d{2})\.\d{4,5}", arxiv or "")
    if match:
        year = 2000 + int(match.group(1))
        month = min(12, max(1, int(match.group(2))))
        return f"{year:04d}-{month:02d}-01"
    match = re.search(r"(?<!\d)(20\d{2})(?:[-_/](\d{2})(?:[-_/](\d{2}))?)?", row.get("title", ""))
    if match:
        return f"{match.group(1)}-{match.group(2) or '01'}-{match.group(3) or '01'}"
    return None


def paper_from(row: dict, category: str, source: str) -> dict | None:
    date = date_for(row)
    if not date:
        return None
    ident = row.get("arxiv_id") or (row.get("id") if re.fullmatch(r"\d{4}\.\d{4,5}", row.get("id", "")) else None)
    abs_url = row.get("abs_url") or row.get("public_url") or (f"https://arxiv.org/abs/{ident}" if ident else None)
    pdf_url = row.get("pdf_url") or (f"https://arxiv.org/pdf/{ident}" if ident else row.get("download_url"))
    return {
        "id": ident or row.get("id") or normalize_title(row.get("title", ""))[:60],
        "title": row.get("title", "Untitled"),
        "date": date,
        "authors": row.get("authors", []) if isinstance(row.get("authors"), list) else [],
        "abstract": row.get("abstract", ""),
        "abs": abs_url,
        "pdf": pdf_url,
        "source": source,
        "category": category,
    }


def load_data() -> dict[str, list[dict]]:
    master = json.loads((ROOT / "resources/paper-master-index.json").read_text(encoding="utf-8"))["records"]
    cs_sd = json.loads((ROOT / "resources/arxiv-cs-sd/papers.json").read_text(encoding="utf-8"))["records"]
    catalog = json.loads((ROOT / "resources/catalog.json").read_text(encoding="utf-8"))["resources"]
    grouped = defaultdict(list)
    for row in cs_sd:
        for raw in row.get("repository_categories", []):
            category = ALIASES.get(raw, raw)
            if category in CATEGORIES:
                paper = paper_from(row, category, "arXiv cs.SD")
                if paper:
                    grouped[category].append(paper)
    for row in master:
        category = row.get("primary_category")
        if category in CATEGORIES:
            paper = paper_from(row, category, "仓库论文主索引")
            if paper:
                grouped[category].append(paper)
        title = (row.get("title") or "").casefold()
        inferred = None
        if any(k in title for k in ("face recognition", "facial recognition", "arcface")):
            inferred = "face-recognition"
        elif any(k in title for k in ("visual anomaly", "image anomaly", "industrial defect", "surface defect", "patchcore", "padim")):
            inferred = "visual-anomaly"
        if inferred:
            paper = paper_from(row, inferred, "仓库论文主索引（标题归类）")
            if paper:
                grouped[inferred].append(paper)
    for row in catalog:
        category = row.get("domain")
        if row.get("type") == "paper" and category in CATEGORIES:
            ident_match = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", row.get("url", ""))
            paper = paper_from({"id": ident_match.group(1) if ident_match else row["id"], "title": row["title"], "public_url": row.get("url"), "pdf_url": row.get("pdf_url")}, category, "资源目录")
            if paper:
                grouped[category].append(paper)
    for category, papers in grouped.items():
        dedup = {}
        for paper in papers:
            key = paper["id"] if re.fullmatch(r"\d{4}\.\d{4,5}", str(paper["id"])) else normalize_title(paper["title"])
            current = dedup.get(key)
            if not current or (paper.get("abstract") and not current.get("abstract")):
                dedup[key] = paper
        grouped[category] = sorted(dedup.values(), key=lambda p: (p["date"], p["title"]))
    return grouped


def classify_themes(papers: list[dict], category: str) -> None:
    clusters = CLUSTERS.get(category, {})
    for paper in papers:
        text = (paper["title"] + " " + paper.get("abstract", "")).casefold()
        paper["themes"] = [name for name, terms in clusters.items() if any(term in text for term in terms)] or ["其他"]


def trend_findings(papers: list[dict], category: str) -> list[dict]:
    counts = Counter(theme for paper in papers for theme in paper["themes"] if theme != "其他")
    recent = Counter(theme for paper in papers if paper["date"] >= "2026-01-01" for theme in paper["themes"] if theme != "其他")
    older = Counter(theme for paper in papers if paper["date"] < "2026-01-01" for theme in paper["themes"] if theme != "其他")
    findings = []
    if counts:
        top, count = counts.most_common(1)[0]
        examples = [p for p in reversed(papers) if top in p["themes"]][:3]
        findings.append({"title": f"{top}是当前最密集的方法主线", "text": f"在可定年论文中命中 {count} 篇，占 {count / max(1, len(papers)):.1%}；这说明该方向的工作重心持续围绕这一问题展开。", "evidence": examples})
        growth = []
        n_recent = sum(p["date"] >= "2026-01-01" for p in papers)
        n_older = len(papers) - n_recent
        for theme in counts:
            if counts[theme] >= 3:
                delta = recent[theme] / max(1, n_recent) - older[theme] / max(1, n_older)
                growth.append((delta, theme))
        if growth:
            delta, theme = max(growth)
            examples = [p for p in reversed(papers) if theme in p["themes"] and p["date"] >= "2026-01-01"][:3]
            findings.append({"title": f"{theme}在近期论文中的相对占比上升", "text": f"2026 年以来命中 {recent[theme]} 篇；相对 2025 年及以前的集合占比变化为 {delta:+.1%}。这是集合内趋势，不等同于全领域文献计量结论。", "evidence": examples})
    monthly = Counter(p["date"][:7] for p in papers)
    if monthly:
        month, count = monthly.most_common(1)[0]
        examples = [p for p in papers if p["date"].startswith(month)][:3]
        findings.append({"title": f"{month} 是当前收录的论文高峰月", "text": f"该月收录 {count} 篇。时间线中的密集节点可用于进一步核对数据集、任务或会议周期是否造成集中发布。", "evidence": examples})
    return findings[:3]


def escape_json(value) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def build_html(category: str, title: str, papers: list[dict]) -> str:
    classify_themes(papers, category)
    findings = trend_findings(papers, category)
    themes = sorted({theme for paper in papers for theme in paper["themes"]})
    years = sorted({paper["date"][:4] for paper in papers})
    min_date = papers[0]["date"] if papers else "—"
    max_date = papers[-1]["date"] if papers else "—"
    finding_html = "".join(
        f'<article class="finding"><h3>{html.escape(f["title"])}</h3><p>{html.escape(f["text"])}</p><div class="evidence">证据：' + " · ".join(f'<a href="{html.escape(p.get("abs") or p.get("pdf") or "#")}" target="_blank" rel="noopener">{html.escape(p["title"][:62])}</a>' for p in f["evidence"]) + "</div></article>"
        for f in findings
    )
    options_year = '<option value="">全部年份</option>' + "".join(f'<option value="{y}">{y}</option>' for y in years)
    options_theme = '<option value="">全部主题</option>' + "".join(f'<option value="{html.escape(t)}">{html.escape(t)}</option>' for t in themes)
    data = escape_json(papers)
    template = '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__论文时间线</title>
<style>
:root{--bg:#f6f8fb;--panel:#fff;--text:#172033;--muted:#647085;--line:#d8deea;--accent:#1667d9;--accent2:#14a38b;--soft:#eaf2ff;--shadow:0 12px 30px rgba(23,32,51,.08)}
@media(prefers-color-scheme:dark){:root{--bg:#10141d;--panel:#171d28;--text:#edf2ff;--muted:#a9b3c7;--line:#303a4c;--accent:#6aa6ff;--accent2:#5fd1bc;--soft:#1b2c48;--shadow:none}}
*{box-sizing:border-box} body{margin:0;background:var(--bg);color:var(--text);font:15px/1.6 system-ui,-apple-system,"Segoe UI",sans-serif} a{color:var(--accent)} .wrap{max-width:1380px;margin:auto;padding:28px 24px 60px} header{display:grid;gap:18px} h1{font-size:clamp(28px,4vw,48px);line-height:1.1;margin:0} .subtitle{color:var(--muted);max-width:900px} .stats{display:flex;gap:12px;flex-wrap:wrap} .stat{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:12px 16px;box-shadow:var(--shadow)} .stat b{font-size:22px;display:block} .findings{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px} .finding{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:18px;box-shadow:var(--shadow)} .finding h3{margin:0 0 8px;font-size:17px} .finding p{margin:0 0 10px} .evidence{font-size:12px;color:var(--muted)} .evidence a{display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis} main{margin-top:22px;background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:18px;box-shadow:var(--shadow)} .controls{display:flex;gap:10px;flex-wrap:wrap;align-items:center} input,select,button{font:inherit;color:var(--text);background:var(--panel);border:1px solid var(--line);border-radius:9px;padding:9px 11px} input{min-width:260px;flex:1} button{cursor:pointer;background:var(--soft)} .count{margin-left:auto;color:var(--muted)} .chart{position:relative;margin-top:16px} svg{display:block;width:100%;height:auto;min-height:360px} .axis,.curve{fill:none;stroke:var(--line)} .curve{stroke:var(--accent);stroke-width:2.2;opacity:.65} .axis-text,.node-label{fill:var(--muted);font-size:11px} .point{fill:var(--accent2);stroke:var(--panel);stroke-width:1.5;cursor:pointer} .point:hover,.point.active{fill:var(--accent);stroke-width:3} .tooltip{position:absolute;display:none;max-width:340px;background:var(--text);color:var(--bg);border-radius:9px;padding:9px 11px;font-size:12px;pointer-events:none;z-index:4} .detail{display:grid;grid-template-columns:1fr auto;gap:12px;margin-top:8px;padding:14px;border-top:1px solid var(--line)} .detail h2{font-size:18px;margin:0 0 4px} .detail p{margin:0;color:var(--muted)} .actions{display:flex;gap:8px;align-items:start} .actions a{text-decoration:none;border:1px solid var(--line);border-radius:8px;padding:7px 10px;white-space:nowrap} .empty{padding:80px 20px;text-align:center;color:var(--muted)}
@media(max-width:850px){.findings{grid-template-columns:1fr}.count{width:100%;margin:0}.detail{grid-template-columns:1fr}.wrap{padding:20px 12px 40px}}
</style></head><body><div class="wrap">
<header><div><h1>__TITLE__论文时间线</h1><p class="subtitle">基于仓库当前论文索引生成。曲线按发表时间排列；节点可悬停查看、点击展开摘要并打开官方页面或下载 PDF。趋势结论只依赖本页收录论文及其标题、摘要和时间，不外推为完整学科计量。</p></div>
<div class="stats"><div class="stat"><b>__COUNT__</b>可定年论文</div><div class="stat"><b>__MIN_DATE__</b>最早记录</div><div class="stat"><b>__MAX_DATE__</b>最新记录</div><div class="stat"><b>__PDF_COUNT__</b>可下载记录</div></div>
<section class="findings" aria-label="技术趋势总结">__FINDINGS__</section></header>
<main><div class="controls"><input id="search" type="search" placeholder="搜索标题、摘要或作者" aria-label="搜索论文"><select id="year" aria-label="筛选年份">__YEAR_OPTIONS__</select><select id="theme" aria-label="筛选主题">__THEME_OPTIONS__</select><button id="export" type="button">导出当前 CSV</button><span id="count" class="count"></span></div>
<div class="chart"><svg id="timeline" viewBox="0 0 1200 420" role="img" aria-label="可交互论文时间线"></svg><div id="tooltip" class="tooltip"></div></div>
<section id="detail" class="detail" aria-live="polite"><div><h2>选择曲线上的论文节点</h2><p>悬停可快速查看，点击节点显示摘要与下载入口。</p></div></section></main></div>
<script>
const papers=__PAPER_DATA__; const svg=document.getElementById('timeline'), tip=document.getElementById('tooltip'), detail=document.getElementById('detail'), search=document.getElementById('search'), year=document.getElementById('year'), theme=document.getElementById('theme'), count=document.getElementById('count');
const NS='http://www.w3.org/2000/svg'; const E=(name,attrs={})=>{const e=document.createElementNS(NS,name);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,v));return e};
function filtered(){const q=search.value.trim().toLowerCase();return papers.filter(p=>(!year.value||p.date.startsWith(year.value))&&(!theme.value||p.themes.includes(theme.value))&&(!q||[p.title,p.abstract,(p.authors||[]).join(' ')].join(' ').toLowerCase().includes(q)))}
function render(){const rows=filtered(); count.textContent=`显示 ${rows.length} / ${papers.length} 篇`; svg.replaceChildren(); if(!rows.length){const t=E('text',{x:600,y:210,'text-anchor':'middle',class:'axis-text'});t.textContent='没有匹配论文';svg.append(t);return} const W=1200,H=420,L=58,R=30,T=40,B=58; const ts=rows.map(p=>Date.parse(p.date)), lo=Math.min(...ts),hi=Math.max(...ts),span=Math.max(86400000,hi-lo); const x=t=>L+(t-lo)/span*(W-L-R); const y=t=>210+70*Math.sin(((t-lo)/span)*Math.PI*4); let path=''; for(let i=0;i<220;i++){const t=lo+span*i/219;path+=(i?' L':'M')+x(t).toFixed(1)+' '+y(t).toFixed(1)} svg.append(E('path',{d:path,class:'curve'})); svg.append(E('line',{x1:L,y1:H-B,x2:W-R,y2:H-B,class:'axis'})); const startY=new Date(lo).getUTCFullYear(),endY=new Date(hi).getUTCFullYear(); for(let yr=startY;yr<=endY;yr++){const t=Date.parse(yr+'-01-01');if(t<lo||t>hi)continue;const xx=x(t);svg.append(E('line',{x1:xx,y1:H-B,x2:xx,y2:H-B+7,class:'axis'}));const tx=E('text',{x:xx,y:H-B+24,'text-anchor':'middle',class:'axis-text'});tx.textContent=yr;svg.append(tx)} const occupied={}, labelIds=new Set(); const labelCount=rows.length<=40?rows.length:8; for(let n=0;n<labelCount;n++){const target=lo+span*(n+.35)/labelCount;let best=0,dist=Infinity;ts.forEach((t,i)=>{const d=Math.abs(t-target);if(d<dist){dist=d;best=i}});labelIds.add(best)} rows.forEach((p,i)=>{const t=Date.parse(p.date),xx=x(t),bucket=Math.round(xx/7),stack=occupied[bucket]||0;occupied[bucket]=stack+1;const yy=y(t)+(stack%2?1:-1)*Math.ceil(stack/2)*5;const c=E('circle',{cx:xx,cy:yy,r:4,class:'point','aria-label':p.date+' '+p.title});c.addEventListener('mouseenter',ev=>showTip(ev,p));c.addEventListener('mousemove',moveTip);c.addEventListener('mouseleave',()=>tip.style.display='none');c.addEventListener('click',()=>selectPaper(p,c));svg.append(c);if(labelIds.has(i)){const tx=E('text',{x:Math.min(W-R-180,xx+6),y:yy+(i%2?-10:17),class:'node-label'});tx.textContent=p.date.slice(0,7)+' · '+p.title.slice(0,22);svg.append(tx)}})}
function showTip(ev,p){tip.innerHTML='<b>'+escapeHtml(p.date+' · '+p.title)+'</b><br>'+escapeHtml((p.authors||[]).slice(0,3).join(', '));tip.style.display='block';moveTip(ev)} function moveTip(ev){const box=svg.parentElement.getBoundingClientRect();tip.style.left=Math.min(box.width-350,Math.max(0,ev.clientX-box.left+12))+'px';tip.style.top=Math.max(0,ev.clientY-box.top-70)+'px'}
function selectPaper(p,node){svg.querySelectorAll('.active').forEach(n=>n.classList.remove('active'));node.classList.add('active');const links=[];if(p.abs)links.push('<a href="'+attr(p.abs)+'" target="_blank" rel="noopener">论文页</a>');if(p.pdf)links.push('<a href="'+attr(p.pdf)+'" target="_blank" rel="noopener" download>下载 PDF</a>');detail.innerHTML='<div><h2>'+escapeHtml(p.title)+'</h2><p>'+escapeHtml(p.date+' · '+(p.authors||[]).join(', '))+'</p><p>'+escapeHtml((p.abstract||'暂无摘要').slice(0,900))+'</p></div><div class="actions">'+links.join('')+'</div>'}
function escapeHtml(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))} function attr(s){return escapeHtml(s)}
[search,year,theme].forEach(el=>el.addEventListener(el===search?'input':'change',render));document.getElementById('export').addEventListener('click',()=>{const rows=filtered(),cols=['date','id','title','authors','themes','abs','pdf'];const csv=[cols.join(',')].concat(rows.map(p=>cols.map(k=>'"'+String(Array.isArray(p[k])?p[k].join('; '):(p[k]||'')).replace(/"/g,'""')+'"').join(','))).join('\\n');const a=document.createElement('a');a.href=URL.createObjectURL(new Blob(['\ufeff'+csv],{type:'text/csv'}));a.download='__CATEGORY__-papers.csv';a.click();URL.revokeObjectURL(a.href)});render();
</script></body></html>'''
    replacements = {
        "__TITLE__": html.escape(title), "__COUNT__": str(len(papers)),
        "__MIN_DATE__": min_date, "__MAX_DATE__": max_date,
        "__PDF_COUNT__": str(sum(bool(p.get("pdf")) for p in papers)),
        "__FINDINGS__": finding_html, "__YEAR_OPTIONS__": options_year,
        "__THEME_OPTIONS__": options_theme, "__PAPER_DATA__": data,
        "__CATEGORY__": category,
    }
    for key, value in replacements.items():
        template = template.replace(key, value)
    return template


def main() -> None:
    grouped = load_data()
    manifest = {"generated_at": datetime.utcnow().isoformat() + "Z", "categories": {}}
    for category, (title, relative) in CATEGORIES.items():
        papers = grouped.get(category, [])
        target = ROOT / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(build_html(category, title, papers), encoding="utf-8")
        manifest["categories"][category] = {"title": title, "path": relative, "paper_count": len(papers), "pdf_count": sum(bool(p.get("pdf")) for p in papers)}
        print(f"{category}: {len(papers)} -> {relative}")
    (ROOT / "resources/category-timeline-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

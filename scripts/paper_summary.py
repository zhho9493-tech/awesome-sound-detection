#!/usr/bin/env python3
"""Conservative abstract-grounded summaries for public research indexing.

No generative model, no invented scores. Every non-empty field is an extract
of a sentence in the supplied public abstract. Title-only entries stay pending.
"""
import re

METHOD = re.compile(r"\b(propos(?:e|es|ed)|present(?:s|ed)?|introduc(?:e|es|ed)|develop(?:s|ed)?|design(?:s|ed)?|framework|approach|method|model|architectur\w*|algorithm|train(?:ing)?|learn(?:ing)?|based on|we use|we employ)\b", re.I)
RESULT = re.compile(r"\b(experiment\w*|result\w*|evaluat\w*|demonstrat\w*|outperform\w*|improv\w*|achiev\w*|benchmark\w*|test\w*|perform\w*|comparison|accuracy|precision|recall|f1|auc|pauc)\b", re.I)
OBJECTIVE = re.compile(r"\b(challeng\w*|aim\w*|goal|problem|task|detect\w*|recogniz\w*|classif\w*|monitor\w*|localiz\w*|predict\w*|address\w*|investigat\w*)\b", re.I)

def sentences(text):
    """Split text without fabricating additional content."""
    clean=" ".join(str(text or "").split())
    if not clean:
        return []
    parts=re.split(r"(?<=[.!?。！？])\s+(?=[A-Z0-9“(])|(?<=[。！？])(?=\S)",clean)
    return [p.strip() for p in parts if p.strip()]

def extract_summary(abstract, title=""):
    ss=sentences(abstract)
    blank={"status":"needs-abstract","basis":"none","objective":"","method":"","finding":"","caveat":"原索引未提供可验证的摘要，尚无法从原文总结；请打开论文来源核实。"}
    if not ss:
        return blank
    def pick(pattern, used=None):
        for i,s in enumerate(ss):
            if i not in (used or set()) and pattern.search(s):
                return i
        return None
    oi=pick(OBJECTIVE)
    if oi is None:oi=0
    mi=pick(METHOD,{oi})
    if mi is None and METHOD.search(ss[oi]): mi=oi
    fi=pick(RESULT,{oi,mi} if mi is not None else {oi})
    if fi is None:
        for i in [mi,oi]:
            if i is not None and RESULT.search(ss[i]):
                fi=i
                break
    clip=lambda i:ss[i][:500] if i is not None else ""
    return {
        "status":"abstract-extract",
        "basis":"public-abstract",
        "objective":clip(oi),
        "method":clip(mi),
        "finding":clip(fi),
        "caveat":"自动摘取摘要原句，属于作者自述而非独立复核。无原句时留空；不代表已完成论文全文解读或实验复现。"
    }

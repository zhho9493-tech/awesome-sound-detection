#!/usr/bin/env python3
"""Check that every research topic has an auditable paper selection rule."""
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parents[1]
taxonomy=json.loads((ROOT/"resources/research-taxonomy.json").read_text(encoding="utf-8"))["dimensions"]
rules=json.loads((ROOT/"resources/topic-paper-rules.json").read_text(encoding="utf-8"))["topics"]
expected={r["id"] for group in ("applications","problems","methods") for r in taxonomy[group]}
assert set(rules)==expected, f"rule coverage mismatch; missing={expected-set(rules)}, extra={set(rules)-expected}"
for slug,rule in rules.items():
    assert rule["match"] in {"exact-category","keyword-candidate"},slug
    assert isinstance(rule["categories"],list) and isinstance(rule["terms"],list),slug
    if rule["match"]=="exact-category":
        assert rule["categories"] and not rule["terms"],slug
    else:
        assert rule["terms"] and not rule["categories"],slug
        assert all(isinstance(term,str) and (len(term)>=3 or (len(term)>=2 and any('\u4e00'<=ch<='\u9fff' for ch in term))) for term in rule["terms"]),slug
portal=(ROOT/"portal/topic.html").read_text(encoding="utf-8")
assert "data-topic" in portal and "来源" in portal and "作者" in portal and "继续加载更多论文" in portal
wf=(ROOT/".github/workflows/publish-research-portal.yml").read_text(encoding="utf-8")
assert "portal/topic.html" in wf and "resources/topic-paper-rules.json" in wf
print(f"Validated {len(expected)} per-topic selection rules and publishing references")

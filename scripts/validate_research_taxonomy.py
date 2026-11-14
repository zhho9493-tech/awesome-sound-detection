#!/usr/bin/env python3
"""Validate the additive research taxonomy and its referenced repository paths."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TAXONOMY = ROOT / "resources" / "research-taxonomy.json"
DIMENSIONS = ("applications", "problems", "methods", "assets")

def main() -> int:
    obj = json.loads(TAXONOMY.read_text(encoding="utf-8"))
    assert obj.get("schema_version"), "schema_version required"
    dims = obj["dimensions"]
    assert set(dims) == set(DIMENSIONS), "expected four dimensions"
    seen = set()
    for group, items in dims.items():
        assert isinstance(items, list) and items, f"{group}: empty"
        for item in items:
            for key in ("id", "name", "path"):
                assert isinstance(item.get(key), str) and item[key].strip(), f"{group}: missing {key}"
            ident = (group, item["id"])
            assert ident not in seen, f"duplicate id {ident}"
            seen.add(ident)
            target = (ROOT / item["path"]).resolve()
            assert target.is_relative_to(ROOT.resolve()), f"unsafe path: {item['path']}"
            assert target.is_file(), f"missing linked file: {item['path']}"
            for tag in item.get("tags", []):
                assert isinstance(tag, str) and tag.strip(), f"invalid tag {ident}"
    assert (ROOT / "portal" / "index.html").is_file(), "missing interactive portal"
    print(f"Validated {sum(map(len, dims.values()))} navigation entries across {len(dims)} dimensions")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyError, AssertionError, ValueError) as exc:
        print(f"Taxonomy validation failed: {exc}", file=sys.stderr)
        sys.exit(1)

#!/usr/bin/env python3
import json
from pathlib import Path
from urllib.parse import urlparse

path = Path(__file__).resolve().parents[1] / "resources" / "catalog.json"
obj = json.loads(path.read_text(encoding="utf-8"))
assert obj.get("schema_version"), "Missing schema version"
seen = set()
for item in obj["resources"]:
    for field in ("id", "domain", "type", "title", "url", "status"):
        assert item.get(field), f"Missing {field}: {item}"
    assert item["id"] not in seen, f"Duplicate: {item['id']}"
    seen.add(item["id"])
    assert urlparse(item["url"]).scheme == "https", item["url"]
print(f"Validated {len(seen)} resources")

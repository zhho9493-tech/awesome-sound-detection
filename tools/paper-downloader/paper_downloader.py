#!/usr/bin/env python3
"""Discover and download every explicitly downloadable paper in this repository."""
from __future__ import annotations

import argparse
import concurrent.futures
import csv
import hashlib
import json
import os
import re
import shutil
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path

TEXT_SUFFIXES = {".md", ".html", ".htm", ".csv", ".tsv"}
JSON_URL_KEYS = {"pdf", "pdf_url", "download_url", "drive_download_url"}
SKIP_DIRS = {".git", ".venv", "node_modules", "__pycache__"}
URL_RE = re.compile(r"https?://[^\s<>\"'\])}]+", re.I)
ARXIV_RE = re.compile(r"arxiv\.org/(?:pdf|abs)/(\d{4}\.\d{4,5})(?:v\d+)?(?:\.pdf)?", re.I)
INVALID_FILENAME_RE = re.compile(r"[^0-9A-Za-z._-]+")


@dataclass
class Paper:
    key: str
    url: str
    title: str = ""
    source: str = ""
    arxiv_id: str = ""
    filename: str = ""


@dataclass
class Result:
    key: str
    url: str
    filename: str
    status: str
    bytes: int = 0
    error: str = ""
    source: str = ""


def clean_url(value: str) -> str:
    value = value.strip().rstrip(".,;:")
    value = value.replace("&amp;", "&")
    match = ARXIV_RE.search(value)
    if match:
        return f"https://arxiv.org/pdf/{match.group(1)}"
    parsed = urllib.parse.urlsplit(value)
    return urllib.parse.urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), parsed.path, parsed.query, ""))


def is_download_url(url: str, key: str = "") -> bool:
    lowered = url.casefold()
    return bool(
        key in JSON_URL_KEYS
        or "/pdf/" in lowered
        or lowered.endswith(".pdf")
        or "export=download" in lowered
        or "download=" in lowered
    )


def paper_from_url(url: str, source: Path, title: str = "") -> Paper | None:
    url = clean_url(url)
    if not is_download_url(url):
        return None
    match = ARXIV_RE.search(url)
    arxiv_id = match.group(1) if match else ""
    key = f"arxiv:{arxiv_id}" if arxiv_id else "url:" + hashlib.sha256(url.encode()).hexdigest()[:20]
    if arxiv_id:
        stem = arxiv_id
    else:
        label = INVALID_FILENAME_RE.sub("-", title).strip("-._")[:80] or "paper"
        stem = f"{label}--{key.split(':', 1)[1][:12]}"
    return Paper(key=key, url=url, title=title, source=str(source), arxiv_id=arxiv_id, filename=stem + ".pdf")


def walk_json(value, source: Path, inherited_title: str = ""):
    if isinstance(value, dict):
        title = str(value.get("title") or inherited_title or "")
        for key, item in value.items():
            if key in JSON_URL_KEYS and isinstance(item, str) and item.startswith(("http://", "https://")):
                paper = paper_from_url(item, source, title)
                if paper:
                    yield paper
            elif isinstance(item, (dict, list)):
                yield from walk_json(item, source, title)
    elif isinstance(value, list):
        for item in value:
            yield from walk_json(item, source, inherited_title)


def discover_file(path: Path):
    try:
        if path.suffix.casefold() == ".json":
            yield from walk_json(json.loads(path.read_text(encoding="utf-8")), path)
            return
        if path.suffix.casefold() not in TEXT_SUFFIXES:
            return
        text = path.read_text(encoding="utf-8", errors="ignore")
        for line in text.splitlines():
            title = re.sub(r"<[^>]+>|\[PDF\]|\bPDF\b", " ", line, flags=re.I)
            title = " ".join(title.split())[:160]
            for url in URL_RE.findall(line):
                paper = paper_from_url(url, path, title)
                if paper:
                    yield paper
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"warning: cannot scan {path}: {exc}", file=sys.stderr)


def discover(root: Path, sources: list[Path] | None = None, output: Path | None = None) -> list[Paper]:
    paths = sources or [root]
    found: dict[str, Paper] = {}
    output_resolved = output.resolve() if output else None
    for start in paths:
        iterator = [start] if start.is_file() else start.rglob("*")
        for path in iterator:
            if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
                continue
            if output_resolved and output_resolved in path.resolve().parents:
                continue
            for paper in discover_file(path):
                current = found.get(paper.key)
                if current is None or (paper.title and not current.title):
                    found[paper.key] = paper
    return sorted(found.values(), key=lambda paper: (paper.arxiv_id or "z", paper.url))


def is_pdf(path: Path) -> bool:
    try:
        with path.open("rb") as handle:
            return handle.read(5) == b"%PDF-"
    except OSError:
        return False


def tls_context(ca_bundle: Path | None = None) -> ssl.SSLContext:
    if ca_bundle:
        return ssl.create_default_context(cafile=str(ca_bundle))
    try:
        import certifi  # optional; fixes standalone Python installations without system CA linkage
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


def download_with_curl(url: str, partial: Path, timeout: float, retries: int, ca_bundle: Path | None) -> str:
    curl = shutil.which("curl")
    if not curl:
        return "curl is not installed"
    command = [curl, "-L", "--fail", "--silent", "--show-error", "--continue-at", "-", "--max-time", str(int(timeout)), "--retry", str(retries), "--output", str(partial)]
    if ca_bundle:
        command.extend(["--cacert", str(ca_bundle)])
    command.append(url)
    completed = subprocess.run(command, capture_output=True, text=True)
    if completed.returncode:
        return completed.stderr.strip() or f"curl exited with status {completed.returncode}"
    return "" if is_pdf(partial) else "curl response is not a PDF file"


def download_one(paper: Paper, output: Path, timeout: float, retries: int, overwrite: bool, ca_bundle: Path | None = None) -> Result:
    target = output / paper.filename
    partial = target.with_suffix(target.suffix + ".part")
    if target.exists() and not overwrite and is_pdf(target):
        return Result(paper.key, paper.url, paper.filename, "skipped", target.stat().st_size, source=paper.source)
    last_error = ""
    for attempt in range(retries + 1):
        try:
            offset = partial.stat().st_size if partial.exists() else 0
            headers = {"User-Agent": "awesome-sound-detection-paper-downloader/1.0"}
            if offset:
                headers["Range"] = f"bytes={offset}-"
            request = urllib.request.Request(paper.url, headers=headers)
            with urllib.request.urlopen(request, timeout=timeout, context=tls_context(ca_bundle)) as response:
                append = offset > 0 and getattr(response, "status", 200) == 206
                if offset and not append:
                    offset = 0
                with partial.open("ab" if append else "wb") as handle:
                    while chunk := response.read(1024 * 1024):
                        handle.write(chunk)
            if not is_pdf(partial):
                raise ValueError("response is not a PDF file")
            os.replace(partial, target)
            return Result(paper.key, paper.url, paper.filename, "downloaded", target.stat().st_size, source=paper.source)
        except (OSError, ValueError, urllib.error.URLError) as exc:
            last_error = str(exc)
            if attempt < retries:
                time.sleep(min(2 ** attempt, 8))
    if "CERTIFICATE_VERIFY_FAILED" in last_error:
        curl_error = download_with_curl(paper.url, partial, timeout, retries, ca_bundle)
        if not curl_error:
            os.replace(partial, target)
            return Result(paper.key, paper.url, paper.filename, "downloaded", target.stat().st_size, source=paper.source)
        last_error = f"{last_error}; curl fallback: {curl_error}"
    return Result(paper.key, paper.url, paper.filename, "failed", error=last_error, source=paper.source)


def write_reports(output: Path, papers: list[Paper], results: list[Result]) -> None:
    payload = {
        "summary": {
            "discovered": len(papers),
            "downloaded": sum(item.status == "downloaded" for item in results),
            "skipped": sum(item.status == "skipped" for item in results),
            "failed": sum(item.status == "failed" for item in results),
        },
        "results": [asdict(item) for item in results],
    }
    (output / "download-report.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (output / "download-report.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(Result("", "", "", "")).keys()))
        writer.writeheader()
        writer.writerows(asdict(item) for item in results)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[2], help="repository root")
    parser.add_argument("--source", action="append", type=Path, help="file or directory to scan; repeatable")
    parser.add_argument("--output", type=Path, help="download directory (default: <repo>/downloads/papers)")
    parser.add_argument("--workers", type=int, default=4, help="parallel downloads (default: 4)")
    parser.add_argument("--timeout", type=float, default=60, help="per-request timeout in seconds")
    parser.add_argument("--retries", type=int, default=2, help="retries after the first attempt")
    parser.add_argument("--ca-bundle", type=Path, help="custom PEM CA bundle for HTTPS verification")
    parser.add_argument("--limit", type=int, help="download at most N papers (useful for validation)")
    parser.add_argument("--list-only", action="store_true", help="discover links without downloading")
    parser.add_argument("--overwrite", action="store_true", help="replace already valid PDF files")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    repo = args.repo.resolve()
    output = (args.output or repo / "downloads/papers").resolve()
    sources = [(path if path.is_absolute() else repo / path).resolve() for path in (args.source or [])]
    papers = discover(repo, sources or None, output)
    if args.limit is not None:
        papers = papers[: max(0, args.limit)]
    print(f"discovered {len(papers)} unique downloadable papers")
    if args.list_only:
        for paper in papers:
            print(f"{paper.filename}\t{paper.url}\t{paper.source}")
        return 0
    output.mkdir(parents=True, exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = [pool.submit(download_one, paper, output, args.timeout, args.retries, args.overwrite, args.ca_bundle) for paper in papers]
        results = []
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)
            print(f"[{result.status}] {result.filename}" + (f": {result.error}" if result.error else ""))
    results.sort(key=lambda item: item.filename)
    write_reports(output, papers, results)
    failed = sum(item.status == "failed" for item in results)
    print(f"report: {output / 'download-report.json'}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

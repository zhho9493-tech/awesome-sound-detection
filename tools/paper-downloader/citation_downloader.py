#!/usr/bin/env python3
"""Resolve citation-only CSV rows to legal public PDFs, download them, and report gaps."""
from __future__ import annotations

import argparse
import concurrent.futures
import csv
import difflib
import hashlib
import json
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field
from pathlib import Path

from paper_downloader import Paper, Result, clean_url, download_one

USER_AGENT = "awesome-sound-detection-citation-downloader/1.0 (mailto:{email})"
ARXIV_ID_RE = re.compile(r"(?:arxiv[:\s/]|arxiv\.org/(?:abs|pdf)/)(\d{4}\.\d{4,5})(?:v\d+)?", re.I)
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
WORD_RE = re.compile(r"[0-9a-z\u4e00-\u9fff]+", re.I)


@dataclass
class Citation:
    row_number: int
    title: str
    authors: str = ""
    publication: str = ""
    year: str = ""
    volume: str = ""
    number: str = ""
    pages: str = ""
    publisher: str = ""


@dataclass
class Resolution:
    citation: Citation
    status: str = "unresolved"
    provider: str = ""
    matched_title: str = ""
    match_score: float = 0.0
    doi: str = ""
    arxiv_id: str = ""
    landing_url: str = ""
    pdf_urls: list[str] = field(default_factory=list)
    error: str = ""


def text(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def normalized_title(value: str) -> str:
    return " ".join(WORD_RE.findall(text(value).casefold()))


def title_score(left: str, right: str) -> float:
    a, b = normalized_title(left), normalized_title(right)
    if not a or not b:
        return 0.0
    sequence = difflib.SequenceMatcher(None, a, b).ratio()
    aa, bb = set(a.split()), set(b.split())
    jaccard = len(aa & bb) / max(1, len(aa | bb))
    return round(0.65 * sequence + 0.35 * jaccard, 4)


def load_citations(path: Path) -> list[Citation]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        aliases = {name.casefold(): name for name in (reader.fieldnames or [])}
        required = {"title", "authors", "publication", "year"}
        missing = required - set(aliases)
        if missing:
            raise ValueError(f"CSV missing fields: {', '.join(sorted(missing))}")
        rows = []
        seen = set()
        for row_number, row in enumerate(reader, 2):
            title = text(row.get(aliases["title"]))
            key = normalized_title(title)
            if not key or key in seen:
                continue
            seen.add(key)
            get = lambda name: text(row.get(aliases.get(name, "")))
            rows.append(Citation(row_number, title, get("authors"), get("publication"), get("year"), get("volume"), get("number"), get("pages"), get("publisher")))
    return rows


class Resolver:
    def __init__(self, email: str, cache_path: Path, timeout: float = 30, polite_delay: float = 0.12):
        self.email = email
        self.cache_path = cache_path
        self.timeout = timeout
        self.polite_delay = polite_delay
        try:
            self.cache = json.loads(cache_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            self.cache = {}
        try:
            import certifi
            self.context = ssl.create_default_context(cafile=certifi.where())
        except ImportError:
            self.context = ssl.create_default_context()

    def save(self) -> None:
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        self.cache_path.write_text(json.dumps(self.cache, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def get_json(self, url: str) -> dict:
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT.format(email=self.email), "Accept": "application/json"})
        with urllib.request.urlopen(request, timeout=self.timeout, context=self.context) as response:
            return json.load(response)

    def direct_arxiv(self, citation: Citation) -> Resolution | None:
        match = ARXIV_ID_RE.search(" ".join([citation.publication, citation.title]))
        if not match:
            return None
        aid = match.group(1)
        return Resolution(citation, "resolved", "citation-arxiv", citation.title, 1.0, arxiv_id=aid, landing_url=f"https://arxiv.org/abs/{aid}", pdf_urls=[f"https://arxiv.org/pdf/{aid}"])

    def openalex(self, citation: Citation) -> Resolution | None:
        params = {"search": citation.title, "per-page": 5, "mailto": self.email}
        data = self.get_json("https://api.openalex.org/works?" + urllib.parse.urlencode(params))
        best = None
        for item in data.get("results", []):
            score = title_score(citation.title, item.get("display_name", ""))
            year = str(item.get("publication_year") or "")
            if citation.year and year and citation.year != year:
                score -= 0.05
            if best is None or score > best[0]:
                best = (score, item)
        if not best or best[0] < 0.78:
            return None
        score, item = best
        oa = item.get("best_oa_location") or {}
        primary = item.get("primary_location") or {}
        pdfs = [text(oa.get("pdf_url"))]
        if (item.get("open_access") or {}).get("is_oa"):
            pdfs.append(text(primary.get("pdf_url")))
        doi = text(item.get("doi")).removeprefix("https://doi.org/")
        landing = text(oa.get("landing_page_url") or primary.get("landing_page_url") or (f"https://doi.org/{doi}" if doi else ""))
        pdfs = list(dict.fromkeys(clean_url(x) for x in pdfs if x.startswith("http")))
        return Resolution(citation, "resolved" if pdfs else "metadata-only", "openalex", text(item.get("display_name")), score, doi=doi, landing_url=landing, pdf_urls=pdfs)

    def crossref(self, citation: Citation) -> Resolution | None:
        params = {"query.title": citation.title, "rows": 5, "mailto": self.email, "select": "DOI,title,published,URL,link"}
        data = self.get_json("https://api.crossref.org/works?" + urllib.parse.urlencode(params))
        best = None
        for item in data.get("message", {}).get("items", []):
            candidate = " ".join(item.get("title") or [])
            score = title_score(citation.title, candidate)
            if best is None or score > best[0]:
                best = (score, item, candidate)
        if not best or best[0] < 0.82:
            return None
        score, item, candidate = best
        doi = text(item.get("DOI"))
        pdfs = []
        for link in item.get("link") or []:
            url, content_type = text(link.get("URL")), text(link.get("content-type")).casefold()
            if url.startswith("http") and ("pdf" in content_type or url.casefold().endswith(".pdf")):
                pdfs.append(clean_url(url))
        return Resolution(citation, "resolved" if pdfs else "metadata-only", "crossref", candidate, score, doi=doi, landing_url=text(item.get("URL") or (f"https://doi.org/{doi}" if doi else "")), pdf_urls=list(dict.fromkeys(pdfs)))

    def unpaywall(self, resolution: Resolution) -> Resolution:
        if not resolution.doi or not self.email or self.email.endswith("@example.com"):
            return resolution
        try:
            data = self.get_json(f"https://api.unpaywall.org/v2/{urllib.parse.quote(resolution.doi)}?email={urllib.parse.quote(self.email)}")
            best = data.get("best_oa_location") or {}
            urls = [text(best.get("url_for_pdf"))]
            resolution.pdf_urls = list(dict.fromkeys(resolution.pdf_urls + [clean_url(x) for x in urls if x.startswith("http")]))
            resolution.landing_url = resolution.landing_url or text(best.get("url_for_landing_page"))
            if resolution.pdf_urls:
                resolution.status = "resolved"
                resolution.provider += "+unpaywall"
        except Exception as exc:  # metadata lookup failure must not discard other providers
            resolution.error = f"Unpaywall: {exc}"
        return resolution

    def resolve(self, citation: Citation) -> Resolution:
        key = hashlib.sha256(normalized_title(citation.title).encode()).hexdigest()[:24]
        cached = self.cache.get(key)
        if cached:
            data = dict(cached)
            data["citation"] = citation
            return Resolution(**data)
        direct = self.direct_arxiv(citation)
        if direct:
            result = direct
        else:
            candidates = []
            errors = []
            for provider in (self.openalex, self.crossref):
                try:
                    found = provider(citation)
                    if found:
                        candidates.append(found)
                except Exception as exc:
                    errors.append(f"{provider.__name__}: {exc}")
                time.sleep(self.polite_delay)
            candidates.sort(key=lambda x: (bool(x.pdf_urls), x.match_score), reverse=True)
            result = candidates[0] if candidates else Resolution(citation, error="; ".join(errors) or "No reliable title match")
            if candidates and not result.pdf_urls:
                for candidate in candidates[1:]:
                    if candidate.pdf_urls:
                        result = candidate
                        break
            result = self.unpaywall(result)
            if errors and not result.error:
                result.error = "; ".join(errors)
        serial = asdict(result)
        serial.pop("citation")
        transient_error = result.status == "unresolved" and any(term in result.error for term in ("CERTIFICATE_VERIFY_FAILED", "timed out", "HTTP Error 429", "HTTP Error 5"))
        if not transient_error:
            self.cache[key] = serial
        return result


def safe_filename(citation: Citation, resolution: Resolution) -> str:
    prefix = citation.year or "unknown-year"
    label = re.sub(r"[\\/:*?\"<>|\x00-\x1f]+", "-", citation.title).strip(" .-")[:150]
    identity = resolution.arxiv_id or resolution.doi or hashlib.sha256(normalized_title(citation.title).encode()).hexdigest()[:10]
    suffix = re.sub(r"[^0-9A-Za-z._-]+", "-", identity)[:40]
    return f"{prefix}-{label}--{suffix}.pdf"


def paper_for(resolution: Resolution, url: str) -> Paper:
    citation = resolution.citation
    key = "arxiv:" + resolution.arxiv_id if resolution.arxiv_id else ("doi:" + resolution.doi.casefold() if resolution.doi else "title:" + hashlib.sha256(normalized_title(citation.title).encode()).hexdigest()[:20])
    return Paper(key, url, citation.title, source=f"citation row {citation.row_number}", arxiv_id=resolution.arxiv_id, filename=safe_filename(citation, resolution))


def flatten(resolution: Resolution, result: Result | None, attempted: list[str], failure: str = "") -> dict:
    c = resolution.citation
    return {
        "row_number": c.row_number, "title": c.title, "authors": c.authors, "publication": c.publication,
        "year": c.year, "publisher": c.publisher, "status": result.status if result else resolution.status,
        "provider": resolution.provider, "matched_title": resolution.matched_title,
        "match_score": f"{resolution.match_score:.4f}", "doi": resolution.doi, "arxiv_id": resolution.arxiv_id,
        "landing_url": resolution.landing_url, "pdf_url": result.url if result else (resolution.pdf_urls[0] if resolution.pdf_urls else ""),
        "attempted_urls": " | ".join(attempted), "failure_reason": failure or (result.error if result else resolution.error),
        "suggested_action": "人工访问落地页或图书馆检索；补充合法 PDF 后重新运行" if (not resolution.pdf_urls or (result is not None and result.status == "failed")) else "",
    }


def write_csv(path: Path, rows: list[dict]) -> None:
    fields = list(flatten(Resolution(Citation(0, "")), None, []).keys())
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("citations", type=Path, help="citation CSV containing Title, Authors, Publication and Year")
    parser.add_argument("--output", type=Path, default=Path("downloads/citations"))
    parser.add_argument("--email", default="paper-downloader@example.com", help="contact email for polite APIs and optional Unpaywall")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=float, default=60)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--resolve-only", action="store_true", help="resolve links and write reports without downloading PDFs")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--cache", type=Path, help="resolver cache JSON (default: <output>/resolver-cache.json)")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    citations = load_citations(args.citations)
    if args.limit is not None:
        citations = citations[:max(0, args.limit)]
    args.output.mkdir(parents=True, exist_ok=True)
    resolver = Resolver(args.email, args.cache or args.output / "resolver-cache.json", min(args.timeout, 30))
    resolutions = []
    for index, citation in enumerate(citations, 1):
        resolution = resolver.resolve(citation); resolutions.append(resolution)
        print(f"[resolve {index}/{len(citations)}] {resolution.status}: {citation.title}")
        if index % 25 == 0:
            resolver.save()
    resolver.save()
    results: dict[int, tuple[Result | None, list[str], str]] = {}

    def download(resolution: Resolution):
        attempted, failures = [], []
        if args.resolve_only:
            return None, attempted, ""
        for url in resolution.pdf_urls:
            attempted.append(url)
            result = download_one(paper_for(resolution, url), args.output, args.timeout, args.retries, args.overwrite)
            if result.status in {"downloaded", "skipped"}:
                return result, attempted, ""
            failures.append(result.error)
        return None, attempted, "; ".join(x for x in failures if x) or ("No public PDF URL found" if not attempted else "All public PDF attempts failed")

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        future_map = {pool.submit(download, r): r for r in resolutions}
        for future in concurrent.futures.as_completed(future_map):
            r = future_map[future]; results[r.citation.row_number] = future.result()
    all_rows, failed_rows = [], []
    for resolution in resolutions:
        result, attempted, failure = results[resolution.citation.row_number]
        row = flatten(resolution, result, attempted, failure)
        all_rows.append(row)
        needs_followup = (not resolution.pdf_urls) if args.resolve_only else (result is None or result.status == "failed")
        if needs_followup:
            failed_rows.append(row)
    write_csv(args.output / "download-report.csv", all_rows)
    write_csv(args.output / "failed-downloads.csv", failed_rows)
    summary = {"citations": len(citations), "resolved_public_pdf": sum(bool(r.pdf_urls) for r in resolutions), "downloaded_or_existing": sum((results[r.citation.row_number][0] is not None and results[r.citation.row_number][0].status in {"downloaded", "skipped"}) for r in resolutions), "failed_or_not_public": len(failed_rows)}
    (args.output / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False)); print(f"manual follow-up: {args.output / 'failed-downloads.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

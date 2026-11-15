import csv
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
SPEC = importlib.util.spec_from_file_location("citation_downloader", HERE / "citation_downloader.py")
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class CitationDownloaderTests(unittest.TestCase):
    def test_csv_loads_and_deduplicates_titles(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "citations.csv"
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=["Authors", "Title", "Publication", "Year"])
                writer.writeheader()
                writer.writerow({"Authors": "A", "Title": "Paper: One", "Publication": "Journal", "Year": "2025"})
                writer.writerow({"Authors": "A", "Title": "Paper One", "Publication": "Journal", "Year": "2025"})
            rows = module.load_citations(path)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0].year, "2025")

    def test_title_score_rejects_unrelated_and_accepts_punctuation_change(self):
        self.assertGreater(module.title_score("Sound Event Detection: A Review", "Sound Event Detection — A Review"), 0.95)
        self.assertLess(module.title_score("Sound Event Detection", "Protein Folding with Graphs"), 0.4)

    def test_direct_arxiv_resolution(self):
        with tempfile.TemporaryDirectory() as temp:
            resolver = module.Resolver("test@example.com", Path(temp) / "cache.json")
            citation = module.Citation(2, "Example", publication="arXiv preprint arXiv:2406.09167", year="2024")
            result = resolver.direct_arxiv(citation)
            self.assertIsNotNone(result)
            self.assertEqual(result.arxiv_id, "2406.09167")
            self.assertEqual(result.pdf_urls, ["https://arxiv.org/pdf/2406.09167"])

    def test_failed_csv_contains_manual_followup_fields(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "failed-downloads.csv"
            citation = module.Citation(2, "Unavailable Paper", "A", "Journal", "2025")
            row = module.flatten(module.Resolution(citation, landing_url="https://doi.org/10.1/test"), None, [], "No public PDF URL found")
            module.write_csv(path, [row])
            with path.open(encoding="utf-8-sig", newline="") as handle:
                saved = next(csv.DictReader(handle))
            self.assertEqual(saved["failure_reason"], "No public PDF URL found")
            self.assertIn("人工", saved["suggested_action"])
            self.assertEqual(saved["landing_url"], "https://doi.org/10.1/test")


if __name__ == "__main__":
    unittest.main()

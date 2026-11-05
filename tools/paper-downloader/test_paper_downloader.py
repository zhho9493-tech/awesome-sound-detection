import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("paper_downloader.py")
SPEC = importlib.util.spec_from_file_location("paper_downloader", MODULE_PATH)
downloader = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = downloader
SPEC.loader.exec_module(downloader)


class PaperDownloaderTests(unittest.TestCase):
    def test_arxiv_urls_are_canonical_and_deduplicated(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "papers.md").write_text(
                "[PDF](https://arxiv.org/pdf/2501.12345.pdf)\n"
                "[same](https://arxiv.org/abs/2501.12345)\n",
                encoding="utf-8",
            )
            papers = downloader.discover(root)
            self.assertEqual(len(papers), 1)
            self.assertEqual(papers[0].url, "https://arxiv.org/pdf/2501.12345")
            self.assertEqual(papers[0].filename, "2501.12345.pdf")

    def test_json_download_fields_are_discovered(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "index.json").write_text(json.dumps({"title": "Paper A", "pdf_url": "https://example.org/a.pdf"}))
            papers = downloader.discover(root)
            self.assertEqual(len(papers), 1)
            self.assertEqual(papers[0].title, "Paper A")

    def test_download_validates_pdf(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "source.pdf"
            output = root / "output"
            output.mkdir()
            source.write_bytes(b"%PDF-1.4\nmock paper\n%%EOF\n")
            paper = downloader.Paper("test", source.as_uri(), filename="paper.pdf")
            result = downloader.download_one(paper, output, timeout=3, retries=0, overwrite=False)
            self.assertEqual(result.status, "downloaded")
            self.assertTrue(downloader.is_pdf(output / "paper.pdf"))


if __name__ == "__main__":
    unittest.main()

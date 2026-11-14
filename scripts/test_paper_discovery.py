#!/usr/bin/env python3
"""Lightweight smoke tests for public paper discovery identity and URL guards."""
import importlib.util
import unittest
from pathlib import Path

P = Path(__file__).resolve().parents[0] / "build_paper_discovery.py"
spec = importlib.util.spec_from_file_location("paper_discovery", P)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class DiscoveryChecks(unittest.TestCase):
    def test_arxiv_identity(self):
        self.assertEqual(mod.aid("https://arxiv.org/abs/2601.12345v2"), "2601.12345")
        self.assertEqual(mod.aid("arxiv-2610.31346"), "2610.31346")
        self.assertEqual(mod.aid("random title"), "")
    def test_doi(self):
        self.assertEqual(mod.doi("https://doi.org/10.1109/ABC.2026.123"),"10.1109/abc.2026.123")
        self.assertEqual(mod.doi("not-a-doi"),"")
    def test_private_url_blocked(self):
        hosts=("arxiv.org","doi.org","openreview.net")
        for url in ("https://drive.google.com/file/d/x","https://example.com/private","http://arxiv.org/pdf/1234.5678","https://arxiv.org.evil.test/abs/2601.12345"):
            self.assertEqual(mod.clean_url(url,hosts),"")
        self.assertEqual(mod.clean_url("https://arxiv.org/abs/2601.12345",hosts),"https://arxiv.org/abs/2601.12345")
    def test_category_coercion(self):
        self.assertEqual(mod.cat(["das","sound-event"]),["das","sound-event"])
        self.assertEqual(mod.cat("das;sound-event"),["das","sound-event"])

if __name__ == "__main__":
    unittest.main()

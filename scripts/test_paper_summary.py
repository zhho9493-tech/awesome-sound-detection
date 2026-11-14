#!/usr/bin/env python3
"""Regression tests: paper summaries must be extractive and not hallucinated."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).parent))
from paper_summary import extract_summary, sentences

class SummaryTests(unittest.TestCase):
    def test_missing_abstract(self):
        s=extract_summary("", "A Paper Title")
        self.assertEqual(s["status"],"needs-abstract")
        self.assertFalse(s["objective"])
        self.assertFalse(s["method"])
        self.assertFalse(s["finding"])
    def test_only_source_sentences(self):
        abstract=("Industrial acoustic anomaly detection under noisy conditions is difficult. "
                  "We propose an uncertainty-aware prototype model for acoustic events. "
                  "Experiments show improved accuracy on the collected benchmark.")
        s=extract_summary(abstract)
        self.assertEqual(s["status"],"abstract-extract")
        for key in ("objective","method","finding"):
            if s[key]:
                self.assertIn(s[key],abstract)
        self.assertIn("We propose",s["method"])
        self.assertIn("Experiments show",s["finding"])
    def test_no_unstated_result(self):
        abstract="We propose a self-supervised encoder. The dataset contains field recordings."
        s=extract_summary(abstract)
        self.assertFalse(s["finding"])
    def test_unicode_sentence(self):
        self.assertGreaterEqual(len(sentences("提出一种方法。实验数据来自现场。")),2)

if __name__=="__main__":unittest.main()

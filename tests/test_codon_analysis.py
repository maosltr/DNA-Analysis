import unittest
from src.analysis import codon_analysis
import HtmlTestRunner


class UnitTestsCodonAnalysis(unittest.TestCase):
    def test_codon_analysis_1(self):
        codon = codon_analysis.analyze_codon("AUC")
        self.assertEqual(codon, "Isoleucine")

    def test_codon_analysis_2(self):
        codon = codon_analysis.analyze_codon("UCU")
        self.assertEqual(codon, "Serine")


if __name__ == "__main__":
    # unittest.main()
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            report_name="test_report", output="tests"
        )
    )

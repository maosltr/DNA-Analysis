import unittest
from src.analysis import codon_analysis


class UnitTests(unittest.TestCase):
    def test_codon_analysis(self):
        codon = codon_analysis.analyze_codon("AUC")
        self.assertEqual(codon, "Isoleucine")
        codon = codon_analysis.analyze_codon("UCU")
        self.assertEqual(codon, "Serine")


if __name__ == "__main__":
    # unittest.main()
    unittest.test_codon_analysis()

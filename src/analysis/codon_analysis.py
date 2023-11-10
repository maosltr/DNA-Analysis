import os
from utils import utils
import argparse


def analyze_codon(codon):
    """Function that returns amino acids from genetic code dictionary.

    Args:
        genetic_code_dict
        codon: eg. "AUC"

    Returns:
        amino_acid: eg. "Isoleucine"
    """

    dataset = "genetic_code.tsv"
    dataset_path = os.path.join(os.getcwd(), "data", dataset)
    genetic_code_dict = utils.tsv_to_dict(dataset_path)

    amino_acid = genetic_code_dict[codon][2]

    return amino_acid


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the amino acid from the codon")
    parser.add_argument("--c", dest="codon", type=str, help="Codon (eg. 'AUC')")

    args = parser.parse_args()

    amino_acid = analyze_codon(args.codon)
    print(analyze_codon("AUC"))

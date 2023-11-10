import os
from utils import utils


def analyze_codon(genetic_code_dict, codon):
    """Function that returns amino acids from genetic code dictionary.

    Args:
        genetic_code_dict
        codon: eg. "AUC"

    Returns:
        amino_acid: eg. "Isoleucine"
    """

    amino_acid = genetic_code_dict[codon][2]

    return amino_acid


def main():
    dataset = "genetic_code.tsv"
    dataset_path = os.path.join(os.getcwd(), "data", dataset)
    genetic_code_dict = utils.tsv_to_dict(dataset_path)

    print(analyze_codon(genetic_code_dict, "AUC"))


if __name__ == "__main__":
    main()

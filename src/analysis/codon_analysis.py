import os
from utils import utils
import argparse
import pandas as pd


def analyze_codon(codon):
    """Function that returns amino acids Name from the codon.

    Args:
        codon: eg. "AUC"

    Returns:
        amino_acid Full Name: eg. "Isoleucine"
    """

    dataset = "genetic_code.tsv"

    dataset_path = os.path.join(os.getcwd(), "data", dataset)
    df = pd.read_csv(dataset_path, sep="\t")
    column_names = ["Codon", "Amino Acid", "Abbreviation", "Full Name"]
    df.columns = column_names

    return df[df["Codon"] == codon]["Full Name"].values[0]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the amino acid from the codon")
    parser.add_argument(
        "--c", dest="codon", type=str, help="Codon (eg. 'AUC')", required=True
    )

    args = parser.parse_args()

    amino_acid = analyze_codon(args.codon)
    print(amino_acid)

import csv

def tsv_to_dict(data_file):
    """
    Return a Dict from a .tsv file

    :param data_file: path to a .tsv file
    :type data_file: .tsv file
    :return: Dictionary
    :rtype: Dict

    """    

    RNAcode= {}

    with open(data_file, "r", encoding="utf-8") as file:
        tsvreader = csv.reader(file, delimiter='\t')

        for row in tsvreader:
            RNAcode[row[0]] = [row[1], row[2], row[3]]
    
    return RNAcode
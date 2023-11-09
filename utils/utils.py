

def tsv_to_dict(data_file):

    RNAcode= {}

    with open(data_file, "r", encoding="utf-8") as file:
        tsvreader = csv.reader(file, delimiter='\t')

        for row in tsvreader:
            RNAcode[row[0]] = [row[1], row[2], row[3]]
    
    return RNAcode
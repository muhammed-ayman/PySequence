from complementDNA import complement_DNA


def check_DNA_complement_DNA(seq_1, seq_2):  # get the two DNA sequences
    seq_1_comp = complement_DNA(seq_1)  # get the complementary sequence for seq_1
    if seq_1_comp == seq_2.lower():
        return True  # returning True in case the sequences are complementary

    return False  # default return of False

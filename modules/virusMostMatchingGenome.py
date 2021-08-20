from os import path
from sequencesMatchingPercentage import sequences_matching_percentage
from checkDNAValidity import check_DNA_validity
from checkRNAValidity import check_RNA_validity


def virus_most_matching_genome(virus_seq, comp_seq):  # getting the virus sequence and the file path that includes known viruses' sequences
    if not path.isfile(comp_seq):
        return False  # returning false in case the file path given doesn't exist

    file = open(comp_seq, 'r')
    seqs = []

    # loading the vaild sequences in the file in the seqs array

    for line in file.readlines():
        line = line.strip('\n')
        if check_DNA_validity(line) or check_RNA_validity(line):
            seqs.append(line)

    # calculates the most matching sequences based on the minimum edit distance algorithm

    most_matching_seqs = []
    highest_val = 0
    most_matching_seq = ''
    for seq in seqs:
        per_match = sequences_matching_percentage(virus_seq, seq)
        if per_match > highest_val:
            highest_val = per_match
            most_matching_seq = seq
    for seq in seqs:
        if sequences_matching_percentage(virus_seq, seq) == highest_val:
            most_matching_seqs.append(seq)

    return most_matching_seqs  # returning an array with the closest known viruses' genomes to the given one's

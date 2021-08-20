from os import path
from sequencesMatchingPercentage import sequences_matching_percentage
from checkDNAValidity import check_DNA_validity
from checkRNAValidity import check_RNA_validity


# returns a 2D array each of its array elements has two subsequent elements with the two most matching sequences

def most_matching_seqs(seqs_arr):  # getting an array with genomic sequences
    most_matching_seqs = []
    per_match = 0

    # calculates the matching percentage between all the elements and loads the most_matching_seqs with the most matching ones

    for i in range(len(seqs_arr)):
        for j in range(i + 1, len(seqs_arr)):
            match_per = sequences_matching_percentage(seqs_arr[i],
                    seqs_arr[j])
            if match_per > per_match:
                most_matching_seqs = [[seqs_arr[i], seqs_arr[j]]]
                per_match = match_per
            elif match_per == per_match:
                most_matching_seqs.append([seqs_arr[i], seqs_arr[j]])
            else:
                pass

    return most_matching_seqs


# loads the genomic sequences separately (DNA, RNA) from the file's path given

def load_RNA_and_DNA_seqs(seqs_path):
    rna_seqs = []
    dna_seqs = []
    file = open(seqs_path, 'r')

    # adds the RNA sequences to rna_seqs and the DNA ones to dna_seqs

    for line in file.readlines():
        line = line.strip('\n')
        if check_DNA_validity(line):
            dna_seqs.append(line)
        elif check_RNA_validity(line):
            rna_seqs.append(line)
        else:
            pass

    return (rna_seqs, dna_seqs)


# utilizes the above functions to get the two most matching RNA sequences and DNA ones

def two_closest_sequences(seqs_path):
    if not path.isfile(seqs_path):
        return False

    (rna_seqs, dna_seqs) = load_RNA_and_DNA_seqs(seqs_path)
    rna_most_matching_seqs = most_matching_seqs(rna_seqs)
    dna_most_matching_seqs = most_matching_seqs(dna_seqs)

    return (rna_most_matching_seqs, dna_most_matching_seqs)

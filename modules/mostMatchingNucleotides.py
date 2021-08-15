# getting a genomic sequence and a nucleotide type to count the number of occurences of this nucleotide in the sequence

def count_nucleotide(seq, nuc):
    nuc_count = 0
    for seq_nuc in seq:
        if seq_nuc.upper() == nuc:
            nuc_count += 1

    return nuc_count  # returning the nucleotide count


# getting a genomic sequence and generating an array of each nucleotide count in the following order [A, G, T (OR) U, C]

def generate_nucs_count(seq, changing_nuc):
    seq_nucs_count = [count_nucleotide(seq, 'A'), count_nucleotide(seq,
                      'G'), count_nucleotide(seq, changing_nuc),
                      count_nucleotide(seq, 'C')]

    return seq_nucs_count  # returning the generated array of nucleotides counts


# getting two genomic sequences and returning the most matching nucleotides between them

def most_matching_nucleotides(seq_one, seq_two, seq_type):
    if seq_type.lower() == 'rna':
        changing_nuc = 'U'
    else:
        changing_nuc = 'T'
    nucs_order = ['A', 'G', changing_nuc, 'C']
    seq_one_nucs_count = generate_nucs_count(seq_one, changing_nuc)  # generating nucleotides counts array
    seq_two_nucs_count = generate_nucs_count(seq_two, changing_nuc)  # generating nucleotides counts array

    # calculating the difference between the number of occurences of each nucleotide between the two sequences

    nucs_diff = []
    for i in range(len(seq_one_nucs_count)):
        nucs_diff.append(abs(seq_one_nucs_count[i]
                         - seq_two_nucs_count[i]))

    # calculating the least difference between a particular nucleotide in both sequences

    least_diff = nucs_diff[0]
    for i in range(len(nucs_diff)):
        if nucs_diff[i] < least_diff:
            least_diff = nucs_diff[i]

    # generating an array with the nucleotides having the least occurence difference

    most_matching_nucs = []
    for i in range(len(nucs_diff)):
        if nucs_diff[i] == least_diff:
            most_matching_nucs.append(nucs_order[i])

    return most_matching_nucs  # returning an array of the most matching nucleotides

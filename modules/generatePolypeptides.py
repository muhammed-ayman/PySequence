def generate_triplets(seq):                    # getting the sequence that is wanted to be sliced into triplets
    seq_ = []
    for i in range(0, len(seq), 3):
        if i + 3 < len(seq):
            seq_.append(seq[i:i+3].upper())
        else:
            seq_.append(seq[i:].upper())
    return seq_                                # returning a list of 3-char-strings(triplets)


def get_amino_acid(codon):   # receiving an str input, one codon at a time
    # declaring a dictionary storing the codons and their amino acids correspondents
    corres = {'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu', 'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
              'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': '', 'UAG': '', 'UGU': 'Cys', 'UGC': 'Cys', 'UGA': '', 'UGG': 'Trp',
              'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu', 'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
              'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln', 'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
              'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met', 'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
              'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys', 'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
              'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val', 'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
              'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu', 'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'}
    return corres[codon.upper()]    # returning the corresponding amino acid


def generate_gene_RNA(seq):                                 # Getting an input of RNA sequence
    coding = []                                             # To store the coded sites
    if 'AUG' not in seq:
        return False
    while 'AUG' in seq:
        ind_ = seq.find('AUG')
        seq = seq[ind_:]                                    # Getting rid of unnecessary leads
        seq = generate_triplets(seq)                        # Separating nucleotides in triplets forms
        start_codon = False
        stop_codon = False
        coding_ = ''
        for i in range(len(seq)):
            if len(seq[i]) == 3:
                if seq[i] == 'AUG' and start_codon == False:
                    start_codon = True
                    stop_codon = False
                if start_codon == True:
                    coding_ += seq[i]
                if seq[i] in ['UAA', 'UAG', 'UGA']:
                    start_codon = False
                    stop_codon = True
                    coding.append(coding_)
                    coding_ = ''
                    seq = "".join(seq[i + 1:])              # Joining back the remaining sequence
                    break
        if not stop_codon:
            coding.append(coding_)
            seq = []
    coding = [generate_triplets(i) for i in coding]
    return coding                                           # Returning a list of lists of codons to be translated


def generate_polypeptides(seq):                             # Getting an RNA sequence
    if not generate_gene_RNA(seq):                          # Checking if the sequence contains a start codon
        return False
    traits = generate_gene_RNA(seq)
    generated_polypeptides = []
    for site in traits:
        poly_ = []
        for i in range(len(site)):
            amino = get_amino_acid(site[i])
            if amino != '':
                poly_.append(amino)
        poly_peptide = "–".join(poly_)
        if poly_peptide:
            generated_polypeptides.append(poly_peptide)
    return generated_polypeptides                       # Returning a list of the formed polypeptide chains



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


def generate_gene_RNA(seq):                             # getting triplets input
    RNAgenes = []
    RNAgene = []                                        # storing each slice beginning with a start codon
    start_codon = False
    for i in range(len(seq)):
        if seq[i] == 'AUG' and start_codon == False:
            start_codon = True
        if start_codon == True:
            RNAgene.append(seq[i])
        if seq[i] in ['UAA', 'UAG', 'UGA']:
            start_codon = False
            RNAgenes.append(RNAgene)
            RNAgene = []
    return RNAgenes                                     # returning a 2D array of RNA gene-versions


def generate_polypeptides(codons):                     # getting a list of codons after slicing the RNA strand
    traits = generate_gene_RNA(codons)                 # generating lists of RNA gene-versions
    generated_polypeptides = []
    for seq in traits:
        poly_ = []                                     # an empty list to store the translated amino acids
        for i in range(len(seq)):                      # iterating over the list of codons
            amino = get_amino_acid(seq[i])             # calling the corresponding amino acid of each codon
            if amino != '':
                poly_.append(amino)                    # listing amino acids in order
        poly_peptide = "–".join(poly_)                 # joining amino acids
        generated_polypeptides.append(poly_peptide)
    return generated_polypeptides                      # returning the polypeptide chains

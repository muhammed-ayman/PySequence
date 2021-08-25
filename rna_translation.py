from main import *


def main():
    while True:
        rnaSequence_input = input('Enter RNA sequence > ')
        if check_RNA_validity(rnaSequence_input):
            break
        print(invalid_RNA_seq)

    rnaSequence_triplets = generate_triplets(rnaSequence_input)
    result = generate_polypeptides(rnaSequence_triplets)
    if len(result) > 0:
        print(f'[+]: The Translated RNA Segment(s) is {result}')
    else:
        print(f'[+]: There is no Start Codon')

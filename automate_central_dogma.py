from main import *


def main():
    while True:
        dnaSequence_input = input('Enter The DNA sequence > ')
        if check_DNA_validity(dnaSequence_input):
            break
        print(invalid_DNA_seq)

    printMsgWithDelay(f'\n[=]: Transcribing The DNA\n', 1)
    transcribed_dna = transcribe(dnaSequence_input)
    print(f'[+]: The Transcribed DNA: {transcribed_dna}\n')
    printMsgWithDelay(f'[=]: Translating The RNA\n', 1)
    rnaSequence_triplets = generate_triplets(transcribed_dna)
    result = generate_polypeptides(rnaSequence_triplets)
    if len(result) > 0:
        print(f'[+]: The Translated RNA Segment(s) is {result}')
    else:
        print(f'[+]: There is no Start Codon')

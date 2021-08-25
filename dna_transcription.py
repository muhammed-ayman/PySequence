from main import *


def main():
    while True:
        dnaSequence_input = input('Enter DNA sequence > ')
        if check_DNA_validity(dnaSequence_input):
            break
        print(invalid_DNA_seq)
    result = transcribe(dnaSequence_input)
    print(f'[+]: The transcribed DNA is {result}')

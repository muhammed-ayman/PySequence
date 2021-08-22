from main import *

# returns whether two genomic sequences are of the same type or not
def checkSequenceTypeSimilarity(seq_one, seq_two):
    seq_one_type = 'DNA'
    seq_two_type = 'DNA'
    if check_RNA_validity(seq_one) and not (check_DNA_validity(seq_one)):
        seq_one_type = 'RNA'
    if check_RNA_validity(seq_two) and not (check_DNA_validity(seq_two)):
        seq_two_type = 'RNA'
    if seq_one_type != seq_two_type:
        return (False , seq_one_type)

    return (True , seq_one_type)

# returns a genomic sequence input from the user and handles the errors
def getSequence(user_msg):
    while True:
        seq = input(user_msg)
        if check_DNA_validity(seq) or check_RNA_validity(seq):
            break
        printMsgWithDelay(invalid_seq, 1)

    return seq


# The following functions utilize the above ones & the required modules \
# to process the input and prints the output to the user

def feature_1():
    while True:
        seq_one = getSequence('Enter the first Sequence > ')
        seq_two = getSequence('Enter the second Sequence > ')
        if not (checkSequenceTypeSimilarity(seq_one, seq_two)[0]):
            printMsgWithDelay(invalid_seqs_types, 1)
            continue
        break

    feature_output = round(sequences_matching_percentage(seq_one, seq_two),2)
    print(f'[+]: The sequences matching percentage is {feature_output}%')


def feature_2():
    while True:
        file_path = input('Enter the file relative path > ')
        if not two_closest_sequences(file_path):
            printMsgWithDelay(invalid_file_path, 1)
            continue
        break

    feature_output = two_closest_sequences(file_path)
    if len(feature_output[0]) > 0:
        print(f'[+]: The most matching RNA sequences are {feature_output[0][0]}')
    if len(feature_output[1]) > 0:
        print(f'[+]: The most matching DNA sequences are {feature_output[1][0]}')


def feature_3():
    while True:
        seq_one = getSequence('Enter the first Sequence > ')
        seq_two = getSequence('Enter the second Sequence > ')
        similarity_check_result = checkSequenceTypeSimilarity(seq_one, seq_two)
        if not (similarity_check_result[0]):
            printMsgWithDelay(invalid_seqs_types, 1)
            continue
        break

    feature_output = most_matching_nucleotides(seq_one, seq_two, similarity_check_result[1])

    if len(feature_output) > 1:
        print(f'[+]: The most matching nucleotides are {feature_output}')
    elif len(feature_output) == 1:
        print(f'[+]: The most matching nucleotide is {feature_output[0]}')
    else:
        print(f'[+]: There are no matching nucleotides!')


def feature_4():
    while True:
        virus_seq = input('Enter the virus genomic sequence > ')
        if not(check_DNA_validity(virus_seq) or check_RNA_validity(virus_seq)):
            printMsgWithDelay(invalid_seq, 1)
            continue
        break

    while True:
        file_path = input('Enter the genomic sequences to be compared file path > ')
        match_result = virus_most_matching_genome(virus_seq, file_path)
        if not(match_result):
            printMsgWithDelay(invalid_file_path, 1)
            continue
        break

    if len(match_result) > 1:
        print(f'[+]: The most matching genomic sequences to the virus\'s are {match_result}')
    elif len(match_result) == 1:
        print(f'[+]: The most matching genomic sequence to the virus\'s is {match_result[0]}')
    else:
        print(f'[+]: There are no matching sequences')

# outputs the multi-strand analysis welcome message \
# from the main_helper to the user and directs them to their required feature

def main(first=True):
    if first:
        printMsgWithDelay(multi_strand_analysis_msg, 1)
    multi_strand_analysis_choice = input('> ')
    if not fetchInputError(multi_strand_analysis_choice\
    , 'multiStrandAnalysisPrompt'):
        main(False)
    else:
        eval(multi_strand_analysis_options\
        [multi_strand_analysis_choice] + "()")

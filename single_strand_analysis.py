from main_helper import *

def getDNA():
    while True:
        dna_seq = check_DNA_validity(input('Enter your DNA Sequence > '))
        if dna_seq:
            break
        printMsgWithDelay(invalid_DNA_seq, 1)

    return dna_seq


def getRNA():
    while True:
        rna_seq = check_RNA_validity(input('Enter your RNA Sequence > '))
        if rna_seq:
            break
        printMsgWithDelay(invalid_RNA_seq, 1)

    return rna_seq

def feature_1(first=True):
    dna_seq = getDNA()
    feature_output_1 = number_of_each_nucleotide(dna_seq)
    feature_output_2 = percentage_of_each_nucleotide(dna_seq)
    print(f'[+]: Your nucleotide occurrence in the strand is [G,C,T,A]: {feature_output_1}')
    print(f'[+]: Their Percentages are [G,C,T,A]: {feature_output_2}')


def feature_2():
    dna_seq = getDNA()
    feature_output = complement_DNA(dna_seq)
    print(f'[+]: Your complementary strand is: {feature_output}')


def feature_3():
    dna_seq = getDNA()
    feature_output = cg_content(dna_seq)
    print(f'[+]: The G-C content in your strand is: {feature_output}')


def feature_4():
    dna_seq = getDNA()
    feature_output = ' ' if is_palindrome(dna_seq) else ' NOT '
    print(f'[+]: Your strand is{feature_output}a palindrome!')


def feature_5():
    dna_seq = getDNA()
    while True:
        dna_to_ligate = input('Enter the segment you want to ligate to the original sequence > ')
        if check_DNA_validity(dna_to_ligate):
            break
        printMsgWithDelay(invalid_DNA_seq, 1)
    while True:
        ligate_index = input('Enter the nucleotide index after which you want to ligate the segment > ')
        if ligate_index.isdigit() == True:
            if len(dna_seq) > int(ligate_index) >= 0:
                break
        printMsgWithDelay(invalid_index, 1)
    feature_output = ligate(dna_to_ligate,dna_seq,int(ligate_index))
    print(f'[+]: Your Segment after ligation > {feature_output}')

def feature_6():
    dna_seq = getDNA()
    while True:
        search_segment = input('Enter the segment you want to search for > ')
        if check_DNA_validity(search_segment):
            break
        printMsgWithDelay(invalid_DNA_seq, 1)
    feature_output = ' does ' if restriction_enzyme(dna_seq , search_segment) else ' does NOT '
    print(f'[+]: Your segment{feature_output}exist in the strand!')


def feature_7():
    dna_seq = getDNA()
    while True:
        count_segment = input('Enter the segment you want to find its count > ')
        if check_DNA_validity(count_segment):
            break
        printMsgWithDelay(invalid_DNA_seq, 1)
    feature_output = STPs(dna_seq, count_segment)
    if feature_output != 0:
        print(f'[+]: Your segment occurs {feature_output} times!')
    else:
        print(f'[+]: Your segment doesn\'t occur in the strand')


def feature_8():
    dna_seq = getDNA()
    feature_output = reverse_complement(dna_seq)
    print(f'[+]: The reverse of the complement of your enetred strand is > {feature_output}')


def feature_9():
    rna_seq = getRNA()
    feature_output = reverse_transcriptase(rna_seq)
    print(f'[+]: The DNA strand from your entered RNA strand is > {feature_output}')

def main(first=True):
    if first:
        printMsgWithDelay(single_strand_analysis_msg, 1)
    single_strand_analysis_choice = input('> ')
    if not fetchInputError(single_strand_analysis_choice, 'singleStrandAnalysisPrompt'):
        main(False)
    else:
        eval(single_strand_analysis_options[single_strand_analysis_choice] + "()")

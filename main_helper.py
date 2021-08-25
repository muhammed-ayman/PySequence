import time
import sys
import os

# Appending the modules directory into the main_helper to import all modules

current_working_dir = \
    os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
modules_dir = f'{current_working_dir}/modules'
sys.path.append(modules_dir)

# Importing Modules

from checkDNAValidity import check_DNA_validity
from checkRNAValidity import check_RNA_validity
from nucleotideOccurence import number_of_each_nucleotide
from nucleotideOccurence import percentage_of_each_nucleotide
from complementDNA import complement_DNA
from complementDNA import reverse_complement
from cgContent import cg_content
from IsPalindrome import is_palindrome
from Ligate import ligate
from restrictionEnzyme import restriction_enzyme
from shortTandemRepeat import STPs
from reverseTranscriptase import reverse_transcriptase
from virusMostMatchingGenome import virus_most_matching_genome
from twoClosestSequences import two_closest_sequences
from sequencesMatchingPercentage import sequences_matching_percentage
from mostMatchingNucleotides import most_matching_nucleotides
from transcribe import transcribe
from generateTriplets import generate_triplets
from generatePolypeptides import generate_polypeptides
from longestRepeat import get_longest_consecutive_repeat_s_

welcome_msg = \
    '''
👋Hello!
> This is a software that helps you analyze DNA & RNA strands
> You can also translate DNA & RNA strands to their corresponding polypeptide chains!
'''
main_prompt_msg = \
    """
Enter the number corresponding to the feature you want:
[1]: Analyze DNA & RNA strands
[2]: Proceed with the central dogma process
"""

central_dogma_msg = \
    """
Welcome to Central Dogma!
---------------------------
Enter the number corresponding to the feature you want:
[1]: DNA Transcription
[2]: RNA Translation
[3]: Automate Transcription & Translation
"""

analyze_strands_msg = \
    """
Welcome to Strand analysis!
---------------------------
Enter the number corresponding to the feature you want:
[1]: Single Strand Analysis
[2]: Multi-Strand Analysis
"""
single_strand_analysis_msg = \
    """
Welcome to Single Strand analysis!
----------------------------------
Enter the number corresponding to the feature you want:
[1]: Count the number of nucleotides and find their percentage
[2]: Find the complementary strand
[3]: Find the G-C content
[4]: Check whether the strand is a palindrome or not
[5]: Ligate a segment withing the strand
[6]: Search whether a certain segment exists
[7]: Count the number of times a segment occurs withing the strand
[8]: Find the reverse of the complementary strand
[9]: Reverse Transcriptase
"""
multi_strand_analysis_msg = \
    """
Welcome to Multi-Strand analysis!
----------------------------------
Enter the number corresponding to the feature you want:
[1]: Calculate the matching percentage between two genomic sequences
[2]: Get the two most matching sequences from a file
[3]: Get the most matching nucleotides in two genomic sequences
[4]: Get the closest genomic sequence to a given virus's one
"""
invalid_input = """
[!]: Invalid Input
[!]: Try Again
"""
invalid_DNA_seq = """
[!]: Invalid DNA Sequence
[!]: Try Again
"""
invalid_RNA_seq = """
[!]: Invalid RNA Sequence
[!]: Try Again
"""
invalid_seq = """
[!]: Invalid Sequence
[!]: Try Again
"""
invalid_file_path = """
[!]: Invalid File Path
[!]: Try Again
"""
invalid_seqs_types = """
[!]: The two sequences should be of the same type
[!]: Try Again
"""
invalid_index = """
[!]: Invalid Index
[!]: Try Again
"""
allowed_inputs = {'mainPrompt': [str(i) for i in range(1, 3)],
                  'analyzeStrandsPrompt': [str(i) for i in range(1,
                  3)], 'singleStrandAnalysisPrompt': [str(i) for i in
                  range(1, 10)],
                  'multiStrandAnalysisPrompt': [str(i) for i in range(1,5)]}
main_prompt_options = {'1': 'analyze_strands', '2': 'central_dogma'}
central_dogma_options = {'1': 'dna_transcription',
                         '2': 'rna_translation',
                         '3': 'automate_central_dogma'}
analyze_strands_options = {'1': 'single_strand_analysis',
                           '2': 'multi_strand_analysis'}
single_strand_analysis_options = {
    '1': 'feature_1',
    '2': 'feature_2',
    '3': 'feature_3',
    '4': 'feature_4',
    '5': 'feature_5',
    '6': 'feature_6',
    '7': 'feature_7',
    '8': 'feature_8',
    '9': 'feature_9',
    }
multi_strand_analysis_options = {
    '1': 'feature_1',
    '2': 'feature_2',
    '3': 'feature_3',
    '4': 'feature_4'
    }

def fetchInputError(input_value, input_type):
    if input_value not in allowed_inputs[input_type]:
        printMsgWithDelay(invalid_input, 0.25)
        return False
    return True


def printMsgWithDelay(msg, delay):
    print(msg)
    time.sleep(delay)

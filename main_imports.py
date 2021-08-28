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

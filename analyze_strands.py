from main_helper import *
import single_strand_analysis

def main(first=True):
    if first:
        printMsgWithDelay(analyze_strands_msg, 1)
    analyze_strands_choice = input('> ')
    if not fetchInputError(analyze_strands_choice, 'analyzeStrandsPrompt'):
        main(False)
    else:
        eval(analyze_strands_options[analyze_strands_choice] + ".main()")
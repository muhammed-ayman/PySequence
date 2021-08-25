from main_helper import *
import single_strand_analysis
import multi_strand_analysis


# initializes the strands analysis section and directs to the required sub-section

def main(first=True):
    if first:
        printMsgWithDelay(central_dogma_msg, 1)
    central_dogma_choice = input('> ')
    if not fetchInputError(central_dogma_choice,
                           'centralDogmaPrompt'):
        main(False)
    else:
        eval(central_dogma_options[central_dogma_choice] + '.main()'
             )

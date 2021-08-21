from main_helper import *
import analyze_strands


def welcomeMsg():
    printMsgWithDelay(welcome_msg, 1)
    mainPrompt()


def mainPrompt(first=True):
    if first:
        printMsgWithDelay(main_prompt_msg, 0.25)
    main_prompt_choice = input('> ')
    if not fetchInputError(main_prompt_choice, 'mainPrompt'):
        mainPrompt(False)
    else:
        eval(main_prompt_options[main_prompt_choice] + ".main()")


def main():
    welcomeMsg()

if __name__ == "__main__":
    main()

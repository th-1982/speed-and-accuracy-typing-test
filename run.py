"""This program runs a speed and accuracy typing test."""

import time
from os import system, name
from difflib import SequenceMatcher
from statistics import mean
from ast import literal_eval

import gspread
from google.oauth2.service_account import Credentials

from wonderwords import RandomSentence
from colorama import Fore, Style
import pandas as pd


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Speed-and-accuracy-test')

def clear():
    """
    Clear the terminal window when new text section is displayed adapoted from https://www.geeksforgeeks.org/clear-screen-python/
    """
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and linux
    else:
        system('clear')

    print(Fore.BLUE + 
    "*** Welcome to the Speed and Accuracy Typing Test! ***\n"
    )


def return_to_main():
    """
    Return the user to the beginning of the program  
    """
    print(Fore.GREEN +
        "\nHit enter when you are ready to return to the main menu. \n"
    )
    print(Style.RESET_ALL)
    user_input= input()
    if user_input== "":
        clear()
        main()
    else:
        clear()
        main()


def print_menu():
    """
    Display valid user options, exit or start game
    """
    menu = input(Fore.GREEN + """
    *** Welcome to the Speed and Accuracy Typing Test ***
    
    Main Menu: Please select the options
    1. Read the test Instructions
    2. Tips on improving your typing proficiency
    3. Sign up
    4. Start the Test
    5. Display the Record
    6. Exit the program\n
    """)

    return menu


def display_instructions():
    """
    This function displays the necessary instructions needed to make appropraite use of this application
    """
    instructions = """
How this typing test works is that it calculates your speed and your accuracy.
First we display some sentences to you then prompt you to type along.
"""
    print(Fore.BLUE + instructions)
    print(
        """* Read and follow prompts closely as you navigate through
    the program."""
    )
    print(
        """* When you encounter a choice menu, make sure to enter a
    valid choice."""
    )
    print(
        """* When you are ready to take the test, the program generates
    a paragraph of short random sentences."""
    )
    print(
        """* When you are ready, type the provided paragraph as quickly
    and accurately as possible."""
    )
    print("* Hit enter when you are done typing.")
    print(
        """* Your scores, including accuracy and speed will then be
    calculated and displayed."""
    )
    print(
        """* You will then be able to choose to save your score or return
    to the main menu."""
    )
    print(Style.RESET_ALL)

    return_to_main()


def tips():
    """
    Print on how to improve typing speed and accuracy
    """
    print("How can you improve?\n")
    print("Familiarize yourself with proper keyboard.\n")
    print("Learn proper overall positioning of the screen, your finger and your body.\n")
    print("Keep your eyes on the screen.\n")
    print("Practice regularly.\n")
    print("Take online type test on the internet. \n")
    print("Finally go to the internet to find more detailed advice.\n")

    return_to_main()


def choose_levels():
    """
    This function prompts the user to choose a level
    """
    print(Fore.CYAN + """Select the number for the corresponding level
1) Beginner
2) Intermediate
3) Advanced
""")
    print(Style.RESET_ALL)
    user_input = input()
    if user_input == '1':
        return generate_random_paragraph_beginner()
    elif user_input == '2':
        return generate_random_paragraph_medium()
    elif user_input == '3':
        return generate_random_paragraph_advanced()
    else:
        print("Invalid Input")


def _quit():
    exit()


def run_test_display_results():
    """
    Run the speed and accuracy typing test and display the results
    """
    user_input= input(
            "Hit enter when you are ready to see the paragraph.\n"
    )
    if user_input== "":
        sentences = choose_levels()
        print(Fore.GREEN + "*******************************************")
        print(sentences)
        print("*******************************************\n")
    else:
        sentences = choose_levels()
        print("*******************************************")
        print(sentences)
        print("*******************************************\n")
    print(Style.RESET_ALL)
    user_input= input(
            """Hit enter when you are ready to start typing.
    Do not hit enter again until you are done typing.\n"""
    )
    if user_input== "":
        print("Start typing now.\n")
        test_results = typed_paragraph()
        test_speed_cpm = round(test_results[1])
        test_speed_wpm = round(test_speed_cpm / 5)
        test_para = test_results[0]
    else:
        print("Start typing now.\n")
        test_results = typed_paragraph()
        test_speed_cpm = round(test_results[1])
        test_speed_wpm = round(test_speed_cpm / 5)
        test_para = test_results[0]

    test_typing_accuracy = determine_accuracy(sentences, test_para)

    print("\n******** YOUR SCORE REPORT ********\n")
    print(
        f"Typing accuracy is {test_typing_accuracy}%.\n"
    )
    print(f"Speed is {test_speed_cpm} characters/minute\n")
    print(f"that is approx. {test_speed_wpm} words/minute\n")

    if test_speed_cpm == 0:
        print("Your test scores are 0.")
        print(
            "You did not complete the test as designed"
        )

        return_to_main()

    results = [test_speed_cpm, test_speed_wpm, test_typing_accuracy]

    return results 


def generate_random_paragraph_advanced():
    """
    Create an advanced paragraph of random sentences using wonderwords.
    Adapted from:
    'https://towardsdatascience.com/speed-typing-test-project-with-python-da1a56987a5b'
    """
    sent_list = []
    sent_para = ""

    for i in range(15):
        sent = RandomSentence()
        random_sent = sent.sentence()
        sent_list.append(random_sent)
        sent_para += random_sent + " "

    test_para = sent_para[:-1]

    return test_para


def generate_random_paragraph_intermediate():
    """
    Create a intermediate paragraph of random sentences using wonderwords.
    Adapted from:
    'https://towardsdatascience.com/speed-typing-test-project-with-python-da1a56987a5b'
    """
    sent_list = []
    sent_para = ""

    for i in range(10):
        sent = RandomSentence()
        random_sent = sent.sentence()
        sent_list.append(random_sent)
        sent_para += random_sent + " "

    test_para = sent_para[:-1]

    return test_para


def generate_random_paragraph_beginner():
    """
    Create a beginner paragraph of random sentences using wonderwords.
    Adapted from:
    'https://towardsdatascience.com/speed-typing-test-project-with-python-da1a56987a5b'
    """
    sent_list = []
    sent_para = ""

    for i in range(5):
        sent = RandomSentence()
        random_sent = sent.sentence()
        sent_list.append(random_sent)
        sent_para += random_sent + " "

    test_para = sent_para[:-1]

    return test_para


def typed_paragraph():
    """
    This function captures the typed paragraph from the user and
    measures the time taken to type the paragraphy. Adapted from:
    'https://towardsdatascience.com/
    speed-typing-test-project-with-python-da1a56987a5b'
    """
    start_time = time.time()
    typed_para = input()
    end_time = time.time()

    time_taken = end_time - start_time
    speed = len(typed_para)/(time_taken/60)

    results = [typed_para, speed]

    return results


def determine_accuracy(sent_para, typed_para):
    """
    Accuracy is determined using SequenceMatcher
    """
    sequence_match = SequenceMatcher(a=sent_para, b=typed_para).ratio()
    result = round(100 * sequence_match, 1)

    return result


def see_old_scores_and_statistics():
    """
    Access google sheet with old scores and display scores and statistics
    in the terminal window
    """
    while True:
        try:
            print(
                Fore.GREEN + "Enter your username to see your scores and statistics:\n"
            )
            print(Style.RESET_ALL)
            usrnm = input().lower()
            user_scsht = SH.worksheet(usrnm)
            break
        except gspread.exceptions.WorksheetNotFound:
            while True:
                print(
                    f"\nWorksheet for '{usrnm}' not found\n"
                )
                print("Would you like to:\n")
                print("1. enter a different username or\n")
                print("2. return to the main menu?\n")
                print(
                    "Please enter your numeric choice:\n"
                )
                choice = input()
                if choice == '1':
 
                    see_old_scores_and_statistics()
                elif choice == '2':

                    main()
                else:
                    print(Fore.RED +
                        f"\nInvalid input: {choice}. Please enter 1 or 2.")
                    continue

    print(
        f"\nThe collective test results for '{usrnm}' are:\n"
    )
    dataframe = pd.DataFrame(user_scsht.get_all_records())
    print(dataframe)
    if dataframe.empty:
        print(
            '\nThere are no data in the scoresheet yet.'
        )
        print(
            '\nTake at least one test and save the score.'
        )
        return_to_main()

    try:
        user_speed_cpm_values = user_scsht.col_values(1)
        user_speed_wpm_values = user_scsht.col_values(2)
        user_accuracy_values = user_scsht.col_values(3)

        int_speed_cpm = [literal_eval(i) for i in user_speed_cpm_values[1:]]
        int_speed_wpm = [literal_eval(i) for i in user_speed_wpm_values[1:]]
        int_accuracy = [literal_eval(i) for i in user_accuracy_values[1:]]

        avg_speed_cpm = round(mean(int_speed_cpm))
        avg_speed_wpm = round(mean(int_speed_wpm))
        avg_accuracy = round(mean(int_accuracy), 1)

        print(f"\nStatistics for '{usrnm}'\n")
        print(f"Your average speed is {avg_speed_cpm} characters per minute\n")
        print(f"That is approx. {avg_speed_wpm} words per minute\n")
        print(f"Your average accuracy is {avg_accuracy}%\n")
    except SyntaxError:
        print('\n')
        print(
            Fore.RED + "A Syntax Error has occured and statistics can not be computed.\n"
        )
        print(Fore.RED + "The data file may be corrupted.\n")
        print(Style.RESET_ALL)

    return_to_main()

def create_user_score_sheet():
    """
    Create a google spread sheet to save scores for a new user
    """
    headings = ["speed in cpm", "speed in wpm", "accuracy"]
    print(Fore.GREEN +
        "Enter your username for a new score sheet:\n"
    )
    print(Style.RESET_ALL)
    usrnm = input().lower()
    while True:
        try:
            user_scsht = SH.worksheet(usrnm)
            print(
                f"\nA sheet with the name '{usrnm}' already exist.\n"
            )
            print("Do you you want to:\n")
            print("1. Choose a differnt username?\n")
            print(
                "2. Return to main menu and record data to existing sheet?\n"
            )
            print("Enter your numeric choice:\n")
            choice = input()
            if choice == '1':
                clear()
                create_user_score_sheet()
            elif choice == '2':
                clear()
                main()
            else:
                clear()
                print(
                    f"Invalid input: {choice}. Please enter 1 or 2"
                )
                continue
        except gspread.exceptions.WorksheetNotFound:
            user_scsht = SH.add_worksheet(title=usrnm, rows=100, cols=20)
            user_scsht.append_row(headings)
            print(Fore.GREEN +
                f"\nScoresheet for '{usrnm}' has been created.\n"
            )
            print(Fore.GREEN + "It can now be used to save scores of the test.\n")
            print(Style.RESET_ALL)
            return_to_main()




# These Python codes were taken and developed from the portfolio-project- 3 and the Love Sandwiches walkthrough project. 
"""This program runs a speed and accuracy typing test."""

import time
from os import system, name
from difflib import SequenceMatcher
from statistics import mean
from ast import literal_eval

import gspread
from google.oauth2.service_account import Credentials

from wonderwords import RandomSentence
from colorama import Fore, Back, Style
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

    print(Fore.YELLOW + Style.BRIGHT +
    "*** Welcome to the Speed and Accuracy Typing Test! ***\n" + Style.RESET_ALL
    )


def return_to_main():
    """
    Return the user to the beginning of the program  
    """
    print(Fore.GREEN + Style.BRIGHT +
        "\nPress enter when you are ready to return to the main menu. \n" + Style.RESET_ALL
    )
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
    print(Fore.YELLOW + Style.BRIGHT + "\n*** Welcome to the Speed and Accuracy Typing Test! ***\n" + Style.RESET_ALL)
    print(Fore.WHITE + "Main Menu: Please select the options\n" + Style.RESET_ALL)
    menu = input(
        """\n
    1. Read the test Instructions.\n
    2. Tips on improving your typing proficiency\n
    3. Sign up\n
    4. Start the Test\n
    5. Display the Record\n
    6. Delete Record from database\n
    7. Exit the program\n
"""
    )

    return menu


def display_instructions():
    """
    This function displays the necessary instructions needed to make appropraite use of this application
    """
    print(Fore.BLUE + Style.BRIGHT)
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
    print("* Press enter when you are done typing.")
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
    Print on how to improve speed and accuracy typing test
    """
    print(Fore.MAGENTA + Style.BRIGHT + "How can you improve in speed and accuracy typing test?\n")
    print(Style.RESET_ALL)
    print(Fore.WHITE + "Familiarize yourself with proper keyboard.\n")
    print("Learn proper overall positioning of the screen, your finger and your body.\n")
    print("Keep your eyes on the screen.\n")
    print("Practice regularly.\n")
    print("Take online type test on the internet. \n")
    print("Finally go to the internet to find more detailed advice.\n" + Style.RESET_ALL)

    return_to_main()


def choose_levels():
    """
    This function prompts the user to choose a level
    """
    print(Fore.CYAN + Style.BRIGHT + """Select the number for the corresponding level
1) Beginner
2) Intermediate
3) Advanced
""")
    print(Style.RESET_ALL)
    user_input = input()
    if user_input == '1':
        return generate_random_paragraph(5)
    elif user_input == '2':
        return generate_random_paragraph(10)
    elif user_input == '3':
        return generate_random_paragraph(15)
    else:
        print("Invalid Input")

        return_to_main()


def run_test_display_results():
    """
    Run the speed and accuracy typing test and display the results
    """
    user_input= input(Fore.GREEN + Style.BRIGHT +
            "Press enter when you are ready to see the paragraph.\n" + Style.RESET_ALL)
    if user_input== "":
        sentences = choose_levels()
        sentence_length = len(sentences.split('.'))
        print("*******************************************")
        print(sentences)
        print("*******************************************\n")
    else:
        sentences = choose_levels()
        sentence_length = len(sentences.split('.'))
        print("*******************************************")
        print(sentences)
        print("*******************************************\n")
    user_input= input(Fore.GREEN + Style.BRIGHT + 
            """Press enter when you are ready to start typing.
    Do not Press enter again until you are done typing.\n"""
    )
    print(Style.RESET_ALL)
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

    print(Fore.YELLOW + Style.BRIGHT + "\n******** YOUR SCORE REPORT ********\n" + Style.RESET_ALL)
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

    if sentence_length == 6:
        results = [test_speed_cpm, test_speed_wpm, test_typing_accuracy, "Beginner"]
    elif sentence_length == 11:
        results = [test_speed_cpm, test_speed_wpm, test_typing_accuracy, "Intermediate"]
    elif sentence_length == 16:
        results = [test_speed_cpm, test_speed_wpm, test_typing_accuracy, "Advanced"]
    else:
        results = [test_speed_cpm, test_speed_wpm, test_typing_accuracy, sentence_length]

    return results 


def delete_score_sheet():
    """
    Delete a user score sheet
    """
    while True:
        try:
            print(Fore.GREEN + Style.BRIGHT +
                "Enter username for the scoresheet you want to delete:\n" + Style.RESET_ALL
            )
            usrnm = input().lower()
            if usrnm == 'test':
                print(
                    f"\nThe scoresheet '{usrnm}' cannot be deleted."
                )
                return_to_main()
            user_scsht = SHEET.worksheet(usrnm)
            while True:
                print(
                    f"\nA sheet with the name '{usrnm}' exist.\n"
                )
                print(
                    "Are you sure want to delete it?\n"
                )
                print(
                  f"{Fore.GREEN}{Style.BRIGHT}Type 'yes' if you are ready to delete the sheet,\n"
    f"type 'no' if you do not want to delete it and\n"
    f"return to main menu.\n{Style.RESET_ALL}"
                )
                choice = input()
                if choice == 'yes':
                    SHEET.del_worksheet(user_scsht)
                    print(
                        f"\nThe sheet '{usrnm}' has been deleted"
                    )
                    return_to_main()
                elif choice == 'no':
                    clear()
                    main()
                else:
                    clear()
                    print(Fore.RED + Style.BRIGHT +
                        f"Invalid input: {choice}. Enter 'yes' or 'no'." + Style.RESET_ALL
                    )
                    continue
        except gspread.exceptions.WorksheetNotFound:
            while True:
                print(
                    f"\nA score sheet named '{usrnm}' does not exist.\n"
                )
                print("Do you want to:\n")
                print("1. Enter another username?\n")
                print("2. Return to the main menu?\n")
                print( Fore.GREEN + Style.BRIGHT +
                    "Enter the number of your choice:\n" + Style.RESET_ALL              
                )
                choice = input()
                if choice == '1':
                    clear()
                    delete_score_sheet()
                elif choice == '2':
                    clear()
                    main()
                else:
                    clear()
                    print(Fore.RED + Style.BRIGHT +
                        f"Invalid input: {choice}. Please enter 1 or 2." + Style.RESET_ALL
                    )
                    continue


def generate_random_paragraph(n):
    """
    Create a paragraph of random sentences using wonderwords.
    Adapted from:
    'https://towardsdatascience.com/speed-typing-test-project-with-python-da1a56987a5b'
    """
    sent_list = []
    sent_para = ""

    for i in range(n):
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
                Fore.GREEN + Style.BRIGHT + "Enter your username to see your scores and statistics:\n"
            )
            print(Style.RESET_ALL)
            usrnm = input().lower()
            user_scsht = SHEET.worksheet(usrnm)
            break
        except gspread.exceptions.WorksheetNotFound:
            while True:
                print(Fore.RED + Style.BRIGHT +
                    f"\nWorksheet for '{usrnm}' not found\n" + Style.RESET_ALL
                )
                print("Would you like to:\n")
                print("1. enter a different username or\n")
                print("2. return to the main menu?\n")
                print(Fore.GREEN + Style.BRIGHT +
                    "Please enter your numeric choice:\n" + Style.RESET_ALL
                )
                choice = input()
                if choice == '1':
 
                    see_old_scores_and_statistics()
                elif choice == '2':

                    main()
                else:
                    print(Fore.RED + Style.BRIGHT +
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
            Fore.RED + Style.BRIGHT + "A Syntax Error has occured and statistics can not be computed.\n"
        )
        print(Fore.RED + Style.BRIGHT + "The data file may be corrupted.\n")
        print(Style.RESET_ALL)

    return_to_main()

def create_user_score_sheet():
    """
    Create a google spread sheet to save scores for a new user
    """
    headings = ["speed in cpm", "speed in wpm", "accuracy", "level chosen"]
    print(Fore.GREEN + Style.BRIGHT +
        "Enter your username for a new score sheet:\n" + Style.RESET_ALL
    )
    usrnm = input().lower()
    while True:
        try:
            user_scsht = SHEET.worksheet(usrnm)
            print(
                f"\nA sheet with the name '{usrnm}' already exist.\n"
            )
            print("Do you want to:\n")
            print("1. Choose a differnt username?\n")
            print("2. Return to main menu and record data to existing sheet?\n")
            print(Fore.GREEN + Style.BRIGHT + "Enter your numeric choice:\n" Style.RESET_ALL)
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
            user_scsht = SHEET.add_worksheet(title=usrnm, rows=100, cols=20)
            user_scsht.append_row(headings)
            print( 
                f"\nScoresheet for '{usrnm}' has been created.\n" 
            )
            print("It can now be used to save scores of the test.\n")

            return_to_main()


def post_test_choice(data):
    """
    User gets a choice to save the data or return to the main menu
    """
    print(Fore.YELLOW + Style.BRIGHT + "\nWhat next?\n" + Style.RESET_ALL)
    print("1. Save results.\n")
    print("2. Return to main menu.\n")
    print(Fore.GREEN + Style.BRIGHT + "Please enter your numeric choice:\n" + Style.RESET_ALL)
    now_what = input()
    while True:
        try:
            if now_what == '1':
                save_score(data)
                return_to_main()
            elif now_what == '2':
                clear()
                main()
            else:
                raise ValueError
        except ValueError:
            print(Fore.RED + Style.BRIGHT +
                f"\nInvalid input {now_what}. Please enter 1 or 2.\n" + Style.RESET_ALL
            )

            post_test_choice(data)


def save_score(data):
    """
    Save score to worksheet that matches the username
    """
    while True:
        try:
            print(Fore.GREEN + Style.BRIGHT +
                "\nEnter your username to save the score:\n" + Style.RESET_ALL
            )
            usrnm = input().lower()
            user_scsht = SHEET.worksheet(usrnm)
            print(f"\nUpdating '{usrnm}' scoresheet ...\n")
            user_scsht = SHEET.worksheet(usrnm)
            user_scsht.append_row(data)
            print(
                f"'{usrnm}' scoresheet updated successfully.\n"
            )
            return_to_main()
        except gspread.exceptions.WorksheetNotFound:
            while True:
                print(Fore.RED + Style.BRIGHT +
                    f"\nWorksheet for '{usrnm}' not found\n" + Style.RESET_ALL
                )
                print("Would you like to:\n")
                print("1. input a different username?\n")
                print("2. create a worksheet to save your scores?\n")
                print("3. return to the main menu?\n")
                print(Fore.GREEN + Style.BRIGHT +
                    "Please enter your numeric choice:\n" + Style.RESET_ALL
                )
                choice = input()
                if choice == '1':
                    continue
                elif choice == '2':
                    headings = ["speed in cpm", "speed in wpm", "accuracy", "level chosen"]
                    user_scsht = SHEET.add_worksheet(title=usrnm, rows=50, cols=5)
                    user_scsht.append_row(headings)
                    user_scsht.append_row(data)
                    print(
                        f"\nScoresheet '{usrnm}' created and updated.\n"
                    )
                    return_to_main()
                elif choice == '3':
                    clear()
                    main()
                else:
                    print(Fore.RED + Style.BRIGHT +
                        f"\nInvalid input: {choice}. Enter 1, 2, or 3.\n" + Style.RESET_ALL
                    )
                    continue


def main():
    """
    Run all program functions
    """

    choice = print_menu()

    try:
        if choice == '1':
            clear()
            display_instructions()
        elif choice == '2':
            clear()
            tips()
        elif choice == '3':
            clear()
            create_user_score_sheet()
        elif choice == '4':
            test_scores = run_test_display_results()
            post_test_choice(test_scores)
        elif choice == '5':
            clear()
            see_old_scores_and_statistics()
        elif choice == '6':
            clear()
            delete_score_sheet()
        elif choice == '7':
            print(Fore.MAGENTA + Style.BRIGHT + "\nExiting the program.\n")
            print("Thanks for checking it out!\n")
            print("Come back soon!\n")
            print(Style.RESET_ALL)
            exit()  
        else:
            raise ValueError
    except ValueError:
        print(Fore.RED + Style.BRIGHT +
            f"\nInvalid input: {choice}")
        print(
            "Return to the main menu and enter a number from 1 to 7.\n")
        return_to_main()


main()


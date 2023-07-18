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




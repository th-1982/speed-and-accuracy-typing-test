"""This program runs a speed and accuracy typing test."""

import time
from os import system, name
from difflib import SequenceMatcher
from statistics import mean
from ast import literal_eval

import gspread
from google.oauth2.service_account import Credentials

from wonderwords import RandomSentance
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


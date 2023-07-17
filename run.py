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

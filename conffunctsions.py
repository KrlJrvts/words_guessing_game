# Python program to clear the screen using os.system
import os
from colorama import Fore, Back, Style, init

def clrscr():
    # Check if Operating System is Mac and Linux or Windows
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # Else Operating System is Windows (os.name = nt)
        _ = os.system('cls')



# Color templates


def Blue():
    Fore.BLUE()

def Winner():
    Fore.YELLOW

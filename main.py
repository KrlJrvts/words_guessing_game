# import required modules
from time import sleep
import colorama
from colorama import Fore, Back, Style, init
import os
from conffunctsions import clrscr, Blue, Winner

# initialize colorama
colorama.init(autoreset=True)

# Introduction text for game
print("________________________________________________________")
print(Blue() + "Welcome to words guessing game")
# sleep(1)

# clrscr()

print(Fore.BLUE + "MENU")
print(" 1 - Start a game")
print(" 2 - See a scoreboard")
print(" 3 - Exit game")
# print(Back.RED + "System cleared")

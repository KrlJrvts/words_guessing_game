# import required modules
from time import sleep
import colorama
# from conffunctsions import clrscr
from ui import Clrs

# initialize colorama
colorama.init(autoreset=True)

# Introduction text for game
print("________________________________________________________")
print(f"{Clrs.bggrn}Welcome to words guessing game")
sleep(1)

# clrscr()

print(f"{Clrs.bbl}MENU")
print(f"{Clrs.bgrn} 1 - Start a game")
print(f"{Clrs.bgrn} 2 - See a scoreboard")
print(f"{Clrs.bgrn} 3 - Exit game")


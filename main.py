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

while True:
    print(f"{Clrs.bbl}MENU")
    print(f"{Clrs.bgrn} 1 - Start a game")
    print(f"{Clrs.bgrn} 2 - See a scoreboard")
    print(f"{Clrs.brd} 3 - Exit game")
    player_option = input(f"{Clrs.bl2} Your answer: ")
    if player_option == "1":
        pass

    elif player_option == "2":
        while True:
            print(f"{Clrs.bbl}What game level of scoreboard You would like to see?")
            print(f"{Clrs.bgrn} 1 - Easy")
            print(f"{Clrs.bgrn} 2 - Medium")
            print(f"{Clrs.bgrn} 3 - Hard")
            print(f"{Clrs.brd} 4 - Exit Scoreboards")
            player_score = input(f"{Clrs.bl2} Your answer: ")
            if player_score == "1" or player_score == "2" or player_score == "3":
                pass

    elif player_option == "3":
        print()
        break

    else:
        print(f"{Clrs.brd} Please make a valid choice!")

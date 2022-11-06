# File to create standard colors pallets for game design.

from colorama import Fore, Back, Style
import colorama
colorama.init(autoreset=True)


class Fg:
    black = Fore.BLACK
    red = Fore.RED
    green = Fore.GREEN
    yellow = Fore.YELLOW
    blue1 = Fore.BLUE
    blue2 = Fore.LIGHTBLUE_EX


class Bg:
    black = Back.BLACK
    red = Back.RED
    green = Back.GREEN
    yellow = Back.YELLOW
    blue1 = Back.BLUE
    blue2 = Back.LIGHTBLUE_EX


class Stl:
    black = Style.BRIGHT
    red = Style.DIM
    green = Style.NORMAL

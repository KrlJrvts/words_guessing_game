# File to create standard colors pallets for game design.
from colorama import Fore, Style, Back


# Foreground color options
class Clrs:

    # Colors
    grn = Fore.GREEN
    rd = Fore.RED
    bl1 = Fore.BLUE
    bl2 = Fore.LIGHTBLUE_EX
    yllw = Fore.YELLOW
    mgnt = Fore.MAGENTA
    cyn = Fore.CYAN
    clr = Fore.RESET

    # Bright colors
    bgrn = Fore.GREEN + Style.BRIGHT
    brd = Fore.RED + Style.BRIGHT
    bbl = Fore.BLUE + Style.BRIGHT
    byllw = Fore.YELLOW + Style.BRIGHT
    bmgnt = Fore.MAGENTA + Style.BRIGHT
    bcyn = Fore.CYAN + Style.BRIGHT
    bclr = Fore.RESET + Style.RESET_ALL

    # Background colors
    bggrn = Back.GREEN
    bgrd = Back.RED
    bgwht = Back.WHITE


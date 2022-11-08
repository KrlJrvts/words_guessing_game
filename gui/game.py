import tkinter as tk
from design import Ft, Bg


def game():
    """Overall layout"""
    game = tk.Frame(
        bg=Bg.lgry
    )
    game.pack()
    """ Here will be game visual"""
    game_frame = tk.Frame(
        game,
        bg=Bg.grn
    )
    label_game = tk.Label(text="Here will be hangman game", font=Ft.h1)
    game_frame.pack()  # (row=1, column=0, sticky="W")
    """Here will be game inputs (alphabet buttons)"""
    letters_frame = tk.Frame(
        game,
        bg=Bg.lgrn
    )
    letters_frame.pack()  # grid(row=1, column=0, sticky="W")

    i = 0
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    button = []
    for j in range(2):
        for k in range(1, 13):
            button.append(tk.Button(letters_frame, width=4, height=1, font=Ft.text, bd=4, text=alphabet[i]))
            button[i].grid(row=j, column=k, padx=2, pady=2)
            i += 1



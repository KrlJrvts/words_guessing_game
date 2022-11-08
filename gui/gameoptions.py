import tkinter as tk
from design import Ft, Bg
from gui.game import game


def options():
    options_frame = tk.Frame(
        bg=Bg.lgry
    )
    # username label
    options_label = tk.Label(
        options_frame,
        text="Player name:",
        bg=Bg.lgry,
        font=Ft.h2
    )
    options_label.pack()

    # Username entry
    options_name = tk.Entry(
        options_frame,
        width=20,
        font=Ft.h2,
        justify="center"
    )
    options_name.get()
    options_name.pack()

    button1 = tk.Button(
        text="Play",
        font=Ft.h2,
        height=1,
        width=20,
        command=game
    )
    button1.pack()
    options_frame.pack()

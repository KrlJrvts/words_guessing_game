import tkinter as tk
import customtkinter as ctk
from design import Ft
from backend.dictionary import get_word

"""==================== game_frame layout, 3 frames on the top 
                        and one with letters at the bottom middle  ===================="""


def game(game_frame):

    # ==================== Middle frame====================

    game_middle = ctk.CTkFrame(
        master=game_frame,
        width=500,
        height=200
    )
    game_middle.place(
        relx=0.5,
        rely=0.35,
        anchor=ctk.CENTER
    )

    game_field = ctk.CTkLabel(
        master=game_middle,
        text=(10 * "_ "),  # need to figure out how to get word length from option_button()
        text_font=Ft.h1,
    )

    game_field.place(
        relx=0.5,
        rely=0.7,
        anchor=ctk.CENTER
    )

    # ==================== Left frame ====================

    game_left = ctk.CTkFrame(
        master=game_frame,
        width=150,
        height=325,
    )
    game_left.place(
        relx=0.125,
        rely=0.475,
        anchor=tk.CENTER

    )
    label_right = ctk.CTkLabel(
        master=game_left,
        text="Lives left:",
        text_font=Ft.h2,

    )
    label_right.place(
        relx=0.5,
        rely=0.1,
        anchor=tk.N
    )

    # ==================== Right frame ====================

    game_right = ctk.CTkFrame(
        master=game_frame,
        width=150,
        height=325,
    )
    game_right.place(
        relx=0.875,
        rely=0.475,
        anchor=tk.CENTER
    )
    label_right = ctk.CTkLabel(
        master=game_right,
        text="Letters you\n"
             "have guessed:",
        text_font=Ft.h2,
    )
    label_right.place(
        relx=0.5,
        rely=0.1,
        anchor=tk.N
    )
    entry_letters = ctk.CTkEntry(
        master=game_right,
        height=100,
        width=100
    )
    entry_letters.place(
        relx=0.5,
        rely=0.5,
        anchor=tk.N
    )
    # entry_letters.insert(button_click(args))

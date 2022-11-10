import tkinter as tk
import customtkinter as ctk
from design import Ft
from dictionary import get_word


def game(game_frame):

    """==================== Middle frame===================="""

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
        text="word",
        text_font=Ft.h1,
        # print()
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

import tkinter as tk
import customtkinter as ctk
from design import Ft
from main import option_button

from backend.dictionary import get_word


# def option_button(game_frame):
#     game_frame.tkraise()
#     get_word()
#     print(get_word())
#     length = len(get_word())
#     return length

# name_var = tk.StringVar()
#
#
# def names():
#     name = name_var.get()
#     return name


def options(option_frame):
    # Player name entry and words choosing

    option_lbl_1 = ctk.CTkLabel(
        master=option_frame,
        text="Hello traveler!\n"
             "Please insert your name on the text field\n"
             "and choose a category of word.",
        text_font=Ft.h1b
    )
    option_lbl_1.place(
        relx=0.5,
        rely=0.1,
        anchor=tk.CENTER
    )

    option_btn_1 = ctk.CTkButton(
        master=option_frame,
        text="GO",
        text_font=Ft.h2,
        width=300,
        height=40,
        command=lambda: option_button
    )
    option_btn_1.place(
        relx=0.5,
        rely=0.8,
        anchor=tk.CENTER
    )

    name_frame = ctk.CTkFrame(
        master=option_frame,
        width=500,
        height=200
    )
    name_frame.place(
        relx=0.5,
        rely=0.4,
        anchor=ctk.CENTER
    )

    name_label = ctk.CTkLabel(
        master=name_frame,
        text="What is Your name?",
        text_font=Ft.h1
    )
    name_label.place(
        relx=0.5,
        rely=0.2,
        anchor=ctk.CENTER
    )
    name_entry = ctk.CTkEntry(
        master=name_frame,
        width=300,
        height=50,

    )
    name_entry.place(
        relx=0.5,
        rely=0.7,
        anchor=ctk.CENTER
    )

import tkinter as tk
import customtkinter as ctk
from design import Ft

# name_var = tk.StringVar()
#
#
# def names():
#     name = name_var.get()
#     return name


def options(option_frame):

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

    )   # textvariable=name_var
    name_entry.place(
        relx=0.5,
        rely=0.7,
        anchor=ctk.CENTER
    )

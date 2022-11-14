import tkinter as tk
import customtkinter as ctk
from design import Ft


def score(score_frame):

    score_lbl_1 = ctk.CTkLabel(
        master=score_frame,
        text="This is the hall of fame for most dedicated players!\n"
             "Did you find your name in here?",
        text_font=Ft.h1b
    )
    score_lbl_1.place(
        relx=0.5,
        rely=0.1,
        anchor=tk.CENTER
    )

    """==================== Fruits Category ==================== """
    fruit_frame = ctk.CTkFrame(
        master=score_frame,
        width=200,
        height=300
    )
    fruit_frame.place(
        relx=0.125,
        rely=0.2,
        anchor=tk.N
    )
    fruit_label = ctk.CTkLabel(
        master=fruit_frame,
        text="Top health gurus:"
    )
    fruit_label.place(
        relx=0.5,
        rely=0.1,
        anchor=tk.N
    )

    """==================== Animals Category ==================== """
    animal_frame = ctk.CTkFrame(
        master=score_frame,
        width=200,
        height=300
    )
    animal_frame.place(
        relx=0.375,
        rely=0.2,
        anchor=tk.N
    )
    animal_label = ctk.CTkLabel(
        master=animal_frame,
        text="Top zookeepers:"
    )
    animal_label.place(
        relx=0.5,
        rely=0.1,
        anchor=tk.N
    )

    """ ==================== Accessories Category ===================="""
    cloth_frame = ctk.CTkFrame(
        master=score_frame,
        width=200,
        height=300
    )
    cloth_frame.place(
        relx=0.625,
        rely=0.2,
        anchor=tk.N
    )
    cloth_label = ctk.CTkLabel(
        master=cloth_frame,
        text="The fashionistas:"
    )
    cloth_label.place(
        relx=0.5,
        rely=0.1,
        anchor=tk.N
    )

    """ ==================== Office Category ===================="""
    office_frame = ctk.CTkFrame(
        master=score_frame,
        width=200,
        height=300
    )
    office_frame.place(
        relx=0.875,
        rely=0.2,
        anchor=tk.N
    )
    office_label = ctk.CTkLabel(
        master=office_frame,
        text="Top workaholics:"
    )
    office_label.place(
        relx=0.5,
        rely=0.1,
        anchor=tk.N
    )

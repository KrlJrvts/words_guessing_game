# modules to build GUI
import tkinter as tk
import customtkinter as ctk

# support files
from design import Ft
from alphabet import alphabet

# game backend
from backend.dictionary import get_word


def raise_frame(frame):
    frame.tkraise()


def option_button(game_frame):
    raise_frame(game_frame)
    word = get_word()
    print(word)  # print to check word - temp.
    num = int(len(word))
    print(num)   # print to check word == len - temp.
    return num


def main():
    """ CustomTkinter initializing """
    ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

    """ root """
    root = tk.Tk()
    root.title("Words Guessing Game")
    root.geometry("900x500")
    root.minsize(width=900, height=500)
    root.maxsize(width=900, height=500)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    """ definition of frames used in game"""
    main_frame = ctk.CTkFrame(root)
    option_frame = ctk.CTkFrame(root)
    game_frame = ctk.CTkFrame(root)
    score_frame = ctk.CTkFrame(root)

    """ for loop do define frames"""
    for frame in (main_frame, option_frame, game_frame, score_frame):
        frame.grid(row=0, column=0, sticky="nsew")

    raise_frame(main_frame)

    """====================  Main_frame  ===================="""

    main_lbl = ctk.CTkLabel(
        master=main_frame,
        text="Welcome to the word guessing game! \n "
             "Please choose from options below",
        text_font=Ft.h1b
    )
    main_lbl.place(
        relx=0.5,
        rely=0.1,
        anchor=tk.CENTER
    )

    # Buttons - New Game, Scoreboard, Exit game
    main_btn_1 = ctk.CTkButton(
        master=main_frame,
        text="New game",
        text_font=Ft.h2,
        width=300,
        height=40,
        command=lambda: raise_frame(option_frame)
    )
    main_btn_1.place(
        relx=0.5,
        rely=0.4,
        anchor=tk.CENTER
    )

    main_btn_2 = ctk.CTkButton(
        master=main_frame,
        text="Scoreboard",
        text_font=Ft.h2,
        width=300,
        height=40,
        command=lambda: raise_frame(score_frame)
    )
    main_btn_2.place(
        relx=0.5,
        rely=0.5,
        anchor=tk.CENTER
    )

    main_btn_3 = ctk.CTkButton(
        master=main_frame,
        text="Exit game",
        text_font=Ft.h2,
        width=300,
        height=40,
        command=root.destroy
    )
    main_btn_3.place(
        relx=0.5,
        rely=0.6,
        anchor=tk.CENTER
    )

    """====================  Options_frame  ===================="""

    option_btn_2 = ctk.CTkButton(
        master=option_frame,
        text="Return to main menu",
        text_font=Ft.h2,
        width=300,
        height=40,
        command=lambda: raise_frame(main_frame)
    )
    option_btn_2.place(
        relx=0.5,
        rely=0.9,
        anchor=tk.CENTER
    )

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
        command=lambda: option_button(game_frame)
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

    """====================  Game_frame ===================="""

    game_btn_1 = ctk.CTkButton(
        master=game_frame,
        text="Return to main menu",
        text_font=Ft.h2,
        width=300,
        height=40,
        command=lambda: raise_frame(main_frame)
    )
    game_btn_1.place(
        relx=0.5,
        rely=0.9,
        anchor=tk.CENTER
    )

    # Actual letters visual frame
    game_lbl_1 = ctk.CTkLabel(
        master=game_frame,
        text=f"Good luck!",  # need to fix how to put name in here!
        text_font=Ft.h1b
    )
    game_lbl_1.place(
        relx=0.5,
        rely=0.1,
        anchor=tk.CENTER
    )

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
        text=(num * "_ "),  # need to figure out how to get word length from option_button()
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
    alphabet(game_frame)

    """====================  Scoreboard_frame  ===================="""

    score_btn_1 = ctk.CTkButton(
        master=score_frame,
        text_font=Ft.h2,
        text="Return to main menu",
        width=300,
        height=40,
        command=lambda: raise_frame(main_frame)
    )
    score_btn_1.place(
        relx=0.5,
        rely=0.9,
        anchor=tk.CENTER
    )

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

    root.mainloop()


if __name__ == "__main__":
    main()

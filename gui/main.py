# modules to build GUI
import tkinter as tk
import customtkinter as ctk
from design import Ft

# Files to bring GUI together
from scoreboard import score
from game import game
from options import options
from alphabet import alphabet

# Backend files to make game function
# from backend.game import game_engine
from backend.dictionary import get_word


def raise_frame(frame):
    frame.tkraise()


def option_button():
    raise_frame(game_frame)
    get_word()
    print(get_word())
    length = len(get_word())
    return length


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
# Game greeting message and first step introduction

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
    command=lambda: option_button(),

)
option_btn_1.place(
    relx=0.5,
    rely=0.8,
    anchor=tk.CENTER
)

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

options(option_frame)


"""====================  Game_frame ===================="""

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

# Alphabet for the game
alphabet(game_frame)

# Actual letters visual frame
game(game_frame)


"""====================  Scoreboard_frame  ===================="""

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

score(score_frame)

root.mainloop()

import tkinter as tk
# from scoreboard import score
from design import Ft, Bg


# Score table view
def score():
    score_frame = tk.Frame(root)
    score_label = tk.Label(
        score_frame,
        text="This is scoreboard",
        background=Bg.grn
    )
    score_label.pack()
    score_frame.pack()


# Player name input and game style menu
def options():
    options_frame = tk.Frame(
        root,
        bg=Bg.lgry
    )
    # username label
    options_label = tk.Label(
        options_frame,
        text="Username",
        bg=Bg.lgry,
        font=Ft.h2
    )
    options_label.pack()

    # Username entry
    options_name = tk.Entry(
        options_frame,
        width=20,
        font=Ft.h2,

    )
    options_name.pack()
    options_name.get()
    options_frame.pack()


"""_________________________ Main GUI _________________________________"""

root = tk.Tk()
root.title("Words guessing game")
root.configure(
    bg=Bg.lgry
)
root.geometry("900x500")

# root label

label = tk.Label(
    text="Welcome to the word guessing game! \n "
         "Please choose from options below",
    bg=Bg.lgry,
    font=Ft.h1,
    pady=40,
    width=50
)
label.pack()

# root buttons
button1 = tk.Button(
    root,
    text="New Game",
    font=Ft.h2,
    height=1,
    width=20,
    command=options
)
button1.pack()

button2 = tk.Button(
    root,
    text="Scoreboard",
    font=Ft.h2,
    height=1,
    width=20,
    command=score
)
button2.pack()

button3 = tk.Button(
    root,
    text="Exit game",
    font=Ft.h2,
    height=1,
    width=20,
    command=root.destroy
)
button3.pack()

root.mainloop()

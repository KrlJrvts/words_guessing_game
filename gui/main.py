import tkinter as tk
from scoreboard import score
from gameoptions import options
from design import Ft, Bg


"""_________________________ Main GUI _________________________________"""

root = tk.Tk()
root.title("Words guessing game")
root.configure(
    bg=Bg.lgry
)
root.geometry("1080x500")

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

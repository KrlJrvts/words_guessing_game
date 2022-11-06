from tkinter import *

# Window dimensions
window = Tk()
window.title("Words guessing game")
window.geometry("900x500")
window.configure(bd=5, background="green")

# Buttons for main menu
button1 = Button(window, text="New game", fg="black")
button1.config(height=1, width=20)
button1.place(x=350, y=100)
button2 = Button(window, text="Scoreboard", fg="black")
button2.config(height=1, width=20)
button2.place(x=350, y=150)
button3 = Button(window, text="Exit game", fg="black")
button3.config(height=1, width=20)
button3.place(x=350, y=200)


window.mainloop()

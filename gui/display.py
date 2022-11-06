from tkinter import *

# Window dimensions
window = Tk()
window.title("Words guessing game")
window.geometry("900x500")
window.configure(bd=20, background="green")

# Main label
label1 = Label(window, text="Welcome to the word guessing game!", font=("Helvetica", 16))
label1.config(height=1, width=50)
label1.place(x=150, y=10)
label2 = Label(window, text="Please choose from options below", font=("Helvetica", 16))
label2.config(height=1, width=50)
label2.place(x=150, y=40)


# Buttons for main menu
button1 = Button(window, text="New game", fg="black", font="Helvetica")
button1.config(height=1, width=20)
button1.place(x=350, y=200)
button2 = Button(window, text="Scoreboard", fg="black", font="Helvetica")
button2.config(height=1, width=20)
button2.place(x=350, y=250)
button3 = Button(window, text="Exit game", fg="black", font="Helvetica")
button3.config(height=1, width=20)
button3.place(x=350, y=300)

window.mainloop()

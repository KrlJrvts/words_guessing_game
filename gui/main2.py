import tkinter as tk
# from tkinter.messagebox import showinfo
# from tkinter.messagebox import showwarning

from gui.scoreboard import Score
from gui.gameoptions import Options


class Root(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        root = tk.Frame(self)

        root.pack(side="top", fill="both", expand=True)

        # Root configuration
        root.title("Words guessing game")
        root.geometry("900x500")
        self.configure(background="light gray")

        # Label
        self.label = tk.Label(self,
                              text="Welcome to the word guessing game! \n "
                                   "Please choose from options below",
                              background="light gray",
                              font=("Helvetica", 16),
                              height=5,
                              width=50)
        self.label.place(x=150, y=10)

        # Buttons
        self.button1 = tk.Button(self,
                                 text="New game",
                                 fg="black",
                                 font="Helvetica",
                                 height=1,
                                 width=20,
                                 command=Options)
        self.button1.place(x=350, y=200)
        self.button2 = tk.Button(self,
                                 text="Scoreboard",
                                 fg="black",
                                 font="Helvetica",
                                 height=1,
                                 width=20,
                                 command=Score)
        self.button2.place(x=350, y=250)
        self.button3 = tk.Button(self,
                                 text="Exit game",
                                 fg="black",
                                 font="Helvetica",
                                 height=1,
                                 width=20,
                                 command=self.destroy)
        self.button3.place(x=350, y=300)



root = Root()
root.mainloop()

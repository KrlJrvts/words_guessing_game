import tkinter as tk


class Options(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(fill="both")
        container.label = tk.Label(text="This is a game option window! \n"
                                        "Insert your name \n"
                                        "Please choose words category \n",
                                   background="light gray",
                                   font=("Helvetica", 16),
                                   height=5,
                                   width=50)

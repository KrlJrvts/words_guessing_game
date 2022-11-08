import tkinter as tk


class Game:
    def __init__(self):
        super(Game, self).__init__()
        self.label = tk.Label(root,
                              text="This is a game window! \n",
                              background="light gray",
                              font=("Helvetica", 16),
                              height=5,
                              width=50)

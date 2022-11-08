import tkinter as tk
from design import Ft, Bg


def score():
    score_frame = tk.Frame()
    score_label = tk.Label(
        score_frame,
        text="This is scoreboard",
        font=Ft.h2,
        background=Bg.grn
    )
    score_label.pack()
    score_frame.pack()
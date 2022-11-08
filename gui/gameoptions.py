import tkinter as tk
from design import Ft, Bg

def options():
    options_frame = tk.Frame(
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

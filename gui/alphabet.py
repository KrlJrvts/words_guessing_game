import tkinter as tk
import customtkinter as ctk

# Function to call button clicks to the game engine


def button_click(args):
    if args == "a":
        print("a")
        return "a"
    if args == "b":
        return "b"
    if args == "c":
        return "c"
    if args == "d":
        return "d"
    if args == "e":
        return "e"
    if args == "f":
        return "f"
    if args == "g":
        return "g"
    if args == "h":
        return "h"
    if args == "i":
        return "i"
    if args == "j":
        return "j"
    if args == "k":
        return "k"
    if args == "l":
        return "l"
    if args == "m":
        return "m"
    if args == "n":
        return "n"
    if args == "o":
        return "o"
    if args == "p":
        return "p"
    if args == "q":
        return "q"
    if args == "r":
        return "r"
    if args == "s":
        return "s"
    if args == "t":
        return "t"
    if args == "u":
        return "u"
    if args == "v":
        return "v"
    if args == "w":
        return "w"
    if args == "y":
        return "y"
    if args == "x":
        return "x"
    if args == "z":
        return "z"


def alphabet(game_frame):
    abc = ctk.CTkFrame(
        master=game_frame,
        width=500,
        height=100,
    )
    abc.place(
        relx=0.5,
        rely=0.7,
        anchor=tk.CENTER
    )

    btn_a = ctk.CTkButton(abc, text="A", width=30, height=30, border_width=2, command=lambda: button_click("a"))
    btn_b = ctk.CTkButton(abc, text="B", width=30, height=30, border_width=2, command=lambda: button_click("b"))
    btn_c = ctk.CTkButton(abc, text="C", width=30, height=30, border_width=2, command=lambda: button_click("c"))
    btn_d = ctk.CTkButton(abc, text="D", width=30, height=30, border_width=2, command=lambda: button_click("d"))
    btn_e = ctk.CTkButton(abc, text="E", width=30, height=30, border_width=2, command=lambda: button_click("e"))
    btn_f = ctk.CTkButton(abc, text="F", width=30, height=30, border_width=2, command=lambda: button_click("f"))
    btn_g = ctk.CTkButton(abc, text="G", width=30, height=30, border_width=2, command=lambda: button_click("g"))
    btn_h = ctk.CTkButton(abc, text="H", width=30, height=30, border_width=2, command=lambda: button_click("h"))
    btn_i = ctk.CTkButton(abc, text="I", width=30, height=30, border_width=2, command=lambda: button_click("i"))
    btn_j = ctk.CTkButton(abc, text="J", width=30, height=30, border_width=2, command=lambda: button_click("j"))
    btn_k = ctk.CTkButton(abc, text="K", width=30, height=30, border_width=2, command=lambda: button_click("k"))
    btn_l = ctk.CTkButton(abc, text="L", width=30, height=30, border_width=2, command=lambda: button_click("l"))
    btn_m = ctk.CTkButton(abc, text="M", width=30, height=30, border_width=2, command=lambda: button_click("m"))
    btn_n = ctk.CTkButton(abc, text="N", width=30, height=30, border_width=2, command=lambda: button_click("n"))
    btn_o = ctk.CTkButton(abc, text="O", width=30, height=30, border_width=2, command=lambda: button_click("o"))
    btn_p = ctk.CTkButton(abc, text="P", width=30, height=30, border_width=2, command=lambda: button_click("p"))
    btn_q = ctk.CTkButton(abc, text="Q", width=30, height=30, border_width=2, command=lambda: button_click("q"))
    btn_r = ctk.CTkButton(abc, text="R", width=30, height=30, border_width=2, command=lambda: button_click("r"))
    btn_s = ctk.CTkButton(abc, text="S", width=30, height=30, border_width=2, command=lambda: button_click("s"))
    btn_t = ctk.CTkButton(abc, text="T", width=30, height=30, border_width=2, command=lambda: button_click("t"))
    btn_u = ctk.CTkButton(abc, text="U", width=30, height=30, border_width=2, command=lambda: button_click("u"))
    btn_v = ctk.CTkButton(abc, text="V", width=30, height=30, border_width=2, command=lambda: button_click("v"))
    btn_w = ctk.CTkButton(abc, text="W", width=30, height=30, border_width=2, command=lambda: button_click("w"))
    btn_x = ctk.CTkButton(abc, text="X", width=30, height=30, border_width=2, command=lambda: button_click("x"))
    btn_y = ctk.CTkButton(abc, text="Y", width=30, height=30, border_width=2, command=lambda: button_click("y"))
    btn_z = ctk.CTkButton(abc, text="Z", width=30, height=30, border_width=2, command=lambda: button_click("z"))

    # Buttons grid

    btn_a.place(relx=0.0714, rely=0.30, anchor=tk.CENTER)
    btn_b.place(relx=0.1428, rely=0.30, anchor=tk.CENTER)
    btn_c.place(relx=0.2142, rely=0.30, anchor=tk.CENTER)
    btn_d.place(relx=0.2856, rely=0.30, anchor=tk.CENTER)
    btn_e.place(relx=0.3570, rely=0.30, anchor=tk.CENTER)
    btn_f.place(relx=0.4284, rely=0.30, anchor=tk.CENTER)
    btn_g.place(relx=0.4998, rely=0.30, anchor=tk.CENTER)
    btn_h.place(relx=0.5712, rely=0.30, anchor=tk.CENTER)
    btn_i.place(relx=0.6426, rely=0.30, anchor=tk.CENTER)
    btn_j.place(relx=0.7140, rely=0.30, anchor=tk.CENTER)
    btn_k.place(relx=0.7854, rely=0.30, anchor=tk.CENTER)
    btn_l.place(relx=0.8586, rely=0.30, anchor=tk.CENTER)
    btn_m.place(relx=0.9282, rely=0.30, anchor=tk.CENTER)
    btn_n.place(relx=0.0714, rely=0.70, anchor=tk.CENTER)
    btn_o.place(relx=0.1428, rely=0.70, anchor=tk.CENTER)
    btn_p.place(relx=0.2142, rely=0.70, anchor=tk.CENTER)
    btn_q.place(relx=0.2856, rely=0.70, anchor=tk.CENTER)
    btn_r.place(relx=0.3570, rely=0.70, anchor=tk.CENTER)
    btn_s.place(relx=0.4284, rely=0.70, anchor=tk.CENTER)
    btn_t.place(relx=0.4998, rely=0.70, anchor=tk.CENTER)
    btn_u.place(relx=0.5712, rely=0.70, anchor=tk.CENTER)
    btn_v.place(relx=0.6426, rely=0.70, anchor=tk.CENTER)
    btn_w.place(relx=0.7140, rely=0.70, anchor=tk.CENTER)
    btn_x.place(relx=0.7854, rely=0.70, anchor=tk.CENTER)
    btn_y.place(relx=0.8586, rely=0.70, anchor=tk.CENTER)
    btn_z.place(relx=0.9282, rely=0.70, anchor=tk.CENTER)

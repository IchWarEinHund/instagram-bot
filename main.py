from tkinter import Tk, ttk
import tkinter as tk

from following_by_users_followers import Example as TabA
from following_by_location import Example as TabB
from following_by_tag import Example as TabC
from following_by_users_following import Example as TabD
from likes_by_feed import  Example as TabE
from likes_by_location import  Example as TabS
from likes_by_tag import  Example as TabW


class MainInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('version')
        self.window.geometry("524x368")
        self.create_widgets()

    def create_widgets(self):
        self.window['padx'] = 10
        self.window['pady'] = 10

        self.notebook = ttk.Notebook(self.window, width=500, height=300)

        a_tab = TabA(self.notebook)
        b_tab = TabB(self.notebook)
        c_tab = TabC(self.notebook)
        d_tab = TabD(self.notebook)
        e_tab = TabE(self.notebook)
        s_tab = TabS(self.notebook)
        w_tab = TabW(self.notebook)

        self.notebook.add(a_tab, text="f1")
        self.notebook.add(d_tab, text="f2")
        self.notebook.add(b_tab, text="f3")
        self.notebook.add(c_tab, text="f4")
        self.notebook.add(e_tab, text="l1")
        self.notebook.add(s_tab, text="l2")
        self.notebook.add(w_tab, text="l3")

        self.notebook.grid(row=1, column=1)


if __name__ == '__main__':
    program = MainInterface()
    program.window.mainloop()

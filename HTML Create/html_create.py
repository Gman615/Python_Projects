import webbrowser
from webbrowser import *
from tkinter import *
import tkinter as tk
from tkinter import messagebox

import html_create_gui
import html_create_func1


# creates class for window frame
class ParentWindow(Frame):
    def __init__(self, master, *args,**kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        #creates window frame size and info
        self.master = master
        self.master.minsize(500,200)
        self.master.maxsize(500,200)
        self.master.title("Make your own webtext")
        self.master.configure(bg="indigo")
        self.master.protocol("WM_DELETE_WINDOW", lambda: html_create_func1.ask_quit(self))
        arg = self.master
        #loads gui
        html_create_gui.load_gui(self)
        




# program flow
if __name__ == "__main__":
    root= tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

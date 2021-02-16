import shutil
import os, sys, time
import datetime
from tkinter import *
import tkinter as tk
from tkinter import messagebox


import file_manager_gui
import file_manager_func


        
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        self.master.minsize(500,200)
        self.master.maxsize(700,400)
        self.master.title("File Manager")
        self.master.configure(bg="indigo")
        self.master.protocol("WM_DELETE_WINDOW", lambda: file_manager_func.ask_quit(self))
        arg = self.master

        file_manager_gui.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()







       







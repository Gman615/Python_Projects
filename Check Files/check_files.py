from tkinter import *
import tkinter as tk
from tkinter import messagebox


import check_files_gui_with_text
import check_files_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        self.master.minsize(500,150)
        self.master.maxsize(500,150)
        check_files_func.center_window(self,500,150)
        self.master.title("Check files")
        self.master.configure(bg="lightgrey")
        self.master.protocol("WM_DELETE_WINDOW", lambda: check_files_func.ask_quit(self))
        arg = self.master

        check_files_gui_with_text.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
        
        
        



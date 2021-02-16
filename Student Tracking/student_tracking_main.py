
from tkinter import *
import tkinter as tk
from tkinter import messagebox


# importing other modules
import student_tracking_gui
import student_tracking_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)

        student_tracking_func.center_window(self,500,300)
        self.master.title("Student Tracking")
        self.master.configure(bg='lightblue')

        self.master.protocol("WM_DELETE_WINDOW", lambda: student_tracking_func.ask_quit(self))
        arg = self.master

        student_tracking_gui.load_gui(self)



if __name__ == "__main__":
    root= tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

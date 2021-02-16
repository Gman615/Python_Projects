import shutil, sys, time, os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk


import check_files
import check_files_gui_with_text


def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get users screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes the app
        self.master.destroy()
        os._exit(0)

def file_search(self):
    file_path = filedialog.askdirectory()
    self.txt_path1.insert(END, file_path)


    

if __name__ == "__main__":
    pass


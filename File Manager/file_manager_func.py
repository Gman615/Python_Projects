import shutil
import os, sys, time
import datetime
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import file_manager
import file_manager_gui



def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes the app
        self.master.destroy()
        os._exit(0)

def file_search(self):
    global file_path # makes file path a global variable to use elsewhere
    file_path = filedialog.askdirectory()
    self.txt_path1.insert(END, file_path)
    

def file_search1(self):
    global file_path1 # makes file path a global variable to use elsewhere
    file_path1 = filedialog.askdirectory()
    self.txt_path2.insert(END, file_path1)
    

def file_move(self):
    source = file_path # stores selected fp in source
    destination = file_path1 # store selected fp in source
    dirs = os.listdir(source)
    for files in dirs:   # finds the current time, subtracts 24 hrs (in secs) and creates a veriable for a time period 24 hrs in the past    
        time_now = time.time()
        time_yest = time_now - 86400
        if files.endswith(''): # iterates through files to find a time as well as join file path
            abPath = os.path.join(source, files)
            get_time = os.path.getmtime(abPath)
            if time_yest < get_time:
                shutil.copy(abPath, destination) # copies files to destination folder with joined fp

if __name__ == "__main__":
    pass






import shutil, sys, time, os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk

import check_files
import check_files_func



    
def load_gui(self):

    self.btn_add = tk.Button(self.master,width=12,height=1,text='Browse',command=lambda: check_files_func.file_search(self))
    self.btn_add.grid(row=1,column=0,padx=(25,0),pady=(20,10),sticky=W)
    self.btn_add = tk.Button(self.master,width=12,height=2,text='Check for files...')
    self.btn_add.grid(row=3,column=0,padx=(25,0),pady=(10,0),sticky=W)
    self.btn_add = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: check_files_func.ask_quit(self))
    self.btn_add.grid(row=3,column=1,padx=(235,0),pady=(10,0),sticky=W)

    self.txt_path1 = tk.Text(self.master,width=41,height=1)
    self.txt_path1.grid(row=1,column=1,padx=(25,0),pady=(20,10),sticky=W)
    



if __name__ == "__main__":
    pass

    

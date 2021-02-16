import webbrowser
from webbrowser import *
from tkinter import *
import tkinter as tk
from tkinter import messagebox

import html_create
import html_create_func1


# function for loading gui
def load_gui(self):
    # label for text box
    self.lbl = tk.Label(self.master,text='Enter Text:')
    self.lbl.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=W)
    # entry field for user input
    self.entry = tk.Text(self.master,width=40,height=5)
    self.entry.grid(row=0,column=1,columnspan=2,padx=(25,0),pady=(20,10),sticky=W)
    # button that creates the new page
    self.btn = tk.Button(self.master,width=20,height=2,text='Create new page',command=lambda: html_create_func1.file_create(self))
    self.btn.grid(row=2,column=2,padx=(25,0),pady=(10,10),sticky=W)
                    
if __name__ == "__main__":
    pass

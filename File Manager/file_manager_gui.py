import shutil
import os, sys, time
from tkinter import *
import tkinter as tk

import file_manager_func
import file_manager


def load_gui(self):

    self.btn_add = tk.Button(self.master,width=12,height=1,text='Source File',command=lambda: file_manager_func.file_search(self))
    self.btn_add.grid(row=1,column=0,padx=(25,0),pady=(20,10),sticky=W)
    self.btn_add = tk.Button(self.master,width=12,height=1,text='File Transfer To',command=lambda: file_manager_func.file_search1(self))
    self.btn_add.grid(row=2,column=0,padx=(25,0),pady=(20,10),sticky=W)
    self.btn_add = tk.Button(self.master,width=12,height=2,text='Move',command=lambda: file_manager_func.file_move(self))
    self.btn_add.grid(row=3,column=0,padx=(25,0),pady=(10,0),sticky=W)
    self.btn_add = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: file_manager_func.ask_quit(self))
    self.btn_add.grid(row=3,column=1,padx=(235,0),pady=(10,0),sticky=W)

    self.txt_path1 = tk.Text(self.master,width=41,height=1)
    self.txt_path1.grid(row=1,column=1,padx=(25,0),pady=(20,10),sticky=W)
    self.txt_path2 = tk.Text(self.master,width=41,height=1)
    self.txt_path2.grid(row=2,column=1,padx=(25,0),pady=(20,10),sticky=W)


if __name__ == "__main__":
    pass

import os
import webbrowser
from webbrowser import *
from tkinter import *
import tkinter as tk
from tkinter import messagebox

import html_create_gui
import html_create

uinput = 

def file_create(self):
    f = open("simHTML1.html", "w")
    f.write("""<html>
        <body>
            <h1>
                Stay tuned for our amazing summer sale!
            </h1>
        </body>
    </html>""")
    f.close()
    f = open("simHTML1.html", "w")
    txt = f.replace("Stay tuned for our amazing summer sale", 
    webbrowser.open_new_tab("simHTML1.html")


# Catch if the user clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes the app
        self.master.destroy()
        os._exit(0)

if __name__ == "__main__":
    pass
    

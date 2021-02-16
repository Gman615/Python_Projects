import os
import webbrowser
from tkinter import *
import tkinter as tk
from tkinter import messagebox

import html_create
import html_create_gui



def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes the app
        self.master.destroy()
        os._exit(0)


# function for creating a new document if it does not exist,
# as well as altering the one that does exist
def file_create(self):
    uinput = self.entry.get("1.0",END) # takes user input and 
    f = open("simHTML1.html", "w")
    f.write("""<html>
    <body><h1>Stay tuned for our amazing summer sale!</h1>
    </body></html>""")
    f.close()

    f = open("simHTML1.html", "w")
    f.write("""<html>
    <body><h1>{}<h1></body></html>""".format(uinput)) # formats input string and puts in document
    f.close()           
    webbrowser.open_new_tab("simHTML1.html") # opens web page in a new tab
    


        
if __name__ == "__main__":
    pass

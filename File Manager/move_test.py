import shutil
import os, sys, time
import datetime
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

source = 'C:/Users/gma61/Desktop/NewlyModified/'

destination = 'C:/Users/gma61/Desktop/ProcessedFiles/'

dirs = os.listdir(source)
time_now = time.time()
time_yest = time_now - 86400


for files in dirs:
        if files.endswith(''):
            abPath = os.path.join(source, files)
            get_time = os.path.getmtime(abPath)
            if time_yest < get_time:
                shutil.move(source+files, destination)

from os import scandir
from tkinter import filedialog as fd
from tkinter import *

import os
import tkinter
import os

currdir = os.getcwd()

# Main function, remove spaces
def space_remover():
    source_dir = fd.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    with scandir(source_dir) as entries:
        for entry in entries:
            name = entry.name
            new_name = entry.name.replace(" ", "")
            os.rename(os.path.join(source_dir, name), os.path.join(source_dir, new_name))   # Directory navigator

root = tkinter.Tk()
root.geometry("600x200")
root.title("Space Remover")
root.resizable(False, False)

Label(root, text="Click the button below to \nremove spaces from whatever folder you wish!", font=('Ariel', 16)).pack()

rmv_btn = Button(root, text="Remove Spaces!", command=space_remover).pack()

root.update()

root.mainloop()


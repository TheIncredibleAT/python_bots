from os import scandir
from tkinter import filedialog as fd
from tkinter import *

import os
import tkinter
import os
currdir = os.getcwd()
""" def get_dir():
    source_dir = fd.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    os.chdir(source_dir)
    box1.config(state=NORMAL)
    box1.delete(0, END)
    box1.insert(0, source_dir)
    box1.config(state=DISABLED)

    return source_dir """


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
# Entry box to display selected directory
""" pwd = StringVar(root, value=currdir)
box1 = Entry(root, textvariable=pwd, font=('Ariel', 16))
box1.config(state=DISABLED)
box1.pack()

dir_select = Button(root, text="Select Folder", command=get_dir).pack(padx=20, pady=20) """

rmv_btn = Button(root, text="Remove Spaces!", command=space_remover).pack()

root.update()

root.mainloop()


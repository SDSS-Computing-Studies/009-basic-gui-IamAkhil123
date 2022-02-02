#!python3

import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("tk")
window.geometry("400x40")

label = tk.Label(window, text="x")
label.pack()

label2 = tk.Label(window, text="=")
label2.pack()

label2.place(x=21,y=45)
label.place(x=23,y=50)

window.mainloop()

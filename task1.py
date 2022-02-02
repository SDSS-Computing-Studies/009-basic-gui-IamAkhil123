#!python3
import tkinter as tk 
from tkinter import *
import tkinter as ttk


window = tk.Tk()
window.title("Hi!")
window.geometry("300x50")
L1 = Label(window, text="=")
L1.pack( side = LEFT)
E1 = Entry(window, bd =1)
E1.pack(side = RIGHT)
E1 = Entry(window, bd =1)
E1.pack(side = LEFT)
E1 = Entry(window, bd =1)
E1.pack(side = bottom)


window.mainloop()

label = ttk.Label(window, text = "x")
label.grid(column = 0, row = 0)
name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 15, textvariable = name)
nameEntered.grid(column = 0, row = 1)

text_box = Text(
    height=12,
    width=40
)
text_box.pack()
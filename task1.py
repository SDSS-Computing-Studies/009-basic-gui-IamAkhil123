#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk


"""
window = tk.Tk()
window.title("Hi!")
window.geometry("300x50")
L1 = Label(window, text="=")
L1.pack( center(side))
E1 = Entry(window, bd =1)
E1.pack(side = RIGHT)
E1 = Entry(window, bd =1)
E1.pack(side = LEFT)



window.mainloop()
"""



window = tk.Tk()
window.title("Packing Widgets example")

window.resizable(False,False)

label1 = tk.Label(window,text="x")

dogphoto = PhotoImage(file="dog.png")
label2 = tk.Label(window, image=dogphoto, borderwidth=3, relief=SUNKEN)

lable3 = tk.Label(window, text="Note that an image can be in a label or a button!", borderwidth=4, relief=SUNKEN)

button1 = tk.Button(window,text="A button\nis clickable")

entry1 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)

combo = ttk.Combobox(window,values=["1","2","3"])

label1.grid(row = 1, column = 1)
label2.grid(row = 1, column = 2, rowspan = 2)
lable3.grid(row = 2, column = 1)

entry1.grid(row=3, column = 1, columnspan=2)

window.mainloop()
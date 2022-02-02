#!python3

from tkinter import Text, Tk
import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("tk")
window.geometry("400x40")
label = tk.Label(window, text="x")
label.pack()
label2 = tk.Label(window, text="=")
label2.pack()
label2.place(x=165,y=6)
label.place(x=70,y=6)
t = Text(window, height=1, width=5)
t.place(x=10,y=6)
t = Text(window, height=1, width=5)
t.place(x=100,y=6)
t = Text(window, height=1, width=20)
t.place(x=200,y=6)
window.mainloop()




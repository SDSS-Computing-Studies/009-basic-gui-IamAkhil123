#!python3

from tkinter import Text, Tk
import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("tk")
window.geometry("400x200")

label = tk.Label(window, text="Client database")
label.pack()
label2 = tk.Label(window, text="Search by Name")
label2.pack()
label3 = tk.Label(window, text="Name")
label3.pack()
label4 = tk.Label(window, text="Type")
label4.pack()
label5 = tk.Label(window, text="Breed")
label5.pack()
label6 = tk.Label(window, text="Owner")
label6.pack()
label7 = tk.Label(window, text="Birthdate")
label7.pack()
label8 = tk.Label(window, text="< Previous")
label8.pack()
label9 = tk.Label(window, text="Next")
label9.pack()
label10 = tk.Label(window, text="Save Entry")
label10.pack()
label.place(x=150,y=40)
label2.place(x=225,y=6)
label3.place(x=20,y=110)
label4.place(x=100,y=110)
label5.place(x=180,y=110)
label6.place(x=260,y=110)
label7.place(x=340,y=110)
label8.place(x=8,y=170)
label9.place(x=340,y=110)
label9.place(x=340,y=110)

t = Text(window, height=1, width=9)
t.place(x=320,y=6)
t = Text(window, height=1, width=5)
t.place(x=20,y=130)
t = Text(window, height=1, width=5)
t.place(x=100,y=130)
t = Text(window, height=1, width=5)
t.place(x=180,y=130)
t = Text(window, height=1, width=5)
t.place(x=260,y=130)
t = Text(window, height=1, width=5)
t.place(x=340,y=130)
t = Text(window, height=1, width=5)
t.place(x=10,y=6)
t = Text(window, height=1, width=5)
t.place(x=10,y=6)
t = Text(window, height=1, width=5)
t.place(x=10,y=6)
canvas = Canvas(window, width = 110, height = 110)      
canvas.place(x=-10,y=-10)     
img = PhotoImage(file="dog.png")      
canvas.create_image(20,20, anchor=NW, image=img)   

window.mainloop()


#: A minimal tkinter Application

from tkinter import *
import tkinter
w = Tk()

l1 = Label(w, text="one",height=5,width=10, bg="#FFB857")
l1.pack()
l2 = Label(w, text="two",height=5,width=10, bg="#8EC2C9")
l2.pack()
l3 = Label(w, text="three",height=5,width=10, bg="#FF7182")
l3.pack()

l4 = Label(w, text="four",height=5,width=10, bg="#FFB857")
l4.pack()
l5 = Label(w, text="five",height=5,width=10, bg="#8EC2C9")
l5.pack()
l6 = Label(w, text="six",height=5,width=10, bg="#FF7182")
l6.pack()

l7 = Label(w, text="seven",height=5,width=10, bg="#FFB857")
l7.pack()
l8 = Label(w, text="eight",height=5,width=10, bg="#8EC2C9")
l8.pack()
l9 = Label(w, text="nine",height=5,width=10, bg="#FF7182")
l9.pack()

l10 = Label(w, text="ten",height=5,width=10, bg="#FFB857")
l10.pack()

w.mainloop()
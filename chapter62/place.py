from tkinter import *
top = Tk()  
top.geometry("400x250")  
Username = Label(top, text = "Username").place(x = 30,y = 50)  
email = Label(top, text = "Email").place(x = 30, y = 90)  
e1 = Entry(top).place(x = 80, y = 50)  
e2 = Entry(top).place(x = 80, y = 90)  
top.mainloop()  

######geometry manager
#pack
import tkinter as tk
win = tk.Tk()
# add an orange frame
frame1 = tk.Frame(master=win, width=100, height=100, bg="orange")
frame1.pack()
# add blue frame
frame2 = tk.Frame(master=win, width=100, height=100, bg="blue")
frame2.pack()

# add red frame
frame3 = tk.Frame(master=win, width=100, height=100, bg="red")
frame3.pack()
win.mainloop()


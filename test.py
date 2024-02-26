from tkinter import *

window = Tk()
window.geometry("200x200")
r = Label(window, bg="red",width=10, height=10)
g = Label(window,bg = "green",width=10,height=10)
r.grid(row=0, column=0)
g.grid(row=1, column=1)
window.mainloop()
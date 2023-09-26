from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Календарь")
root.geometry("400x350")
icon = PhotoImage(file = "img/list1.png")
root.iconphoto(False, icon)
root.configure(background="violet")

label = Label(text="Hello world!")
label.pack()


root.mainloop()
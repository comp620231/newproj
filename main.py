from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Календарь")
root.geometry("400x350")
icon = PhotoImage(file = "img/list1.png")
root.iconphoto(False, icon)
root.configure(background="pink")

label = Label(text="Добрый день!")
label.pack()


root.mainloop()
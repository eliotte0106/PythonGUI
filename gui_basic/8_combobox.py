import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Hong GUI")
root.geometry("640x480")#width * height + x coor + y coor
values = [str(i) + "day" for i in range(1,32)]
combobox = ttk.Combobox(root, height = 5, values =values)
combobox.pack()
combobox.set("due date")

readonly_combobox = ttk.Combobox(root, height = 10, values =values,state="readonly")
readonly_combobox.current(0) # 0 index
readonly_combobox.pack()

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())


btn = Button(root, text="select", command = btncmd)
btn.pack()

root.mainloop()
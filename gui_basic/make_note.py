import os
from tkinter import *

root = Tk()
root.title("no title - note")
root.geometry("640x480")#width * height + x coor + y coor

#save, open file name
filename = "mynote.txt"

#commands
def open_file():
    if os.path.isfile(filename): #if file exists, true
        with open(filename,"r",encoding = "utf8") as file:
            txt.delete("1.0",END) # delete original text
            txt.insert(END, file.read()) # insert txt
def save_file():
    with open(filename,"w",encoding="utf8") as file:
        file.write(txt.get("1.0",END)) # save all info
def cut():
    pass
def appear():
    pass
def pre():
    pass
def search():
    pass

#file, view, help, finder
menu = Menu(root)

menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="open", command = open_file)
menu_file.add_command(label="save", command = save_file)
menu_file.add_separator()
menu_file.add_command(label="exit",command=root.quit)
menu.add_cascade(label="file",menu=menu_file)

menu_edit = Menu(menu,tearoff=1)
menu_edit.add_command(label="cut",command = cut)
menu.add_cascade(label="edit",menu=menu_edit)

menu_view = Menu(menu,tearoff=2)
menu.add_cascade(label="view",menu = menu_view)
menu_view.add_command(label="appearance", command = appear)

menu_Finder = Menu(menu,tearoff=3)
menu_Finder.add_command(label="preference",command = pre)
menu.add_cascade(label="Finder",menu = menu_Finder)

menu_help = Menu(menu,tearoff=4)
menu_help.add_command(label="search", command = search)
menu.add_cascade(label="help",menu = menu_help)

#scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill = "y")

#for write
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)

root.config(menu=menu)

root.mainloop()
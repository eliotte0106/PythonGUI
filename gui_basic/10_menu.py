from tkinter import *

root = Tk()
root.title("Hong GUI")
root.geometry("640x480")

def create_new_file():
    print("make a new file")

menu = Menu(root)

menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label="New File", command = create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(lab="Open File...")

menu.add_cascade(label="File", menu=menu_file)

root.config(menu=menu)
root.mainloop()
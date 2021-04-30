from tkinter import *

root = Tk()
root.title("Hong GUI")
root.geometry("640x480+300+200")

label1 = Label(root,text ="hello")
label1.pack() 

photo = PhotoImage(file="img.png")
label2 = Label(root,image=photo)
label2.pack()

def change():
    label1.config(text="see u")

    global photo2
    photo2 = PhotoImage(file="hair.png")
    label2.config(image=photo2)

btn = Button(root,text="click",command = change)
btn.pack()
root.mainloop()
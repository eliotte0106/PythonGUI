from tkinter import *

root = Tk()
root.title("Hong GUI")
root.geometry("640x480")#width * height + x coor + y coor

chkvar = IntVar()
chkbox = Checkbutton(root, text = "no see today",variable = chkvar)
# chkbox.select()
# chkbox.deselect()
chkbox.pack()

chkvar2= IntVar()
chkbox2 = Checkbutton(root,text="no see for a week",variable=chkvar2)
chkbox2.pack()
def btncmd():
   print(chkvar.get()) #0 : not check, 1: check

btn = Button(root, text="click", command = btncmd)
btn.pack()

root.mainloop()
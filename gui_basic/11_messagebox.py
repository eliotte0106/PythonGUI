import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Hong GUI")
root.geometry("640x480")

#ex)train ticket
def info():
    msgbox.showinfo("notice","complete purchase")

def warn():
    msgbox.showwarning("notice","no seats available")

def error():
    msgbox.showwarning("error","error!!!")

def okcancel():
    msgbox.askokcancel("buy/ no","this seat is narrow, you want to buy ?")

def retrycancel():
    msgbox.askretrycancel("retry/ no","temporary error. retry ?")

def yesno():
    msgbox.askyesno("yes/ no","reversed way, you want to reserve ?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None,message="yes or no or cancel? ")
    if response == 1:
        print("yes")
    elif response == 0:
        print("no")
    else:
        print("cancel")
Button(root,command=info,text="notice").pack()
Button(root,command=warn,text="warning").pack()
Button(root,command=error,text="error").pack()
Button(root,command=okcancel,text="ok cancel").pack()
Button(root,command=retrycancel,text="retry cancel").pack()
Button(root,command=yesno,text="yes no").pack()
Button(root,command=yesnocancel,text="yes no cancel").pack()

root.mainloop()
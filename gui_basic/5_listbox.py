from tkinter import *

root = Tk()
root.title("Hong GUI")
root.geometry("640x480")#width * height + x coor + y coor

listbox = Listbox(root,selectmode="extended",height=0)
listbox.insert(0,"apple")
listbox.insert(1,"strawberry")
listbox.insert(2,"banana")
listbox.insert(END,"watermelon")
listbox.insert(END,"grape")
listbox.pack()



def btncmd():
    listbox.delete(END)#delete last one
    #갯수확인
    #print("list is",listbox.size(),"here")
    #항목확인
    #print("from 1 to 3 :",listbox.get(0,2))
    #선택된 항목 확인
    print("selected index :",listbox.curselection())

btn = Button(root, text="click", command = btncmd)
btn.pack()

root.mainloop()
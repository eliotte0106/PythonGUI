from tkinter import *

root = Tk()
root.title("Hong GUI")

btn1 = Button(root,text = "button1")
btn1.pack()

btn2 = Button(root,padx = 5,pady=10,text="button2")
btn2.pack()

btn3 = Button(root,width=10,height=3,text="button3")
btn3.pack()

btn5 = Button(root,fg="red", bg="yellow", text="button5")
btn5.pack()

photo = PhotoImage(file="img.png")
btn6 = Button(root,image=photo)
btn6.pack()

def btncmd():
    print("button is clicked")

btn7 = Button(root, text = "operating button", command = btncmd)
btn7.pack()
root['bg'] = 'blue'

root.mainloop()
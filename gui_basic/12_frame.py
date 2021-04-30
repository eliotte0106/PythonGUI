from tkinter import *

root = Tk()
root.title("Hong GUI")
root.geometry("640x480")

Label(root,text="choose the menu").pack(side="top")

Button(root,text = "order").pack(side="bottom")
#frame
frame_burger = Frame(root, relief = "solid", bd = 1)
#use all the left side
frame_burger.pack(side ="left",fill="both",expand=True)

Button(frame_burger, text="burger").pack()
Button(frame_burger, text="cheese burger").pack()
Button(frame_burger, text="chicken burger").pack()

#label frame
frame_drink = LabelFrame(root,text = "drink")
#use all the right side
frame_drink.pack(side="right",fill="both",expand=True)
Button(frame_drink, text="sprite").pack()
Button(frame_drink, text="coke").pack()

root.mainloop()
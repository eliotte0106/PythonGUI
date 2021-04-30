import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Hong GUI")
root.geometry("640x480")#width * height + x coor + y coor

#progressbar = ttk.Progressbar(root,maximum=100,mode="indeterminate")
# progressbar = ttk.Progressbar(root,maximum=100,mode="determinate")
# progressbar.start(10)
# progressbar.pack()

# def btncmd():
#     progressbar.stop()


# btn = Button(root, text="stop", command = btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root,maximum=100,length=150,variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1,101):
        time.sleep(0.01) # 0.01 delay
        p_var2.set(i) # 값 설정
        progressbar2.update() # ui update
        print(p_var2.get())

btn = Button(root, text="start", command = btncmd2)
btn.pack()

root.mainloop()
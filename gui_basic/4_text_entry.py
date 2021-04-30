from tkinter import *

root = Tk()
root.title("Hong GUI")
root.geometry("640x480")#width * height + x coor + y coor

txt = Text(root,width=30,height=5)
txt.pack()
txt.insert(END,"enter words")

e = Entry(root, width=30)
e.pack()
e.insert(0,"enter only one line")

def btncmd():
    #내용 출력
    print(txt.get("1.0",END)) # 1:첫번째라인, 0:0번째 콜럼 위치
    print(e.get())
    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)
btn = Button(root, text="click", command = btncmd)
btn.pack()

root.mainloop()
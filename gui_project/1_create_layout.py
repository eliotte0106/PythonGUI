import tkinter.ttk as ttk 
from tkinter import *

root = Tk()
root.title("Hong GUI")

#file frame (file add, delete)
file_frame = Frame(root)
file_frame.pack(fill="x",padx=5,pady=5) #space

btn_add_file = Button(file_frame,padx=5,pady=5,width=12,text="file add")
btn_add_file.pack(side="left")
btn_delete_file = Button(file_frame,padx=5,pady=5,width=12,text="delete file")
btn_delete_file.pack(side="right")

#list frame
list_frame = Frame(root)
list_frame.pack(fill="both",padx=5,pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right",fill="y")

list_file = Listbox(list_frame,selectmode="extended",height=15,yscrollcommand=scrollbar.set)
list_file.pack(side="left",fill="both",expand=True)
scrollbar.config(command=list_file.yview)

#path frame
path_frame = LabelFrame(root,text="save path")
path_frame.pack(fill="x",padx=5,pady=5,ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left",fill="x",expand=True,padx=5,pady=5,ipady=4)#height change

btn_dest_path = Button(path_frame,text = "look up file",width = 10)
btn_dest_path.pack(side="right",padx=5,pady=5)

#option frame
frame_option = LabelFrame(root,text="option")
frame_option.pack(padx=5,pady=5,ipady=5)

#1.width area option
#width area label
lbl_width = Label(frame_option,text="width area",width=8)
lbl_width.pack(side="left",padx=5,pady=5)

#width area combo
opt_width = ["original","1024","800","640"]
cmb_width = ttk.Combobox(frame_option,state="readonly",values=opt_width,width=10)
cmb_width.current(0)
cmb_width.pack(side="left",padx=5,pady=5)

#2.space option
#space option label
lbl_space = Label(frame_option,text="width area",width=8)
lbl_space.pack(side="left",padx=5,pady=5)

#space option combo
opt_space = ["none","narrow","normal","wide"]
cmb_space = ttk.Combobox(frame_option,state="readonly",values=opt_space,width=10)
cmb_space.current(0)
cmb_space.pack(side="left",padx=5,pady=5)
#3.file format option
#format option label
lbl_format = Label(frame_option,text="format",width=8)
lbl_format.pack(side="left",padx=5,pady=5)

#format option combo
opt_format = ["png","jpg","bmp"]
cmb_format = ttk.Combobox(frame_option,state="readonly",values=opt_format,width=10)
cmb_format.current(0)
cmb_format.pack(side="left",padx=5,pady=5)

#progress bar
frame_progess = LabelFrame(root,text="in progess")
frame_progess.pack(fill="x",padx=5,pady=5,ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progess,maximum=100,variable=p_var)
progress_bar.pack(fill="x",padx=5,pady=5)

#run frame
frame_run = Frame(root)
frame_run.pack(fill="x",padx=5,pady=5)

btn_close=Button(frame_run,padx=5,pady=5,text="close",width=12,command=root.quit)
btn_close.pack(side="right",padx=5,pady=5)
btn_start = Button(frame_run,padx=5,pady=5,text="start",width=12)
btn_start.pack(side="right",padx=5,pady=5)



root.resizable(False, False)#x,y cannot change
root.mainloop()
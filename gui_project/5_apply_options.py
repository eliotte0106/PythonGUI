import os
import tkinter.ttk as ttk 
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("Hong GUI")

#file add
def add_file():
    files = filedialog.askopenfilenames(title="select image file", \
        filetypes=(("png file","*.png"),("jpg file","*.jpg"),("all file","*.*")),\
        initialdir="/Users/")
    #selected file list
    for file in files:
        list_file.insert(END, file)

#file delete
def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

#save path (folder)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '': #if user used cancel
        return
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(0,folder_selected)


#image merge
def merge_image():
    #print("width area: ",cmb_width.get())
    #print("space: ", cmb_space.get())
    #print("format: ",cmb_format.get())

    try:
        #width length
        img_width = cmb_width.get()
        if img_width == "original":
            img_width = -1 # -1 : original
        else:
            img_width = int(img_width)
        
        #space
        img_space = cmb_space.get()
        if img_space == "narrow":
            img_space = 30
        elif img_space == "normal":
            img_space = 60
        elif img_space == "wide":
            img_space = 90
        else:
            img_space = 0


        #format
        img_format = cmb_format.get().lower() #png,jpg,bmp to lower case
        
        #####

        images = [Image.open(x) for x in list_file.get(0,END)]

        #image size list and process each one
        image_sizes = []
        if img_width > -1:
            # width size change (ratio rule)
            image_sizes = [(int(img_width),int(img_width*x.size[1]/x.size[0])) for x in images]
        else:
            image_sizes = [(x.size[0],x.size[1]) for x in images] # original size

        #equation
        #if 100 * 60 image, width --> 80, height --> ?

        widths,heights = zip(*(image_sizes))

        max_width, total_height = max(widths),sum(heights)
        
        #sketchbook
        if img_space > 0: #image space option
            total_height += (img_space * (len(images) -1))
        result_img = Image.new("RGB",(max_width,total_height),(255,255,255))#white background
        y_offset = 0 # y position
    
        
        for idx,img in enumerate(images):
            #if width is not original image size change need
            if img_width > -1 :
                img = img.resize(image_sizes[idx])

            result_img.paste(img,(0,y_offset))
            y_offset += (img.size[1] + img_space) # height + user input space

            progress = (idx + 1) / len(images) * 100 # actual percentage info calculate
            p_var.set(progress)
            progress_bar.update()


        #format option
        file_name = "hong_photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(),file_name)
        result_img.save(dest_path)
        msgbox.showinfo("notice","process complete")
    except Exception as err:
        msgbox.showerror("error",err)

#start
def start():
    #each option
    print("width area: ",cmb_width.get())
    print("space: ", cmb_space.get())
    print("format: ",cmb_format.get())

    #file list check
    if list_file.size() == 0:
        msgbox.showwarning("warning","add your image file")
        return
    #path check
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("warning","select your save path")
        return
    #image process
    merge_image()

#file frame (file add, delete)
file_frame = Frame(root)
file_frame.pack(fill="x",padx=5,pady=5) #space

btn_add_file = Button(file_frame,padx=5,pady=5,width=12,text="add file",command=add_file)
btn_add_file.pack(side="left")
btn_delete_file = Button(file_frame,padx=5,pady=5,width=12,text="delete file",command=del_file)
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

btn_dest_path = Button(path_frame,text = "look up path",width = 10,command=browse_dest_path)
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
btn_start = Button(frame_run,padx=5,pady=5,text="start",width=12,command = start)
btn_start.pack(side="right",padx=5,pady=5)



root.resizable(False, False)#x,y cannot change
root.mainloop()
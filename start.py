########################################################################################################################
####################################### NOTESPRO STARTING UI ###########################################################
########################################################################################################################

from tkinter import *
import os

from cam_ocr import main
from file_explorer import mn
root=Tk()
root.title("Note-Taking App")
p=Label(root,text="AENTO", height="9",width="250",bg='brown',fg='white',font=('Times New Roman','35','bold'))
p.pack()
root.configure(bg='brown')
root.geometry('600x700')
def notes():
    import cam_ocr
    import file_explorer
butt1=Button(root,text="Add Notes",command=main,bg = "olive",fg='white',padx=40,pady=10,font=('Comic Sans MS','10','bold'))
butt1.pack(padx=25,pady=0)
butt2=Button(root,text="Browse Notes",command=mn,bg = "olive",fg='white',padx=35,pady=10,font=('Comic Sans MS','10','bold'))
butt2.pack(padx=25,pady=5)
button=Button(root,text="Exit",command=root.destroy,bg = "#636466",fg='white',padx=30,pady=10,font=('Comic Sans MS','10','bold'))
button.pack(padx=25,pady=0)
root.mainloop()
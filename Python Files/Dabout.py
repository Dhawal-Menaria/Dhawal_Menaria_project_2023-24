# Dabout page
from tkinter import *
root=Tk()
x = int((root.winfo_screenwidth() - 500) / 2)
y = int((root.winfo_screenheight() - 500) / 2)
root.geometry(f'500x500+{x}+{y}')
root.title("Dhawal's About Window")
root.resizable(False,False)
root.config(bg='#ec1c24')

head_about = Label(root,text='About Me',font=('Canva Sans',20),bg='#ec1c24', fg='#ffde91')
head_about.place(x=190,y=50)

description = Label(root,text="""


I'm Dhawal Menaria from Class XI Science D

at St. Anthony's Sr. Sec. School.I believe 

in the power of collective effort to overcome 

challenges and create something extraordinary.""",font=('Canva Sans',15),bg='#ec1c24', fg='#ffde91')
description.place(x=40,y=100)

def on_close():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)


root.mainloop()
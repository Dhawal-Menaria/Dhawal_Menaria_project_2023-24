# Dwelcomescreen page
from tkinter import *

root=Tk()
x = int((root.winfo_screenwidth() - 1000) / 2)
y = int((root.winfo_screenheight() - 562) / 2)
root.geometry(f'1000x562+{x}+{y}')
root.title("Dhawal's Welcome Screen")
root.overrideredirect(True)


def afterIT():
    root.destroy()

bg_img=PhotoImage(file='my_img_welcome.png')
bg=Label(root, image=bg_img,border=0)
bg.place(x=0,y=0)

root.after(5000,afterIT)


root.mainloop()

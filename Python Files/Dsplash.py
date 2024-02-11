# Dsplash page
from tkinter import *
import time

root = Tk()
x = int((root.winfo_screenwidth() - 500) / 2)
y = int((root.winfo_screenheight() - 500) / 2)



root.geometry(f'500x500+{x}+{y}')
root.config(bg="white")
root.overrideredirect(True)

img = PhotoImage(file="my_img_splash.png")
main_pic = Label(image=img,bg="#ffca18")
main_pic.place(x=-1,y=-1)

logo = PhotoImage(file="school_logo/school_logo_yellow.png")
schl_logo = Label(image=logo, bg="#ffca18")
schl_logo.place(x=0,y=0)


schl_name = Label(text="""St. Anthony's Sr. Sec. School 
Project 2023-2024""",font=("Californian FB",22),bg="#ffca18")
schl_name.place(x=155,y=2)

My_name = Label(text="""Made By : Dhawal Menaria
Class : XI Science D""",font=("Californian FB",25),bg="#ffca18")
My_name.place(x=50,y=400)

def closeIT():
    root.destroy()
root.after(3000,closeIT)
root.mainloop()
# Dprogressbar page

from tkinter import *
from tkinter.ttk import Progressbar

root=Tk()
x = int((root.winfo_screenwidth() - 500) / 2)
y = int((root.winfo_screenheight() - 500) / 2)
root.overrideredirect(True)
root.geometry(f'500x450+{x}+{y}')
root.title("Dhawal Menaira's Progress Bar")

img = PhotoImage(file="my_img_progress.png")
main_pic = Label(image=img,border=0)
main_pic.place(x=0,y=0)

pro_name1 = Label(root, text = 'Project', font = ("Arial",20),bg='#bf0b0d', fg='white')
pro_name1.place(x=140,y=10)
pro_name2 = Label(root, text = '2023-2024', font = ("Arial",20),bg='#bf0b0d', fg='white')
pro_name2.place(x=275,y=10)

lbl1 = Label(root, text = "ST.", font = ("Consolas",19),bg='#931920', fg='white')
lbl1.place(x=50,y=50)
lbl2 = Label(root, text = "ANTHONY'S", font = ("Consolas",19),bg='#bf0b0d', fg='white')
lbl2.place(x=100,y=50)
lbl3 = Label(root, text = "SR.SEC.SCHOOL", font = ("Consolas",19),bg='#bf0b0d', fg='white')
lbl3.place(x=270,y=50)

lb3 =Label(root,text="0%",font=('bold',30), bg='#eefefe')
lb3.place(x=200,y=115)


def startbar():
    s=""
    import time                      
    for i in range(101):
        bar['value']=i                       
        time.sleep(.01)
        ss=str(i)+"%"
        lb3.config(text=ss)
        root.update_idletasks()
        if i % 5 != 0:
            loading_text.config(fg="#ffffff")
        else:
            loading_text.config(fg="#931217")
    time.sleep(0.3)
        
    root.destroy()

md =Label(root,text="""Made by : Dhawal Menaria
Class XI Science D""",font=('bold',11), bg='#931318',fg="white")
md.place(x=166,y=275)

Label(root,text='Progress Bar...',fg='white', bg='Teal', font=('Arial',15)).place(x=30,y=510)
bar = Progressbar(root, length = 440,value=0,mode='determinate')
bar.place(x=30,y=350)

loading_text = Label(text = "Loading . . .",font=("Arial",15),fg = "#ffffff",bg="#931217")
loading_text.place(x=175,y=375)

root.after(700,startbar)

root.mainloop()
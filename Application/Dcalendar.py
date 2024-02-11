from tkinter import *
from tkcalendar import Calendar

def Dcalendar():
    root = Tk()
    x = int((root.winfo_screenwidth() - 185) / 2)
    y = int((root.winfo_screenheight() - 250) / 2)
    root.geometry(f'250x185+{x}+{y}')
    root.title("Dhawal's Calendar Window")
    root.resizable(False,False)
    mycal = Calendar(root,setmode="day",date_pattern="d/m/yy")
    mycal.pack()
    root.mainloop()

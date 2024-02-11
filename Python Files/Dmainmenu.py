# Dmainmenu page
import Dsplash
import Dprogressbar
import Dwelcomescreen
import Dauth
import Dcalculator
import Dcalendar
import Dscreensaver
import Dgame
from tkinter import *
from tkinter import messagebox
import webbrowser
root = Tk()
root.title("Dhawal's Mainmenu page")
x = int((root.winfo_screenwidth() - 1000) / 2)
y = int((root.winfo_screenheight() - 625) / 2)
root.geometry(f'1000x625+{x}+{y}')
root.resizable(False,False)
menubar = Menu(root)
def dhelp():
    import Dhelp
def dabout():
    import Dabout
menubar.add_command(label ='Help', command = dhelp) 
menubar.add_command(label ='About Me', command = dabout) 
menubar.add_command(label ='Exit', command = root.destroy) 
root.config(bg="#ec1c24",menu=menubar)

bgimg = PhotoImage(file="my_img_main.png")
bg = Label(root,image=bgimg,border=0)
bg.place(x=0,y=0)

def GoToCalculator():
    Dcalculator.dCalc()
def GoToSchoolWebsite():
    webbrowser.open("https://www.sasudaipur.com/")
def GoToMyOwnWebsite():
    webbrowser.open("http://dartstore.vercel.app/")
def GoToGame():
    messagebox.showinfo("Loading","Be patient , game is loading ;)")
    game = Dgame.Dgame()
    game.start_game()
def GoToCalendar():
    Dcalendar.Dcalendar()
def GoToScreenSaver():
    Dscreensaver.Dscreensaver()


mywebbtn = Button(root,text='My Own Website',font=('Roboto Medium',15),bg="#ffcc00",fg="#000000",border=5,command=GoToMyOwnWebsite)
mywebbtn.place(x=10,y=10)
calcbtn = Button(root,text='Calculator',font=('Digital-7',16),bg="#7af3d3",fg="#043c8d",border=5,command=GoToCalculator)
calcbtn.place(x=10,y=200)
gamebtn = Button(root,text='Game',font=('Charge Vector Bold',15),bg="white",fg="red",border=5,command=GoToGame)
gamebtn.place(x=10,y=410)


schwebbtn = Button(root,text='School Website',font=('Arial',15),bg="red",fg="light blue",border=5,command=GoToSchoolWebsite)
schwebbtn.place(x=810,y=10)
screensaverbtn = Button(root,text='Screen Saver',font=('Arial',15),bg="#1f2427",fg="white",border=5,command=GoToScreenSaver)
screensaverbtn.place(x=828,y=200)
calendarbtn = Button(root,text='Calendar',font=('Times New Roman',15),bg="#fff689",fg="#1e2136",border=5,command=GoToCalendar)
calendarbtn.place(x=874,y=410)

root.mainloop()
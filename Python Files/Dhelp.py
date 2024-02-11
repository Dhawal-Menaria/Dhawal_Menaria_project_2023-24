# Dhelp page
from tkinter import *
root=Tk()
x = int((root.winfo_screenwidth() - 700) / 2)
y = int((root.winfo_screenheight() - 500) / 2)
root.geometry(f'700x500+{x}+{y}')
root.title("Dhawal's Help Window")
root.config(bg='#ec1c24')
root.resizable(False,False)

head_about = Label(root,text='Help Page',font=('bold',20),bg='#ec1c24', fg='#ffde91')
head_about.place(x=300,y=50)

description = Label(root,text="""

"Welcome to the Help Section!
This program is designed to assist you with your school project.
If you have any questions or need assistance, please refer to the following:
1. go to second one .
2. go to third one .
3. I can't do anything about this I mean this is a simplest program I can make.
If you still require assistance, feel free to reach out to the developer.
Contact Information:
Developer Name: I mean seriously !!
Thank you for using my program!
""",font=('Canva Sans',15),bg='#ec1c24', fg='#ffde91')
description.place(x=10,y=100)

def on_close():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)


root.mainloop()

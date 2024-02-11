from tkinter import *
from tkinter import messagebox
import sys


class Dauth:
    def __init__(self, root):
        self.root = root
        self.root.title("Dhawal's Login and Registration page")

        x = int((root.winfo_screenwidth() - 750) / 2)
        y = int((root.winfo_screenheight() - 500) / 2)
        root.geometry(f'750x500+{x}+{y}')
        root.resizable(False,False)
        menubar = Menu(root)
        def dhelp():
            import Dhelp
        def dabout():
            import Dabout
        def dexit():
            root.destroy()
            sys.exit()
        menubar.add_command(label ='Help', command = dhelp) 
        menubar.add_command(label ='About Me', command = dabout) 
        menubar.add_command(label ='Exit', command = dexit) 
        root.config(bg="#ec1c24",menu=menubar)
        root.overrideredirect(True)

        self.logoimg = PhotoImage(file="school_logo/school_logo_red.png")
        self.logo = Label(root,image=self.logoimg,border=0)
        self.logo.place(x=450,y=0)

        self.sidimg = PhotoImage(file="my_img_register.png")
        self.sid = Label(self.root,image=self.sidimg,border=0)
        self.sid.place(x=0,y=0)

        
        schl = Label(root, text = "ST. ANTHONY'S SR. SEC. SCHOOL", font = ("Arial",15),bg='#ec1c24', fg='#ffde91')
        schl.place(x=370,y=130)


        pro_name = Label(root, text = '''Project 2023-24
        Made by Dhawal Menaria''', font = ("Arial",15),bg='#ec1c24', fg='#ffde91')
        pro_name.place(x=415,y=155)

        self.login_frame = Frame(root,width=450,height=250,relief="raised",bg='#ec1c24')
        self.register_frame = Frame(root,relief="raised",bg="#ec1c24")

        self.Dlogin()
        self.Dregister()

        self.showDlogin()
    
    def Dlogin(self):
        l1 = Label(self.login_frame, text = "Username", font = ("Arial",15),bg='#ec1c24', fg='#ffde91')
        l1.grid(row=0,column=0)
        e1 = Entry(self.login_frame,font=("Arial",15))
        e1.grid(row=0,column=1)



        show_eye = PhotoImage(file="show_eye.png")
        close_eye = PhotoImage(file="close_eye.png")
        
        def shhi():
            if e2["show"] == "*":
                e2["show"] = ""
                showp["image"] = close_eye
            else:
                e2["show"] = "*"               
                showp["image"] = show_eye
        l2 = Label(self.login_frame, text = "Password", font = ("Arial",15),bg='#ec1c24', fg='#ffde91')
        l2.grid(row=1,column=0,pady=50)
        e2 = Entry(self.login_frame,font=("Arial",15),show="*")
        e2.grid(row=1,column=1,pady=50)
        showp = Button(self.login_frame,text="s",image=show_eye,font=("Arial",12),border=0,command=shhi)
        showp.grid(row=1,column=2,pady=50)

        def login():
            d=e1.get()
            p=e2.get()
            f=open('DataOfUser.xls','r')
            s=f.read().split('\n')
            f.close()
            patanhi = 0
            for i in s:
                a=i.split('\t')
                if len(a[0])<1:
                    break
                if a[1]==d and a[3]==p:
                    patanhi += 1
                    break
                else :
                    patanhi += 0
            if patanhi:
                messagebox.showinfo("Login Successfull!","Successfully logged in")
                root.destroy()
                # main(d)
            else:
                messagebox.showwarning("Login Failed","please re-enter your password or create it.")

        login=Button(self.login_frame,text='Login',bg="#ffde91", fg='#5391a0',font=('Arial',15),command=login)
        login.grid(row=2,column=0)

        goreg=Button(self.login_frame,text='Go to Register page',bg="#ffde91", fg='#5391a0',font=('Arial',15),command=self.showDregister)
        goreg.grid(row=2,column=1)

    def Dregister(self):
        l1 = Label(self.register_frame, text = "Name", font = ("Arial",15),bg='#ec1c24', fg='#ffde91')
        l1.grid(row=0,column=0,)

        self.e1 = Entry(self.register_frame,font=("Arial",15))
        self.e1.grid(row=0,column=1)


        l2 = Label(self.register_frame, text = "Username", font = ("Arial",15),bg='#ec1c24', fg='#ffde91')
        l2.grid(row=1,column=0,padx=0)
        self.e2 = Entry(self.register_frame,font=("Arial",15))
        self.e2.grid(row=1,column=1)



        l3 = Label(self.register_frame, text = "Email ID", font = ("Arial",15),bg='#ec1c24', fg='#ffde91')
        l3.grid(row=2,column=0,padx=0)
        self.e3 = Entry(self.register_frame,font=("Arial",15))
        self.e3.grid(row=2,column=1)



        l4 = Label(self.register_frame, text = "Password", font = ("Arial",15),bg='#ec1c24', fg='#ffde91')
        l4.grid(row=3,column=0,padx=0)
        self.e4 = Entry(self.register_frame,font=("Arial",15))
        self.e4.grid(row=3,column=1)



        l5 = Label(self.register_frame, text = "Re-Type Password", font = ("Arial",15),bg='#ec1c24', fg='#ffde91')
        l5.grid(row=4,column=0,padx=0)
        self.e5 = Entry(self.register_frame,font=("Arial",15))
        self.e5.grid(row=4,column=1)



        l4 = Label(self.register_frame, text = "Gender", font = ("Arial",15),bg='#ec1c24', fg='#ffde91')
        l4.grid(row=5,column=0)
        self.rad = IntVar()
        self.genderframe = Frame(self.register_frame)
        self.f1=Radiobutton(self.genderframe,text="Male",value=1,variable=self.rad, font=('Arial',15),bg="#5391a0", fg='#000000')
        self.f1.grid(row=0,column=0)
        self.f2=Radiobutton(self.genderframe,text="Female",value=2,variable=self.rad, font=('Arial',15),bg="#5391a0", fg='#000000')
        self.f2.grid(row=0,column=1)
        self.genderframe.grid(row=5,column=1)

        regi=Button(self.register_frame,text='Register',bg="#ffde91", fg='#5391a0',font=('Arial',15),command=self.register)
        regi.grid(row=6,column=0)
        golog=Button(self.register_frame,text='Go to login page',bg="#ffde91", fg='#5391a0',font=('Arial',15),command=self.showDlogin)
        golog.grid(row=6,column=1)


    def showDlogin(self):
        # Show login layout and hide register layout
        self.register_frame.place_forget()
        self.login_frame.place(x=330,y=250)

    def showDregister(self):
        # Show register layout and hide login layout
        self.login_frame.place_forget()
        self.register_frame.place(x=330,y=250)


    def register(self):
        a=self.e1.get()
        b=self.e2.get()
        c=self.e3.get()
        d=self.e4.get()
        e=self.e5.get()
        f=self.rad.get()
        v=""
        if a == "" or b == "" or c == "" or d == "" or e == "":
            messagebox.showwarning("Insufficient Details","Please fill all the details required")
        elif ".com" not in c:
            messagebox.showwarning("e-mail is not valid","Please enter a valid email address")
        elif d==e:
            if f==1:
                v='Male'
            if f==2:
                v='Female'
        
            s=f"{a}\t{b}\t{c}\t{d}\t{e}\t{v}\n"
            f=open('DataOfUser.xls','a')
            f.write(s)
            f.close()
            self.e1.delete(0,END)
            self.e2.delete(0,END)
            self.e3.delete(0,END)
            self.e4.delete(0,END)
            self.e5.delete(0,END)
            messagebox.showinfo("Account Creation Successful ","Your'e has been created Successfully")
            
        else:
            messagebox.showwarning("Password Doesn't Match","Please Retype correct password")
            e5.delete(0,END)


root = Tk()
app = Dauth(root)
root.mainloop()
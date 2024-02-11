# Dcalculator page
from tkinter import *
class Dcalculator:
    def __init__(self,root):
        self.root = root
        x = int((root.winfo_screenwidth() - 300) / 2)
        y = int((root.winfo_screenheight() - 275) / 2)
        root.geometry(f'260x271+{x}+{y}')
        root.title("Dhawal's Calculator Window")
        root.resizable(False,False)
        self.calculations = ""
        self.text_result = Text(root,height=2,width=14,font=("Arial",24))
        self.text_result.grid(columnspan=5)
        self.btn_1 = Button(root,text='1',command=lambda:self.add_calc(1),width=5,font=("Arial",14),bg="Yellow",fg="Red")
        self.btn_1.grid(row=2,column=1)
        self.btn_2 = Button(root,text='2',command=lambda:self.add_calc(2),width=5,font=("Arial",14),bg="Yellow",fg="Red")
        self.btn_2.grid(row=2,column=2)
        self.btn_3 = Button(root,text='3',command=lambda:self.add_calc(3),width=5,font=("Arial",14),bg="Yellow",fg="Red")
        self.btn_3.grid(row=2,column=3)
        self.btn_4 = Button(root,text='4',command=lambda:self.add_calc(4),width=5,font=("Arial",14),bg="Yellow",fg="Red")
        self.btn_4.grid(row=3,column=1)
        self.btn_5 = Button(root,text='5',command=lambda:self.add_calc(5),width=5,font=("Arial",14),bg="Yellow",fg="Red")
        self.btn_5.grid(row=3,column=2)
        self.btn_6 = Button(root,text='6',command=lambda:self.add_calc(6),width=5,font=("Arial",14),bg="Yellow",fg="Red")
        self.btn_6.grid(row=3,column=3)
        self.btn_7 = Button(root,text='7',command=lambda:self.add_calc(7),width=5,font=("Arial",14),bg="Yellow",fg="Red")
        self.btn_7.grid(row=4,column=1)
        self.btn_8 = Button(root,text='8',command=lambda:self.add_calc(8),width=5,font=("Arial",14),bg="Yellow",fg="Red")
        self.btn_8.grid(row=4,column=2)
        self.btn_9 = Button(root,text='9',command=lambda:self.add_calc(9),width=5,font=("Arial",14),bg="Yellow",fg="Red")
        self.btn_9.grid(row=4,column=3)
        self.btn_0 = Button(root,text='0',command=lambda:self.add_calc(0),width=5,font=("Arial",14),bg="Yellow",fg="Red")
        self.btn_0.grid(row=5,column=2)
        self.btn_o = Button(root,text='(',command=lambda:self.add_calc("("),width=5,font=("Arial",14),bg="Red",fg="Yellow")
        self.btn_o.grid(row=5,column=1)
        self.btn_c = Button(root,text=')',command=lambda:self.add_calc(")"),width=5,font=("Arial",14),bg="Red",fg="Yellow")
        self.btn_c.grid(row=5,column=3)
        self.btn_plus = Button(root,text='+',command=lambda:self.add_calc("+"),width=5,font=("Arial",14),bg="Red",fg="Yellow")
        self.btn_plus.grid(row=2,column=4)
        self.btn_minus = Button(root,text='-',command=lambda:self.add_calc("-"),width=5,font=("Arial",14),bg="Red",fg="Yellow")
        self.btn_minus.grid(row=3,column=4)
        self.btn_multiply = Button(root,text='*',command=lambda:self.add_calc("*"),width=5,font=("Arial",14),bg="Red",fg="Yellow")
        self.btn_multiply.grid(row=4,column=4)
        self.btn_divide = Button(root,text='/',command=lambda:self.add_calc("/"),width=5,font=("Arial",14),bg="Red",fg="Yellow")
        self.btn_divide.grid(row=5,column=4)
        self.btn_equals = Button(root,text='=',command=self.eval_calc,width=11,font=("Arial",14),bg="Orange",fg="Black")
        self.btn_equals.grid(row=6,column=3,columnspan=2)
        self.btn_clear = Button(root,text='C',command=self.clear_field,width=11,font=("Arial",14),bg="Black",fg="White")
        self.btn_clear.grid(row=6,column=1,columnspan=2)
        
    def add_calc(self,sign):
        self.calculations += str(sign)
        self.text_result.delete(1.0,"end")
        self.text_result.insert(1.0,self.calculations)
    def eval_calc(self):
        try:
            self.result = str(eval(self.calculations))
            self.calculations = ""
            self.text_result.delete(1.0,"end")
            self.text_result.insert(1.0,self.result)
        except:
            self.clear_field()
            self.text_result.insert(1.0,"Error")

    def clear_field(self):
        self.calculations = ""
        self.text_result.delete(1.0,"end")


        



def dCalc():
    root = Tk()
    app = Dcalculator(root)
    def on_close():
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

from tkinter import *

from tkinter import ttk, messagebox
import mysql.connector
#import credentials as cr


class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Company Registeration")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "white")

        #self.bg_img = ImageTk.PhotoImage(file="Images/photo1.jpeg")
        #background = Label(self.window,image=self.bg_img).place(x=0,y=0,relwidth=1,relheight=1)


        frame = Frame(self.window, bg="white")
        frame.place(x=350,y=100,width=500,height=550)

        #title1 = Label(frame, text="Register now", font=("times new roman",25,"bold"),bg="white").place(x=20, y=10)
        #title2 = Label(frame, text="Join with us", font=("times new roman",13),bg="white", fg="gray").place(x=20, y=50)

        f_name = Label(frame, text="Company id", font=("helvetica",15,"bold"),bg="white").place(x=20, y=100)
        l_name = Label(frame, text="Company name", font=("helvetica",15,"bold"),bg="white").place(x=240, y=100)

        self.fname_txt = Entry(frame,font=("arial"))
        self.fname_txt.place(x=20, y=130, width=200)

        self.lname_txt = Entry(frame,font=("arial"))
        self.lname_txt.place(x=240, y=130, width=200)

        email = Label(frame, text="Company address", font=("helvetica",15,"bold"),bg="white").place(x=20, y=180)

        self.email_txt = Entry(frame,font=("arial"))
        self.email_txt.place(x=20, y=210, width=420)

        #sec_question = Label(frame, text="Security questions", font=("helvetica",15,"bold"),bg="white").place(x=20, y=260)
        #answer = Label(frame, text="age", font=("helvetica",15,"bold"),bg="white").place(x=240, y=260)

        #self.questions = ttk.Combobox(frame,font=("helvetica",13),state='readonly',justify=CENTER)
        #self.questions['values'] = ("Select","What's your pet name?","Your first teacher name","Your birthplace", "Your favorite movie")
        #self.questions.place(x=20,y=290,width=200)
        #self.questions.current(0)

        #self.answer_txt = Entry(frame,font=("arial"))
        #self.answer_txt.place(x=240, y=290, width=200)

        #password =  Label(frame, text="tid", font=("helvetica",15,"bold"),bg="white").place(x=20, y=340)

        #self.password_txt = Entry(frame,font=("arial"))
        #self.password_txt.place(x=20, y=370, width=420)

        self.terms = IntVar()
        terms_and_con = Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.terms,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=20,y=420)
        self.signup = Button(frame,text="Register Now",command=self.signup_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=120,y=470,width=250)

    def signup_func(self):
        if self.fname_txt.get()=="" or self.lname_txt.get()=="" or self.email_txt.get()=="":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)

        elif self.terms.get() == 0:
            messagebox.showerror("Error!","Please Agree with our Terms & Conditions",parent=self.window)

        else:
            try:
                conn= mysql.connector.connect(host='localhost',password='password@123',user='root',database='buscompany')
                cur = conn.cursor()
                cur.execute("insert into bus_company (cid,cname,caddress) values(%s,%s,%s)",(self.fbn   name_txt.get(),self.lname_txt.get(),self.email_txt.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
                self.reset_fields()
            except Exception as es:
                messagebox.showerror("Error!",f"Error due to {es}",parent=self.window)

    def reset_fields(self):
        self.fname_txt.delete(0, END)
        self.lname_txt.delete(0, END)
        self.email_txt.delete(0, END)
        #self.questions.current(0)
        #self.answer_txt.delete(0, END)
        #self.password_txt.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()

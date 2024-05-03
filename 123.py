from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Company Registeration")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "white")

        frame = Frame(self.window, bg="white")
        frame.place(x=350,y=100,width=500,height=550)

        f_name = Label(frame, text="Company id", font=("helvetica",15,"bold"),bg="white").place(x=20, y=100)
        l_name = Label(frame, text="Company name", font=("helvetica",15,"bold"),bg="white").place(x=240, y=100)

        self.fname_txt = Entry(frame,font=("arial"))
        self.fname_txt.place(x=20, y=130, width=200)

        self.lname_txt = Entry(frame,font=("arial"))
        self.lname_txt.place(x=240, y=130, width=200)

        email = Label(frame, text="Company address", font=("helvetica",15,"bold"),bg="white").place(x=20, y=180)

        self.email_txt = Entry(frame,font=("arial"))
        self.email_txt.place(x=20, y=210, width=420)

        self.terms = IntVar()
        terms_and_con = Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.terms,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=20,y=420)
        self.signup = Button(frame,text="Register Now",command=self.signup_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=120,y=470,width=250)
        self.update = Button(frame,text="Update Now",command=self.update_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=120,y=510,width=250)

    def signup_func(self):
        if self.fname_txt.get()=="" or self.lname_txt.get()=="" or self.email_txt.get()=="":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)

        elif self.terms.get() == 0:
            messagebox.showerror("Error!","Please Agree with our Terms & Conditions",parent=self.window)

        else:
            try:
                conn= mysql.connector.connect(host='localhost',password='password@123',user='root',database='buscompany')
                cur = conn.cursor()
                cur.execute("insert into bus_company (cid,cname,caddress) values(%s,%s,%s)",(self.fname_txt.get(),self.lname_txt.get(),self.email_txt.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
                self.reset_fields()
            except Exception as es:
                 messagebox.showerror("Error!", f"Error Due to: {str(es)}",parent=self.window)





    def update_func(self):
        if self.fname_txt.get()=="" or self.lname_txt.get()=="" or self.email_txt.get()=="":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)

        else:
            try:
                conn= mysql.connector.connect(host='localhost',password='password@123',user='root',database='buscompany')
                cur = conn.cursor()
                cur.execute("UPDATE bus_company SET cname=%s, caddress=%s WHERE cid=%s",(self.lname_txt.get(),self.email_txt.get(),self.fname_txt.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Congratulations!","Update Successful",parent=self.window)
                self.reset_fields()
            except Exception as es:
                messagebox.showerror("Error!", f"Error Due to: {str(es)}",parent=self.window)

    def reset_fields(self):
        self.fname_txt.delete(0,END)
        self.lname_txt.delete(0,END)
        self.email_txt.delete(0,END)
        self.terms.set(0)



# import the necessary modules and classes

root = Tk()
signup = SignUp(root)
root.mainloop()

 

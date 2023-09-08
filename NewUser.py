from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector


def insert():
    name = e1.get()
    userid = e2.get()
    address = e3.get()
    email = e4.get()
    registrationno = e6.get()
    mobileno = e5.get()
    uname = e11.get()
    password = e12.get()
    password2 = e13.get()
    global gender
    try:
        if r == 0:
            gender = "Male"
        if r == 1:
            gender = "Female"
    except:
        messagebox.showinfo("", "Please enter your gender")

    mydb = mysql.connector.connect(host="localhost", user="root",
                                   password="@LEELadhar2719", database="BMS")
    mycursor = mydb.cursor()
    sql = "insert into studentlogin values(%s, %s);"
    sql1 = [(uname, password)]
    sql2 = "insert into student values(%s, %s, %s, %s, %s, %s, %s);"
    sql3 = [(name, uname, address, email, registrationno, mobileno, gender)]
    if len(name) != 0 or len(userid) != 0 or len(address) != 0 or len(email) != 0 or len(registrationno) != 0 or len(
            mobileno) != 0 or len(uname) != 0 or len(password2) != 0 or len(password) != 0:
        if password2 == password and uname == userid:
            try:
                mycursor.executemany(sql, sql1)
                mydb.commit()
                mycursor.executemany(sql2, sql3)
                mydb.commit()
                messagebox.showinfo("", "Details stored \n Now you can click on login")
            except:
                messagebox.showinfo("", "Incorrect Details")
        else:
            messagebox.showinfo("", "Passwords must be same")
    else:
        messagebox.showinfo("", "Entry Fields must not be empty!")


def New_User(self, BMS, root, StudentBeforeLogin):
    fr = Frame(root, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    title = Label(fr, text="New User", bg="light grey", fg="black", bd=15,
                  font=("times new roman", 15, "bold"))
    title.place(x=570, y=0)
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global v1
    l1 = Label(fr, text="Name :", fg="black",
               font=("times new roman", 12, "bold"))
    l1.place(x=200, y=200)
    e1 = Entry(fr, width=20)
    e1.place(x=300, y=203)
    l2 = Label(fr, text="User ID :", fg="black",
               font=("times new roman", 12, "bold"))
    l2.place(x=200, y=250)
    e2 = Entry(fr, width=20)
    e2.place(x=300, y=250)
    l3 = Label(fr, text="Address :", fg="black",
               font=("times new roman", 12, "bold"))
    l3.place(x=200, y=300)
    e3 = Entry(fr, width=30)
    e3.place(x=300, y=303)
    l4 = Label(fr, text="E-Mail :", fg="black",
               font=("times new roman", 12, "bold"))
    l4.place(x=200, y=350)
    e4 = Entry(fr, width=20)
    e4.place(x=300, y=353)
    l5 = Label(fr, text="Mobile.No :", fg="black",
               font=("times new roman", 12, "bold"))
    l5.place(x=700, y=200)
    e5 = Entry(fr, width=20)
    e5.place(x=800, y=203)
    l7 = Label(fr, text="Registration.No :", fg="black",
               font=("times new roman", 12, "bold"))
    l7.place(x=700, y=250)
    e6 = Entry(fr, width=20)
    e6.place(x=850, y=253)
    l6 = Label(fr, text="Gender :", fg="black",
               font=("times new roman", 12, "bold"))
    l6.place(x=700, y=300)
    v1 = IntVar()
    Radiobutton(width=10, text="Male", variable=v1, value=0, command=gen).place(x=800, y=388)
    Radiobutton(width=10, text="Female", variable=v1, value=1, command=gen).place(x=900, y=388)
    b5 = Button(fr, text="Exit", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"), command=lambda: BMS(root))
    b2 = Button(fr, text="Next", height=2, width=7, bg="light grey",
                font=("times new roman", 12, "bold"),
                command=lambda: Create_Password(self, BMS, root, StudentBeforeLogin))
    b2.place(x=700, y=350)
    b5.place(x=800, y=350)


def gen():
    global r
    r = v1.get()


def Create_Password(self, BMS, root, StudentBeforeLogin):
    fr = Frame(root, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    title = Label(fr, text="Create Your Password", bg="light grey", fg="black", bd=15,
                  font=("times new roman", 15, "bold"))
    title.place(x=500, y=0)
    global e11
    global e12
    global e13
    l1 = Label(fr, text="Create New Password :", fg="black",
               font=("times new roman", 10, "bold"))
    l1.place(x=385, y=201)
    e13 = Entry(fr, width=20)
    e13.place(x=550, y=203)
    l2 = Label(fr, text="Confirm Your Password :", fg="black",
               font=("times new roman", 10, "bold"))
    l2.place(x=385, y=251)
    e12 = Entry(fr, width=20)
    e12.place(x=550, y=253)
    l3 = Label(fr, text="Confirm Your User ID :", fg="black",
               font=("times new roman", 10, "bold"))
    l3.place(x=385, y=151)
    e11 = Entry(fr, width=20)
    e11.place(x=550, y=153)
    b1 = Button(fr, text="Submit", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"), command=insert)
    b1.place(x=400, y=300)
    b2 = Button(fr, text="Login", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"), command=StudentBeforeLogin)
    b2.place(x=525, y=300)
    b3 = Button(fr, text="Back", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"), command=lambda: New_User(self, BMS, root, StudentBeforeLogin))
    b3.place(x=650, y=300)

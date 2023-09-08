import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


def Aok(self, root, StudentBeforeLogin, BMS):
    global uname
    mydb = mysql.connector.connect(host="localhost", user="root",
                                   password="@LEELadhar2719", database="BMS")
    mycursor = mydb.cursor()
    uname = e.get()
    sql = "select * from adminstrator where user_name = %s; "
    mycursor.execute(sql, [uname])
    results = mycursor.fetchall()
    if results:
        ACreate_Password(self, root, StudentBeforeLogin, BMS)
        return True
    else:
        if len(uname) == 0:
            messagebox.showinfo("", "Enter your username")
        else:
            messagebox.showinfo("", "User name not found")
        return False


def AForget_Your_Password(self, root, StudentBeforeLogin, BMS):
    fr = Frame(root, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    title = Label(fr, text="Forget Your Password", bg="light grey", fg="black", bd=17,
                  font=("times new roman", 15, "bold"))
    title.place(x=570, y=0)
    global e
    l1 = Label(fr, text="USERNAME :", fg="black",
               font=("times new roman", 12, "bold"))
    l1.place(x=500, y=150)
    e = Entry(fr, width=20)
    e.place(x=620, y=153)
    b1 = Button(fr, text="Create a Password", height=2, width=15, bg="light grey",
                font=("times new roman", 12, "bold"), command=lambda: Aok(self, root, StudentBeforeLogin, BMS))
    b1.place(x=400, y=350)
    b4 = Button(fr, text="BACK", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"),
                command=lambda: StudentBeforeLogin(self, root, BMS))
    b4.place(x=800, y=350)


def Aupdate():
    mydb = mysql.connector.connect(host="localhost", user="root",
                                   password="@LEELadhar2719", database="BMS")
    global password
    password1 = e1.get()
    password2 = e2.get()
    if password1 == password2:
        password = password1
    mycursor = mydb.cursor()
    sql = "update adminstrator set password = %s where user_name = %s;"
    try:
        mycursor.execute(sql, [password, uname])
        mydb.commit()
        messagebox.showinfo("", "Password changed Successfully")
    except:
        messagebox.showinfo("", "Enter a valid password")


def ACreate_Password(self, root, StudentBeforeLogin, BMS):
    fr = Frame(root, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    title = Label(fr, text="Create Your Password", bg="light grey", fg="black", bd=17,
                  font=("times new roman", 15, "bold"))
    title.place(x=570, y=0)
    global e1
    global e2
    l1 = Label(fr, text="Create New Password :", fg="black",
               font=("times new roman", 10, "bold"))
    l1.place(x=500, y=201)
    e1 = Entry(fr, width=20)
    e1.place(x=665, y=203)
    l2 = Label(fr, text="Confirm Your Password :", fg="black",
               font=("times new roman", 10, "bold"))
    l2.place(x=500, y=251)
    e2 = Entry(fr, width=20)
    e2.place(x=665, y=253)
    b1 = Button(fr, text="Update Your new password", height=2, width=20, bg="light grey",
                font=("times new roman", 12, "bold"), command=Aupdate)
    b1.place(x=500, y=300)
    b2 = Button(fr, text="Login", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"),
                command=lambda: StudentBeforeLogin(self, root, BMS))
    b2.place(x=700, y=300)

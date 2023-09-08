import mysql.connector
from AdminLogin import *
from PIL import ImageTk, Image


def ok(self, root, StudentBeforeLogin):
    global uname
    mydb = mysql.connector.connect(host="localhost", user="root",
                                   password="@LEELadhar2719", database="BMS")
    mycursor = mydb.cursor()
    uname = e.get()
    sql = "select * from studentlogin where uname = %s; "
    mycursor.execute(sql, [uname])
    results = mycursor.fetchall()
    if results:
        Create_Password(self, root, StudentBeforeLogin)
        return True
    else:
        if len(uname) == 0:
            messagebox.showinfo("", "Enter your username")
        else:
            messagebox.showinfo("", "User name not found")
        return False


def Forget_Your_Password(self, root, StudentBeforeLogin):
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
                font=("times new roman", 12, "bold"), command=lambda: ok(self, root, StudentBeforeLogin))
    b1.place(x=400, y=350)
    b4 = Button(fr, text="BACK", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"), command=StudentBeforeLogin)
    b4.place(x=800, y=350)


def update():
    mydb = mysql.connector.connect(host="localhost", user="root",
                                   password="@LEELadhar2719", database="BMS")
    global password
    password1 = e1.get()
    password2 = e2.get()
    if password1 == password2:
        password = password1
    mycursor = mydb.cursor()
    sql = "update studentlogin set password = %s where uname = %s;"
    try:
        mycursor.execute(sql, [password, uname])
        messagebox.showinfo("", "Password changed Successfully")
        mydb.commit()
    except:
        messagebox.showinfo("", "Enter a valid password")


def Create_Password(self, root, StudentBeforeLogin):
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
                font=("times new roman", 12, "bold"), command=update)
    b1.place(x=500, y=300)
    b2 = Button(fr, text="Login", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"), command=StudentBeforeLogin)
    b2.place(x=700, y=300)

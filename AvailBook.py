from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image


def issued(uname, Title):
    s = ()
    reg = 0
    bid = 0
    mydb = mysql.connector.connect(host="localhost", user="root",
                                   password="@LEELadhar2719", database="BMS")
    mycursor = mydb.cursor()
    sql = "select registrationno from student where userid = %s;"
    mycursor.execute(sql, [uname])
    for i in mycursor:
        s = i
    for l0 in s:
        reg = l0
    sql1 = "select bookid from books where booktitle = %s;"
    mycursor.execute(sql1, [Title])
    for i in mycursor:
        s = i
    for l0 in s:
        bid = l0
    sql2 = "insert into booksissued values (%s, %s);"
    sql3 = [bid, reg]
    mycursor.execute(sql2, sql3)
    s = ()
    sql4 = "select * from books where bookid = %s;"
    mycursor.execute(sql4, [bid])
    for i in mycursor:
        s = i
    sql5 = "insert into booksissuedtostudents values(%s, %s, %s, %s, %s, %s);"
    sql6 = [s[0], reg, s[1], s[2], s[3], s[4]]
    mycursor.execute(sql5, sql6)
    mydb.commit()


def Avail(self, root, uname, StudentAfterLogin):
    Title = e1.get()
    mydb = mysql.connector.connect(host="localhost", user="root",
                                   password="@LEELadhar2719", database="BMS")
    mycursor = mydb.cursor()
    sql = "update books set bookstatus = %s where booktitle = %s;"
    status = "Issued"
    if len(Title) != 0:
        sql1 = "select bookstatus from books where booktitle = %s;"
        mycursor.execute(sql1, [Title])
        s1 = ()
        for j in mycursor:
            s1 = j
        if s1[0] == 'Available':
            mycursor.execute(sql, [status, Title])
            mydb.commit()
            issued(uname, Title)
            Avail_book(self, root, uname, StudentAfterLogin)
            mydb.commit()
            messagebox.showinfo("", "Book issued")
        else:
            messagebox.showinfo("", "Book is already issued to someone")
    else:
        messagebox.showinfo("", "Enter book title")


def Avail_book(self, root, uname, StudentAfterLogin):
    fr = Frame(root, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    global e1
    title = Label(fr, text="Avail Book", bg="light grey", fg="black", bd=15,
                  font=("times new roman", 15, "bold"))
    title.place(x=570, y=0)
    frame = Frame(fr, width=400, height=350, background="dark slate grey")
    frame.place(x=450, y=100)
    l1 = Label(frame, text="Enter Book Title :", fg="black", font=("times new roman", 10, "bold"))
    l1.place(x=70, y=30)
    e1 = Entry(frame, width=20)
    e1.place(x=210, y=32)
    b1 = Button(frame, text="Avail", height=2, width=9, bg="light grey",
                font=("times new roman", 12, "bold"), command=lambda: Avail(self, root, uname, StudentAfterLogin))
    b1.place(x=155, y=130)
    b2 = Button(fr, text="Back", height=2, width=9, bg="light grey",
                font=("times new roman", 12, "bold"), command=StudentAfterLogin)
    b2.place(x=600, y=350)

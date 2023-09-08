from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image


def ok(uname):
    mydb = mysql.connector.connect(host="localhost", user="root",
                                   password="@LEELadhar2719", database="BMS")
    mycursor = mydb.cursor()
    sql = "select registrationno from student where userid = %s;"
    mycursor.execute(sql, [uname])
    s = ()
    reg = 0
    for i in mycursor:
        s = i
    for l0 in s:
        reg = l0
    booktitle = e.get()
    bookauthor = f.get()
    sql1 = "insert into booksuggetions values (%s, %s, %s);"
    sql2 = [reg, booktitle, bookauthor]
    if len(bookauthor) != 0 and len(booktitle) != 0:
        mycursor.execute(sql1, sql2)
        mydb.commit()
        messagebox.showinfo("", "Book suggested")
    else:
        messagebox.showinfo("", "Enter bookauthor name or book title")


def Book_Suggestions(self, root, uname, StudentAfterLogin):
    fr = Frame(root, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    global e
    global f
    title = Label(fr, text="SUGGEST A BOOK", bg="light grey", fg="black", bd=15,
                  font=("times new roman", 15, "bold"))
    title.place(x=570, y=2)
    frame = Frame(fr, width=400, height=350, background="dark slate grey")
    frame.place(x=450, y=100)
    l1 = Label(frame, text="BOOK TITLE :", fg="black", font=("times new roman", 10, "bold"))
    l1.place(x=70, y=30)
    l2 = Label(frame, text="BOOK AUTHOR :", fg="black",
               font=("times new roman", 10, "bold"))
    l2.place(x=70, y=80)
    e = Entry(frame, width=20)
    e.place(x=210, y=32)
    f = Entry(frame, width=20)
    f.place(x=210, y=82)
    b1 = Button(frame, text="SUBMIT", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"), command=lambda: ok(uname))
    b1.place(x=155, y=130)
    b2 = Button(fr, text="BACK", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"), command=StudentAfterLogin)
    b2.place(x=600, y=350)

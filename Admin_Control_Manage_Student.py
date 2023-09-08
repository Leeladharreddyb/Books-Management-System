import mysql.connector
from Viewbooks import *
from tkinter import messagebox
from PIL import ImageTk, Image


def ok2():
    reg = e8.get()
    mydb = mysql.connector.connect(host="localhost", user="root",
                                   password="@LEELadhar2719", database="BMS")
    mycursor = mydb.cursor()
    sql = "delete from student where registrationno = %s;"
    if len(reg) != 0:
        try:
            mycursor.execute(sql, [reg])
            mydb.commit()
        except:
            messagebox.showinfo("", "User Doesn't exists")
    else:
        messagebox.showinfo("", "Enter Registration Number")


def ok3():
    reg = e6.get()
    title1 = e7.get()
    bid = 0
    s = ()
    mydb = mysql.connector.connect(host="localhost", user="root",
                                   password="@LEELadhar2719", database="BMS")
    mycursor = mydb.cursor()
    try:
        if len(title1) != 0 and len(reg) != 0:
            sql1 = "select bookid from books where booktitle = %s;"
            mycursor.execute(sql1, [title1])
            for i in mycursor:
                s = i
            for l0 in s:
                bid = l0
            sql2 = "select bookstatus from books where booktitle = %s;"
            mycursor.execute(sql2, [title1])
            global status1
            for i in mycursor:
                status1 = i
            if status1[0] == 'Available':
                sql = "update books set bookstatus = %s where booktitle = %s;"
                status2 = "Issued"
                mycursor.execute(sql, [status2, title1])
                mydb.commit()
                sql3 = "select * from books where bookid= %s;"
                mycursor.execute(sql3, [bid])
                global book
                for m in mycursor:
                    book = m
                sql5 = "insert into booksissuedtostudents values(%s, %s, %s, %s, %s, %s);"
                sql6 = [book[0], reg, book[1], book[2], book[3], book[4]]
                mycursor.execute(sql5, sql6)
                mydb.commit()
                sql8 = "insert into booksissued values (%s, %s);"
                sql9 = [bid, reg]
                mycursor.execute(sql8, sql9)
                mydb.commit()
                messagebox.showinfo("", "Book issued")
            else:
                messagebox.showinfo("", "Book is already issued to someone")
        else:
            messagebox.showinfo("", "Title cannot be empty")
    except:
        messagebox.showinfo("", "Book or user is not available")


def Manage_Students(self, root, Admin_After_Login, BMS):
    fr = Frame(root, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    title = Label(fr, text="Manage Students", bg="light grey", fg="black", bd=15,
                  font=("times new roman", 15, "bold"))
    title.place(x=570, y=0)
    frame = Frame(fr, width=400, height=350, background="dark slate grey")
    frame.place(x=450, y=100)
    b2 = Button(frame, text="Delete Existing Student", height=2, width=19, bg="light grey",
                font=("times new roman", 12, "bold"),
                command=lambda: Delete_Student(self, root, Admin_After_Login, BMS))
    b2.place(x=110, y=60)
    b3 = Button(frame, text="Issue a book to a Student", height=2, width=19, bg="light grey",
                font=("times new roman", 12, "bold"),
                command=lambda: Issue_Book_To_Student(self, root, Admin_After_Login, BMS))
    b3.place(x=110, y=140)
    b5 = Button(frame, text="Books issued to students", height=2, width=19, bg="light grey",
                font=("times new roman", 12, "bold"),
                command=lambda: View_Books_issued_to_students(self, root, Manage_Students, Admin_After_Login, BMS))
    b5.place(x=110, y=220)
    b4 = Button(fr, text="BACK", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"), command=lambda: Admin_After_Login(self, root, BMS))
    b4.place(x=610, y=500)


def Issue_Book_To_Student(self, root, Admin_After_Login, BMS):
    fr = Frame(root, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    title = Label(fr, text="Issue Books", bg="light grey", fg="black", bd=15,
                  font=("times new roman", 15, "bold"))
    title.place(x=570, y=0)
    global e6
    global e7
    frame = Frame(fr, width=400, height=350, background="dark slate grey")
    frame.place(x=450, y=100)
    l1 = Label(frame, text="Student Reg-no :", fg="black",
               font=("times new roman", 12, "bold"))
    l1.place(x=50, y=50)
    e6 = Entry(frame, width=20)
    e6.place(x=200, y=53)
    l2 = Label(frame, text="Book Title :", fg="black",
               font=("times new roman", 12, "bold"))
    l2.place(x=50, y=100)
    e7 = Entry(frame, width=20)
    e7.place(x=200, y=103)
    b1 = Button(frame, text="ISSUE", height=1, width=6, bg="light grey",
                font=("times new roman", 12, "bold"), command=ok3)
    b1.place(x=150, y=300)
    b4 = Button(fr, text="BACK", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"),
                command=lambda: Manage_Students(self, root, Admin_After_Login, BMS))
    b4.place(x=610, y=500)


def Delete_Student(self, root, Admin_After_Login, BMS):
    fr = Frame(root, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    title = Label(fr, text="Issue Books", bg="light grey", fg="black", bd=15,
                  font=("times new roman", 15, "bold"))
    title.place(x=570, y=0)
    frame = Frame(fr, width=400, height=250, background="dark slate grey")
    frame.place(x=450, y=100)
    global e8
    l1 = Label(frame, text="Student Reg-no :", fg="black",
               font=("times new roman", 12, "bold"))
    l1.place(x=50, y=50)
    e8 = Entry(frame, width=20)
    e8.place(x=200, y=53)
    b1 = Button(frame, text="DELETE", height=1, width=6, bg="light grey",
                font=("times new roman", 12, "bold"), command=ok2)
    b1.place(x=150, y=300)
    b4 = Button(fr, text="BACK", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"),
                command=lambda: Manage_Students(self, root, Admin_After_Login, BMS))
    b4.place(x=610, y=500)

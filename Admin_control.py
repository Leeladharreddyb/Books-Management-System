from Admin_Control_Manage_Student import *
import mysql.connector


def ok():
    a = e1.get()
    b = e2.get()
    c = e3.get()
    d = e4.get()
    e = e5.get()
    global b6
    mydb = mysql.connector.connect(host="localhost", user="root",
                                   password="@LEELadhar2719", database="BMS")
    mycursor = mydb.cursor()
    try:
        sql1 = "delete from booksuggetions where booktitle = %s;"
        mycursor.execute(sql1, [b])
        mydb.commit()
    except:
        b6 = b
    entries = [a, b, c, d, e]
    sql = "insert into books values (%s, %s, %s, %s, %s);"
    try:
        if len(a) != 0 or len(b) != 0 or len(c) != 0 or len(d) != 0 or len(e) != 0:
            try:
                mycursor.execute(sql, entries)
                mydb.commit()
                messagebox.showinfo("", "Book Added Successfully")
            except:
                messagebox.showinfo("", "Book is already present")
        else:
            messagebox.showinfo("", "All Fields are mandatory")
    except:
        messagebox.showinfo("", "Please try After some time")


def ok2():
    title = en.get()
    mydb = mysql.connector.connect(host="localhost", user="root",
                                   password="@LEELadhar2719", database="BMS")
    mycursor = mydb.cursor()
    try:
        sql1 = "select bookstatus from books where booktitle = %s;"
        mycursor.execute(sql1, [title])
    except:
        messagebox.showinfo("", "Book is not Available")
    global status
    for i in mycursor:
        status = i
    sql = "delete from books where booktitle = %s;"
    try:
        if status[0] == 'Available':
            if len(title) != 0:
                mycursor.execute(sql, [title])
                mydb.commit()
                messagebox.showinfo("", "Book Deleted Successfully")
            else:
                messagebox.showinfo("", "Fields must not be empty")
        else:
            messagebox.showinfo("", "Book issued to someone")
    except:
        messagebox.showinfo("", "Please try After some time")


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


def Manage_Books(self, root, Admin_After_Login, BMS):
    fr = Frame(root, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    title = Label(fr, text="Manage Books", bg="light grey", fg="black", bd=15,
                  font=("times new roman", 15, "bold"))
    title.place(x=570, y=0)
    frame = Frame(fr, width=400, height=350, background="dark slate grey")
    frame.place(x=450, y=100)
    b4 = Button(fr, text="BACK", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"), command=lambda: Admin_After_Login(self, root, BMS))
    b4.place(x=610, y=500)
    b1 = Button(frame, text="Add A book", height=2, width=10, bg="light grey",
                font=("times new roman", 12, "bold"), command=lambda: Add_Book(self, root, Admin_After_Login, BMS))
    b1.place(x=150, y=40)
    b2 = Button(frame, text="Delete Book", height=2, width=10, bg="light grey",
                font=("times new roman", 12, "bold"), command=lambda: Delete_Book(self, root, Admin_After_Login, BMS))
    b2.place(x=150, y=120)
    b3 = Button(frame, text="Issue a book to a Student", height=2, width=19, bg="light grey",
                font=("times new roman", 12, "bold"),
                command=lambda: Issue_Book_To_Student(self, root, Admin_After_Login, BMS))
    b3.place(x=110, y=200)
    b5 = Button(frame, text="Books issued to students", height=2, width=19, bg="light grey",
                font=("times new roman", 12, "bold"),
                command=lambda: View_Books_issued_to_students(self, root, Manage_Books, Admin_After_Login, BMS))
    b5.place(x=110, y=280)


def Add_Book(self, root, Admin_After_Login, BMS):
    fr = Frame(root, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    title = Label(fr, text="Add Books", bg="light grey", fg="black", bd=15,
                  font=("times new roman", 15, "bold"))
    title.place(x=570, y=0)
    frame = Frame(fr, width=400, height=350, background="dark slate grey")
    frame.place(x=450, y=100)
    global e1
    global e2
    global e3
    global e4
    global e5
    l1 = Label(frame, text="Book Id :", fg="black",
               font=("times new roman", 12, "bold"))
    l1.place(x=50, y=50)
    e1 = Entry(frame, width=20)
    e1.place(x=200, y=53)
    l2 = Label(frame, text="Book Title :", fg="black",
               font=("times new roman", 12, "bold"))
    l2.place(x=50, y=100)
    e2 = Entry(frame, width=20)
    e2.place(x=200, y=103)
    l3 = Label(frame, text="Book Author :", fg="black",
               font=("times new roman", 12, "bold"))
    l3.place(x=50, y=150)
    e3 = Entry(frame, width=30)
    e3.place(x=200, y=153)
    l4 = Label(frame, text="Book Status :", fg="black",
               font=("times new roman", 12, "bold"))
    l4.place(x=50, y=200)
    e4 = Entry(frame, width=20)
    e4.place(x=200, y=203)
    l5 = Label(frame, text="Book Price :", fg="black",
               font=("times new roman", 12, "bold"))
    l5.place(x=50, y=250)
    e5 = Entry(frame, width=20)
    e5.place(x=200, y=253)
    b1 = Button(frame, text="ADD", height=1, width=6, bg="light grey",
                font=("times new roman", 12, "bold"), command=ok)
    b1.place(x=150, y=300)
    b4 = Button(fr, text="BACK", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"), command=lambda: Manage_Books(self, root, Admin_After_Login, BMS))
    b4.place(x=610, y=500)


def Delete_Book(self, root, Admin_After_Login, BMS):
    fr = Frame(root, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    title = Label(fr, text="Add Books", bg="light grey", fg="black", bd=15,
                  font=("times new roman", 15, "bold"))
    title.place(x=570, y=0)
    frame = Frame(fr, width=400, height=350, background="dark slate grey")
    frame.place(x=450, y=100)
    global en
    l1 = Label(frame, text="Enter Book Title To delete :", fg="black",
               font=("times new roman", 12, "bold"))
    l1.place(x=50, y=50)
    en = Entry(frame, width=20)
    en.place(x=250, y=53)
    b1 = Button(frame, text="DELETE", height=1, width=6, bg="light grey",
                font=("times new roman", 12, "bold"), command=ok2)
    b1.place(x=150, y=300)
    b4 = Button(fr, text="BACK", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"), command=lambda: Manage_Books(self, root, Admin_After_Login, BMS))
    b4.place(x=610, y=500)


def Issue_Book_To_Student(self, root, Admin_After_Login, BMS):
    fr = Frame(root, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    title = Label(fr, text="Add Books", bg="light grey", fg="black", bd=15,
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
                font=("times new roman", 12, "bold"), command=lambda: Manage_Books(self, root, Admin_After_Login, BMS))
    b4.place(x=610, y=500)

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql

mypass = "root"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root", password='@LEELadhar2719', database='BMS')
cur = con.cursor()

bookTable = "books"


def View(self, root2, BMS):
    fr = Frame(root2, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    headingFrame1 = Frame(fr, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.13, rely=0.05, relwidth=0.2, relheight=0.06)
    headingFrame1.place(x=335, y=50)

    headingLabel = Label(headingFrame1, text="Books Available", bg='dark slate grey', fg='white',
                         font=('Courier', 10))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(fr, bg='dark slate grey')
    labelFrame.place(x=400, y=150, height=350, width=475)
    y = 0.25

    Label(labelFrame, text="%-20s%-35s%-30s%-20s%-20s" % ('BID', 'Title', 'Author', 'Status', 'Price'),
          bg='dark slate grey', fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------------",
          bg='dark slate grey',
          fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select * from " + bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-20s%-30s%-30s%-25s%-20s" % (i[0], i[1], i[2], i[3], i[4]), bg='dark slate grey',
                  fg='white').place(
                relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo(" ", "Failed to fetch files from database")

    quitBtn = Button(fr, text="Back", bg='#f7f1e3', fg='black', command=lambda: BMS(self))
    quitBtn.place(x=550, y=530, height=30, width=100)


def ViewS(self, root2, StudentAfterLogin):
    fr = Frame(root2, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    headingFrame1 = Frame(fr, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.13, rely=0.05, relwidth=0.2, relheight=0.06)
    headingFrame1.place(x=335, y=50)

    headingLabel = Label(headingFrame1, text="Books Available", bg='dark slate grey', fg='white',
                         font=('Courier', 10))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(fr, bg='dark slate grey')
    labelFrame.place(x=400, y=150, height=350, width=475)
    y = 0.25

    Label(labelFrame, text="%-20s%-35s%-30s%-20s%-20s" % ('BID', 'Title', 'Author', 'Status', 'Price'),
          bg='dark slate grey', fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------------",
          bg='dark slate grey',
          fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select * from " + bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-20s%-30s%-30s%-25s%-20s" % (i[0], i[1], i[2], i[3], i[4]), bg='dark slate grey',
                  fg='white').place(
                relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo(" ", "Failed to fetch files from database")

    quitBtn = Button(fr, text="Back", bg='#f7f1e3', fg='black', command=StudentAfterLogin)
    quitBtn.place(x=550, y=530, height=30, width=100)


def ViewA(self, root2, Admin_After_Login, BMS):
    fr = Frame(root2, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    headingFrame1 = Frame(fr, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.13, rely=0.05, relwidth=0.2, relheight=0.06)
    headingFrame1.place(x=335, y=50)

    headingLabel = Label(headingFrame1, text="Books Available", bg='dark slate grey', fg='white',
                         font=('Courier', 10))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(fr, bg='dark slate grey')
    labelFrame.place(x=400, y=150, height=350, width=475)
    y = 0.25

    Label(labelFrame, text="%-20s%-35s%-30s%-20s%-20s" % ('BID', 'Title', 'Author', 'Status', 'Price'),
          bg='dark slate grey', fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------------",
          bg='dark slate grey',
          fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select * from " + bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-20s%-30s%-30s%-25s%-20s" % (i[0], i[1], i[2], i[3], i[4]), bg='dark slate grey',
                  fg='white').place(
                relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo(" ", "Failed to fetch files from database")

    quitBtn = Button(fr, text="Back", bg='#f7f1e3', fg='black', command=lambda: Admin_After_Login(self, root2, BMS))
    quitBtn.place(x=550, y=530, height=30, width=100)


def View_Students(self, root2, Admin_After_Login, BMS):
    fr = Frame(root2, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    headingFrame1 = Frame(fr, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.13, rely=0.05, relwidth=0.2, relheight=0.06)
    headingFrame1.place(x=335, y=0)

    headingLabel = Label(headingFrame1, text="Total Students", bg='dark slate grey', fg='white',
                         font=('Courier', 10))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(fr, bg='dark slate grey')
    labelFrame.place(x=225, y=85, height=400, width=800)
    y = 0.25

    Label(labelFrame,
          text="%-40s%-40s%-40s%-50s%-20s" % (
              'Name', 'UserId', 'Reg-No', 'Mobile-No', 'Gender'),
          bg='dark slate grey', fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame,
          text="-------------------------------------------------------------------------------------------------------"
               "----------------------------",
          bg='dark slate grey',
          fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select name,userid,registrationno,mobileno,gender from student;"
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-40s%-40s%-40s%-50s%-20s" % (i[0], i[1], i[2], i[3], i[4]),
                  bg='dark slate grey', fg='white').place(relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo(" ", "Failed to fetch files from database")

    quitBtn = Button(fr, text="Back", bg='#f7f1e3', fg='black', command=lambda: Admin_After_Login(self, root2, BMS))
    quitBtn.place(x=550, y=530, height=30, width=100)


def View_Books_issued_to_students(self, root2, Manage_Books, Admin_After_Login, BMS):
    fr = Frame(root2, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    headingFrame1 = Frame(fr, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.13, rely=0.05, relwidth=0.2, relheight=0.06)
    headingFrame1.place(x=335, y=0)

    headingLabel = Label(headingFrame1, text="Books issued to Students", bg='dark slate grey', fg='white',
                         font=('Courier', 10))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(fr, bg='dark slate grey')
    labelFrame.place(x=300, y=85, height=400, width=600)
    y = 0.25

    Label(labelFrame,
          text="%-40s%-40s%-50s%-20s" % (
              'Bookid', 'Reg-No', 'BookTitle', 'BookAuthor'),
          bg='dark slate grey', fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame,
          text="------------------------------------------------------------------------------------------------------",
          bg='dark slate grey',
          fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select bookid,registrationno,booktitle,bookauthor from booksissuedtostudents;"
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-40s%-40s%-50s%-20s" % (i[0], i[1], i[2], i[3]),
                  bg='dark slate grey', fg='white').place(relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo(" ", "Failed to fetch files from database")

    quitBtn = Button(fr, text="Back", bg='#f7f1e3', fg='black',
                     command=lambda: Manage_Books(self, root2, Admin_After_Login, BMS))
    quitBtn.place(x=550, y=530, height=30, width=100)

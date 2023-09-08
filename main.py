import mysql.connector
from NewUser import *
from ForgetYourPassword import *
from AvailBook import *
from SubmitBook import *
from BookSuggetions import *


class BMS:
    def __init__(self, roo):
        self.root = roo
        self.root.geometry("1920x1080")
        self.root.title("BMS")

        self.tit = Label(self.root, text="Books Management System", bg="dark slate grey", fg="white", bd=20,
                         font=("times new roman", 30, "bold"), padx=2, pady=6)
        self.tit.pack(side=TOP, fill=X)
        self.fr = Frame(self.root, width=1300, height=600)
        self.fr.place(x=0, y=95)
        self.img = ImageTk.PhotoImage(Image.open('i2.jpg'))
        self.im = Label(self.fr, image=self.img)
        self.im.pack(expand=True)
        self.title = Label(self.fr, text="HOME", bg="light grey", fg="black", bd=15,
                           font=("times new roman", 15, "bold"))
        self.title.place(x=600, y=5)
        self.b1 = Button(self.fr, width=17, height=2, text="STUDENT LOGIN", bg="grey", command=self.StudentBeforeLogin)
        self.b1.place(x=600, y=100)
        self.b2 = Button(self.fr, width=20, height=2, text="ADMINISTRATOR LOGIN", bg="grey",
                         command=lambda: Admin_Login(self.root, root, BMS))
        self.b2.place(x=600, y=200)
        self.b3 = Button(self.fr, width=12, height=2, text="NEW USER", bg="grey",
                         command=lambda: New_User(self.root, BMS, root, self.StudentBeforeLogin))
        self.b3.place(x=600, y=300)
        self.b4 = Button(self.fr, width=17, height=2, text="BOOKS AVAILABLE", bg="grey",
                         command=lambda: View(self.root, root, BMS))
        self.b4.place(x=600, y=400)
        self.b4 = Button(self.fr, width=10, height=2, text="EXIT", bg="grey", command=lambda: self.root.destroy())
        self.b4.place(x=600, y=500)

    def ok(self):
        global uname
        mydb = mysql.connector.connect(host="localhost", user="root",
                                       password="@LEELadhar2719", database="BMS")
        mycursor = mydb.cursor()
        uname = e.get()
        password = f.get()
        sql = "select * from studentlogin where uname = %s and password = %s; "
        mycursor.execute(sql, [uname, password])
        results = mycursor.fetchall()
        if results:
            self.StudentAfterLogin()
            return True
        else:
            if len(uname) == 0:
                messagebox.showinfo("", "Enter your credentials")
            else:
                messagebox.showinfo("", "Incorrect Username or Password")
            return False

    def StudentBeforeLogin(self):
        fr = Frame(self.root, width=1300, height=600)
        fr.place(x=0, y=95)
        self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
        self.im = Label(fr, image=self.img)
        self.im.pack()
        global e
        global f
        title = Label(fr, text="STUDENT LOGIN", bg="light grey", fg="black", bd=15,
                      font=("times new roman", 15, "bold"))
        title.place(x=570, y=5)
        frame = Frame(fr, width=400, height=350, background="dark slate grey")
        frame.place(x=450, y=100)
        l1 = Label(frame, text="USERNAME :", fg="black",
                   font=("times new roman", 12, "bold"))
        l1.place(x=70, y=30)
        l2 = Label(frame, text="PASSWORD :", fg="black",
                   font=("times new roman", 12, "bold"))
        l2.place(x=70, y=70)
        e = Entry(frame, width=20)
        e.place(x=200, y=32)
        f = Entry(frame, width=20, show='*')
        f.place(x=200, y=72)
        b1 = Button(frame, text="LOGIN", height=1, width=8, bg="light grey",
                    font=("times new roman", 12, "bold"), command=self.ok)
        b1.place(x=155, y=130)
        b2 = Button(frame, text="FORGET YOUR PASSWORD ?", height=1, width=25, bg="light grey",
                    font=("times new roman", 12, "bold"),
                    command=lambda: Forget_Your_Password(self.root, root, self.StudentBeforeLogin))
        b2.place(x=80, y=190)
        b3 = Button(frame, text="NEW USER", height=1, width=9, bg="light grey",
                    font=("times new roman", 12, "bold"),
                    command=lambda: New_User(self.root, BMS, root, self.StudentBeforeLogin))
        b3.place(x=155, y=250)
        b4 = Button(frame, text="BACK", height=1, width=8, bg="light grey",
                    font=("times new roman", 12, "bold"), command=lambda: BMS(root))
        b4.place(x=155, y=310)

    def StudentAfterLogin(self):
        fr = Frame(self.root, width=1300, height=600)
        fr.place(x=0, y=95)
        self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
        self.im = Label(fr, image=self.img)
        self.im.pack()
        username = uname
        tit = "Welcome " + username
        title = Label(fr, text=tit, bg="light grey", fg="black", bd=15,
                      font=("times new roman", 15, "bold"))
        title.place(x=570, y=5)
        frame = Frame(fr, width=400, height=430, background="dark slate grey")
        frame.place(x=66, y=150)
        b1 = Button(text="SUBMIT BOOK", height=2, width=12, bg="light grey",
                    font=("times new roman", 12, "bold"),
                    command=lambda: Submit_Book(self.root, root, uname, self.StudentAfterLogin))
        b1.place(x=100, y=300)
        b2 = Button(text="AVAIL BOOK", height=2, width=12, bg="light grey",
                    font=("times new roman", 12, "bold"),
                    command=lambda: Avail_book(self.root, root, username, self.StudentAfterLogin))
        b2.place(x=100, y=450)
        b4 = Button(text="SUGGEST A BOOK", height=2, width=15, bg="light grey",
                    font=("times new roman", 12, "bold"),
                    command=lambda: Book_Suggestions(self.root, root, uname, self.StudentAfterLogin))
        b4.place(x=300, y=300)
        b5 = Button(text="VIEW ALL BOOKS", height=2, width=15, bg="light grey",
                    font=("times new roman", 12, "bold"),
                    command=lambda: ViewS(self.root, root, self.StudentAfterLogin))
        b5.place(x=300, y=450)
        b6 = Button(text="EXIT", height=2, width=8, bg="light grey",
                    font=("times new roman", 12, "bold"), command=self.StudentBeforeLogin)
        b6.place(x=200, y=600)

        headingFrame1 = Frame(fr, bg="#FFBB00", bd=5)
        headingFrame1.place(relx=0.13, rely=0.05, relwidth=0.2, relheight=0.06)
        headingFrame1.place(x=600, y=100)

        headingLabel = Label(headingFrame1, text="Books Availed", bg='dark slate grey', fg='white',
                             font=('Courier', 10))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        labelFrame = Frame(fr, bg='dark slate grey')
        labelFrame.place(x=725, y=200, height=350, width=475)
        y = 0.25

        Label(labelFrame, text="%-20s%-35s%-30s%-20s%-20s" % ('BID', 'Title', 'Author', 'Status', 'Price'),
              bg='dark slate grey', fg='white').place(relx=0.07, rely=0.1)
        Label(labelFrame, text="----------------------------------------------------------------------------------",
              bg='dark slate grey',
              fg='white').place(relx=0.05, rely=0.2)
        sql = "select registrationno from student where userid = %s"
        s = ()
        reg = 0
        cur.execute(sql, uname)
        for i in cur:
            s = i
        for i in s:
            reg = i
        getBooks = '''select bookid,booktitle,bookauthor,bookstatus,bookprice from booksissuedtostudents 
        where registrationno = %s;'''
        try:
            cur.execute(getBooks, [reg])
            con.commit()
            for i in cur:
                Label(labelFrame, text="%-20s%-35s%-30s%-20s%-20s" % (i[0], i[1], i[2], i[3], i[4]),
                      bg='dark slate grey', fg='white').place(relx=0.07, rely=y)
                y += 0.1
        except:
            messagebox.showinfo("Failed to fetch files from database")


if __name__ == "__main__":
    root = Tk()
    win = BMS(root)
    root.mainloop()

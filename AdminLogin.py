import mysql.connector
from AForgetYourPassword import *
from Admin_control import *


def ok(self, root, BMS):
    global user_name
    mydb = mysql.connector.connect(host="localhost", user="root",
                                   password="@LEELadhar2719", database="BMS")
    mycursor = mydb.cursor()
    user_name = e.get()
    password = f.get()
    sql = "select * from adminstrator where user_name = %s and password = %s; "
    mycursor.execute(sql, [user_name, password])
    results = mycursor.fetchall()
    if results:
        Admin_After_Login(self, root, BMS)
        return True
    else:
        if len(user_name) == 0:
            messagebox.showinfo("", "Enter your credentials")
        else:
            messagebox.showinfo("", "Incorrect Username or Password")
        return False


def Admin_Login(self, root, BMS):
    fr = Frame(root, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    title = Label(fr, text="ADMIN LOGIN", bg="light grey", fg="black", bd=15,
                  font=("times new roman", 15, "bold"))
    title.place(x=570, y=0)
    global e
    global f
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
    b1 = Button(frame, text="LOGIN", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"), command=lambda: ok(self, root, BMS))
    b1.place(x=155, y=130)
    b2 = Button(frame, text="FORGET YOUR PASSWORD ?", height=2, width=25, bg="light grey",
                font=("times new roman", 12, "bold"),
                command=lambda: AForget_Your_Password(self, root, Admin_Login, BMS))
    b2.place(x=80, y=190)
    b4 = Button(frame, text="BACK", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"), command=lambda: BMS(root))
    b4.place(x=155, y=250)


def Admin_After_Login(self, root, BMS):
    fr = Frame(root, width=1300, height=600)
    fr.place(x=0, y=95)
    self.img = ImageTk.PhotoImage(Image.open('i1.jpg'))
    self.im = Label(fr, image=self.img)
    self.im.pack()
    tex = "Welcome" + " " + user_name
    title = Label(fr, text=tex, bg="light grey", fg="black", bd=15,
                  font=("times new roman", 15, "bold"))
    title.place(x=570, y=0)
    b4 = Button(fr, text="BACK", height=2, width=8, bg="light grey",
                font=("times new roman", 12, "bold"), command=lambda: Admin_Login(self, root, BMS))
    b4.place(x=800, y=500)
    headingFrame1 = Frame(fr, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.13, rely=0.05, relwidth=0.2, relheight=0.06)
    headingFrame1.place(x=0, y=50)

    headingLabel = Label(headingFrame1, text="Books Suggested", bg='dark slate grey', fg='white',
                         font=('Courier', 10))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(fr, bg='dark slate grey')
    labelFrame.place(x=110, y=150, height=350, width=375)
    y = 0.25

    Label(labelFrame, text="%-30s%-35s%-30s" % ('Student Reg.No', 'Title', 'Author'),
          bg='dark slate grey', fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="---------------------------------------------------------------",
          bg='dark slate grey',
          fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select * from booksuggetions"
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-30s%-35s%-30s" % (i[0], i[1], i[2]), bg='dark slate grey',
                  fg='white').place(relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo(" ", "Failed to fetch files from database")

    b1 = Button(fr, text="Total Students", height=2, width=15, bg="light grey",
                font=("times new roman", 12, "bold"), command=lambda: View_Students(self, root, Admin_After_Login, BMS))
    b1.place(x=800, y=400)
    b2 = Button(fr, text="Books Available", height=2, width=15, bg="light grey",
                font=("times new roman", 12, "bold"), command=lambda: ViewA(self, root, Admin_After_Login, BMS))
    b2.place(x=800, y=300)
    b3 = Button(fr, text="Manage Students", height=2, width=15, bg="light grey",
                font=("times new roman", 12, "bold"),
                command=lambda: Manage_Students(self, root, Admin_After_Login, BMS))
    b3.place(x=800, y=200)
    b5 = Button(fr, text="Manage Books", height=2, width=15, bg="light grey",
                font=("times new roman", 12, "bold"), command=lambda: Manage_Books(self, root, Admin_After_Login, BMS))
    b5.place(x=800, y=100)

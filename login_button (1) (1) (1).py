import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3


root=Tk()
root.geometry("200x100+0+0")
root.title("LMS")

class Library:
    def __init__(self,name,author,issue,password,abooks,amember,bname,btrans,submit,pub,id,cur,conn):
        self.name=name
        self.author=author
        self.issue=issue
        self.password=password
        self.abooks=abooks
        self.amember=amember
        self.bname=bname
        self.btrans=btrans
        self.submit=submit
        self.pub=pub
        self.id=id
        self.cur=cur
        self.conn=conn


    def  stafflogin(self):
        #root=Tk()
        #self.cur.execute("Create table login_home( name varchar,id integer primary key )")
        root.title("Login")
        title=Label(root,text="Please Enter your details")
        title.grid(row=0,columnspan=2)
        name=Label(root,text="Name")
        name.grid(row=1,column=0)
        self.name=Entry(root)
        self.name.grid(row=1,column=1,sticky=E)
        password=Label(root,text="Password")
        password.grid(row=2,column=0)

        self.password=Entry(root,show="*")
        self.password.grid(row=2,column=1)
        loginbutton=Button(root,text="LOGIN",command=self.books)
        loginbutton.grid(row=3,columnspan=2)
        #signuplabel=Button(root,text="Create A new account\nSign Up",command=self.new)
        #signuplabel.grid(row=4,columnspan=2)

    #def login_test(self):
        ##CHECK FROM DATABASE WHETHER THE ENTERED LOGIN ID AND PASSWORD ARE CORRECT OR NOT....
        ##IF CORRECT GOTO COMMAND=SELF.BOOKS
        ##ELSE RESET THE LOGIN FRAME


    def new(self):
        root=Tk()
        root.geometry("255x180+0+0")
        root.title("Member")
        #self.cur.execute("Create table new_details( name varchar,id integer primary key )")
        title=Label(root,text="Enter your Details")
        title.grid(row=0,column=1)
        name=Label(root,text="Name")
        name.grid(row=1,column=0)
        self.name=Entry(root)
        self.name.grid(row=1,column=1)
        id=Label(root,text="Id Number")
        id.grid(row=2,column=0)
        self.id=Entry(root)
        self.id.grid(row=2,column=1)
        submit=Button(root,text="Submit",command=self.insert_newdata)
        submit.grid(row=7,column=4)


    def insert_newdata(self):

        s1="insert into new_details(name,id)  values ('%s','%d')" %(self.name.get(),int(self.id.get()))
        self.cur.execute(s1)
        self.conn.commit()
        tkinter.messagebox.showinfo("Added","Successfully!!!!")
        self.view_mem()


    def  books(self):
        root = Tk()
        root.geometry("245x320+0+0")
        s5="select * from login_home"
        self.cur.execute(s5)
        rows=self.cur.fetchall()
        for row in rows:
            name=row[0]
            id=row[1]
            if(name==str(self.name.get()) and id==int(self.password.get())):
                tkinter.messagebox.showinfo("Library", "Logged in successfully")
                root.title("LMS")
                self.password.delete(0, 'end')
                #self.cur.execute("Create table book_details( name varchar,id integer primary key )")
                abooks=Button(root,text="ADD BOOKS",bg="black",fg="white",command=self.insertbook,height = 3, width = 15)
                abooks.grid(row=0,column=2,columnspan=2,padx=3,pady=3)
                author=Button(root,text="ADD AUTHOR",bg="black",fg="white",command=self.author_details,height = 3, width = 15)
                author.grid(row=1,column=2,columnspan=2,padx=3,pady=3)
                pub=Button(root,text="ADD PUBLISHER",bg="black",fg="white",command=self.pub_details,height = 3, width = 15)
                pub.grid(row=2,column=2,columnspan=2,padx=3,pady=3)
                amember=Button(root,text="ADD MEMBER",bg="black",fg="white",command=self.new,height = 3, width = 15)
                amember.grid(row=3,column=2,columnspan=2,padx=3,pady=3)
            #view books
                bookview=Button(root,text="VIEW BOOKS",bg="black",fg="yellow",command=self.view_books,height = 3, width = 15)
                bookview.grid(row=0,column=8,columnspan=2,padx=3,pady=3)
            #view authors
                authview=Button(root,text="VIEW AUTHORS",bg="black",fg="yellow",command=self.view_auth,height = 3, width = 15)
                authview.grid(row=1,column=8,columnspan=2,padx=3,pady=3)
            #view publishers
                pubview=Button(root,text="VIEW PUBLISHERS",bg="black",fg="yellow",command=self.view_pub,height = 3, width = 15)
                pubview.grid(row=2,column=8,columnspan=2,padx=3,pady=3)
            #view members
                memview=Button(root,text="VIEW MEMBERS",bg="black",fg="yellow",command=self.view_mem,height = 3, width = 15)
                memview.grid(row=3,column=8,columnspan=2,padx=3,pady=3)
            #book transaction
                btrans=Button(root,text="ISSUE BOOK",bg="black",fg="white",command=self.b_trans,height = 3, width = 15)
                btrans.grid(row=6,column=3,columnspan=3,padx=3,pady=3)
                issue=Button(root,text="VIEW ISSUED BOOKS",bg="black",fg="yellow",command=self.view_trans,height = 3, width = 15)
                issue.grid(row=6,column=6,columnspan=3,padx=3,pady=3)
            else:
                tkinter.messagebox.showinfo("Library", "Invalid ID ")
                self.name.delete(0, 'end')
                self.password.delete(0, 'end')

##Reurn book

    def author_details(self):
        root=Tk()
        root.geometry("255x180+0+0")
        root.title("Author")
        #self.cur.execute("Create table Adetails( name varchar,id integer primary key )")
        title=Label(root,text="Enter your Details")
        title.grid(row=0,column=2)
        name=Label(root, text="Name")
        name.grid(row=1,column=1)
        self.name=Entry(root)
        self.name.grid(row=1,column=2)
        id=Label(root,text="ID Number")
        id.grid(row=2,column=1)
        self.id=Entry(root)
        self.id.grid(row=2,column=2)
        submit=Button(root,text="Submit",command=self.insert_Adetails)
        submit.grid(row=7,column=4)

    def insert_Adetails(self):

        root.title("Author Entry")
        s1="insert into Adetails(name,id)  values ('%s','%d')" %(self.name.get(),int(self.id.get()))
        self.cur.execute(s1)
        self.conn.commit()
        tkinter.messagebox.showinfo("LMS","Added Successfully!")
        self.view_auth()





    def pub_details(self):
        root=Tk()
        root.geometry("255x180+0+0")
        root.title("Publisher")
        #self.cur.execute("Create table pub_details( name varchar,id integer primary key )")
        title=Label(root,text="Enter your Details")
        title.grid(row=0,column=2)
        name=Label(root,text="Name")
        name.grid(row=0,column=1)
        self.name=Entry(root)
        self.name.grid(row=0,column=2)
        id=Label(root,text="ID")
        id.grid(row=1,column=1)
        self.id=Entry(root)
        self.id.grid(row=1,column=2)
        submit=Button(root,text="Submit",command=self.insert_pubdata)
        submit.grid(row=7,column=4)






    def insert_pubdata(self):

        root.title("Pub Entry")
        s1="insert into pub_details(name,id)  values ('%s','%d')" %(self.name.get(),int(self.id.get()))
        self.cur.execute(s1)
        self.conn.commit()
        tkinter.messagebox.showinfo("LMS","Added Successfully!")
        self.view_pub()








    def view_books(self):
        root= Tk()
        root.geometry("255x180+0+0")
        root.title("Books")
        s2="select * from Books"
        self.cur.execute(s2)
        rows=self.cur.fetchall()
        i = 0
        #str4="ID name  Author"
        #li=Label(root,text=str4)
        #li.grid(row=0,column=1)
        for row in rows:
            id=row[0]
            name=row[1]
            author=row[3]
            pub=row[2]
            print(" ID \t\t Name\t\t\t Author\t\tPublisher\n",id,name,author,"\t",pub)
            #print("Name :\t ",name)
            #print("Author:\t ",author)
            str2=("ID :\t "+str(row[0])+" \t||  Name : \t"+str(row[1])+" \t||  Author :\t"+str(row[3])+" \t||  Publisher :\t"+str(row[2]))
            li2=Label(root,text="{0}".format(str(str2)))
            li2.grid(row=i,column=0)
            i=i+1

        #tframe=Frame(root)
        #tframe.pack(fill=X)
        #id=Label(tframe, text="ID",fg="red")
        #id.grid(row=1,column=1,columnspan=4)
        #bname=Label(tframe, text="Name",fg="red")
        #bname.grid(row=1,column=9,columnspan=10)
        #author=Label(tframe, text="Author Name",fg="red")
        #author.grid(row=1,column=20,columnspan=9)
        #name=Label(tframe, text="Publication",fg="red")
        #name.grid(row=1,column=33,columnspan=9)


    def view_auth(self):
        root= Tk()
        root.geometry("255x180+0+0")
        root.title("Authors")
       # tframe=Frame(root)
        #tframe.pack(fill=X)
        #id=Label(root, text="ID",fg="red")
        #id.grid(row=1,column=1,columnspan=4)
        #author=Label(root, text="Name",fg="red")
        #author.grid(row=1,column=9,columnspan=10)

        s2="select * from Adetails"
        self.cur.execute(s2)
        rows=self.cur.fetchall()
        i=0
        for row in rows:
            id=row[1]
            name=row[0]
            print(" ID \t Name\t\n",id,name)
            str3=("ID :\t "+str(row[1])+" \t|| Name :\t"+str(row[0]))
            li3=Label(root,text="{0}".format(str(str3)))
            li3.grid()
            i=i+1


    def view_pub(self):
        root= Tk()
        root.geometry("255x180+0+0")
        root.title("Publishers")
        #tframe=Frame(root)
        #tframe.pack(fill=X)
        #id=Label(tframe, text="ID",fg="red")
        #id.grid(row=1,column=1,columnspan=4)
        #name=Label(tframe, text="Name",fg="red")
        #name.grid(row=1,column=9,columnspan=10)

        s2="select * from pub_details"
        self.cur.execute(s2)
        rows=self.cur.fetchall()
        i=0
        for row in rows:
            id=row[1]
            name=row[0]
            print(" ID \t Name\t\n",id,name)
            str3=("ID :\t"+str(row[1])+" \t|| Name :\t"+str(row[0]))
            li3=Label(root,text="{0}".format(str(str3)))
            li3.grid()
            i=i+1


    def view_mem(self):
        root= Tk()
        root.geometry("255x180+0+0")
        root.title("Members")
       # tframe=Frame(root)
        #tframe.pack(fill=X)
        #id=Label(tframe, text="ID",fg="red")
        #id.grid(row=1,column=1,columnspan=4)
        #name=Label(tframe, text="Name",fg="red")
        #name.grid(row=1,column=9,columnspan=10)

        s2="select * from new_details"
        self.cur.execute(s2)
        rows=self.cur.fetchall()
        i=0
        for row in rows:
            id=row[1]
            name=row[0]
            print(" ID \t Name\t\n",id,name)
            #print("Name : ",name)
            str3=("ID :\t "+str(row[1])+" || Name :\t"+str(row[0]))
            li3=Label(root,text="{0}".format(str(str3)))
            li3.grid()
            i=i+1





    def b_trans(self):
        root=Tk()
        root.geometry("255x180+0+0")
        root.title("Issue")
        #self.cur.execute("Create table b_trans( name varchar,id integer primary key,m_id integer)")

        title=Label(root,text="Enter your Details")
        title.grid(row=0,column=2)
        id=Label(root,text="Transaction ID")
        id.grid(row=0,column=1)
        self.id=Entry(root)
        self.id.grid(row=0,column=2)
        bname=Label(root,text="BOOK ID")
        bname.grid(row=1,column=1)
        self.bname=Entry(root)
        self.bname.grid(row=1,column=2)
        amember=Label(root,text="MEMBER ID")
        amember.grid(row=2,column=1)
        self.amember=Entry(root)
        self.amember.grid(row=2,column=2)
        submit=Button(root,text="Submit",command=self.b_transdetails)
        submit.grid(row=7,column=4)


    def b_transdetails(self):

        root.title("Issue")
        s1="insert into b_trans(name,id,m_id)  values ('%s','%d','%d')" %(self.bname.get(),int(self.id.get()),int(self.amember.get()))
        self.cur.execute(s1)
        self.conn.commit()
        tkinter.messagebox.showinfo("LMS","Added Successfully!")
        self.view_trans()



    def view_trans(self):
        root= Tk()
        root.geometry("255x180+0+0")
        root.title("Issued")
       # tframe=Frame(root)
        #tframe.pack(fill=X)
        #id=Label(tframe, text="Transaction ID",fg="red")
        #id.grid(row=1,column=1,columnspan=4)
        #bname=Label(tframe, text="Book ID",fg="red")
        #bname.grid(row=1,column=9,columnspan=10)
        #name=Label(tframe, text="Member's ID",fg="red")
        #name.grid(row=1,column=20,columnspan=10)

        s2="select * from b_trans"
        self.cur.execute(s2)
        rows=self.cur.fetchall()
        i=0
        for row in rows:
            id=row[1]
            name=row[0]
            bname=row[2]
            print(" T_ID \t B_ID\t Mem_ID\n",id,"\t",name,"\t",bname)
            str3=("T_ID :\t "+str(row[1])+" \t|| B_ID :\t"+str(row[0])+"\t|| M_ID :\t"+str(row[2]))
            li3=Label(root,text="{0}".format(str(str3)))
            li3.grid()
            i=i+1




    def insertbook(self):
        root=Tk()
        root.geometry("255x180+0+0")
        root.title("Add Book")
        title=Label(root,text="ENTER BOOK DETAILS")
        title.grid(row=0,column=3)
        #ID
        id=Label(root,text="Book ID")
        id.grid(row=1,column=2)
        self.id=Entry(root)
        self.id.grid(row=1,column=3)
        #Name
        bname=Label(root,text="Name")
        bname.grid(row=2,column=2)
        self.bname=Entry(root)
        self.bname.grid(row=2,column=3)
        #publications
        abooks=Label(root,text="publications")
        abooks.grid(row=3,column=2)
        self.abooks=Entry(root)
        self.abooks.grid(row=3,column=3)
        #Author
        author=Label(root,text="Author")
        author.grid(row=4,column=2)
        self.author=Entry(root)
        self.author.grid(row=4,column=3)
        #price
        #price=Label(root,text="Price")
        #price.grid(row=5,column=2)
        #self.price=Entry(root)
        #self.price.grid(row=5,column=3)
        #submit
        submit=Button(root,text="Submit",command=self.insertdata)
        submit.grid(row=7,column=4)


    def insertdata(self):
        #self.cur.execute("create table Books(id integer primary key not null , name varchar not null , pub varchar , author varchar)")


        s4="insert into Books(id,name,pub,author)  values ('%d','%s','%s','%s')" %(int(self.id.get()),self.bname.get(),self.abooks.get(),self.author.get())
        self.cur.execute(s4)
        self.conn.commit()
        tkinter.messagebox.showinfo("LMS","Added Successfully!")
        self.view_books()


    def showbooks(self):
        s2="select * from Books"
        self.cur.execute(s2)
        rows=self.cur.fetchall()
        for row in rows:
            id=row[0]
            name=row[1]
            author=row[3]
            print("ID :",id)
            print("Name : ",name)
            print("Author: ",author)






    def addmember(self):
        root=Tk()
        root.geometry("255x180+0+0")
        title=Label(root,text="Add Details of new Member")
        title.grid()
        bname=Label(root,text="Name")
        bname.grid(row=2,column=1)





    def create_connection(self):
        self.conn = sqlite3.connect('LibraryMS')
        self.cur = self.conn.cursor()
        print('Connection created Successfully')
        #self.cur.execute("Create table login_home( name varchar,id integer primary key )")
        #s4="insert into login_home(name,id)values ('suyash',123)"#%(self.name.get(),int(self.password.get()))
        #self.cur.execute(s4)
        #self.conn.commit()

    def showinfo(self):
        s = "select *from login_home"
        self.cur.execute(s)
        self.conn.commit()
        rows = self.cur.fetchall()
        i=2
        for row in rows:
            name=row[0]
            id=row[1]
            print("Name:" +str(name) + " id:" + str(id))


    def create_table(self):
        s = "Create table Books(ID INT, Name TEXT,pub TEXT,Author TEXT)"
        self.cur.execute(s)
        self.conn.commit()
        tkinter.messagebox.showinfo("Books", "Table Created SuccessFully")

l=Library("a","b","c","d","e","g","h","i","j","k","l","m","n")



class Call:
   # Title=Label(root,text="label Management System\n\tLOGIN")
    #Title.grid(row=0,columnspan=2)
    l.stafflogin()
    #author=Button(root,text="Staff",command=l.stafflogin)
    #author.grid()
    #user=Button(root,text="Student",command=l.userlogin)
    #user.grid()
    #l.create_table()
    l.create_connection()
    #l.showinfo()

root.mainloop()








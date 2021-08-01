from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def bookRegisterAvail():

   
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = "Avail";
    
    
    
    insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(bid)
    print(title)
    print(author)
    print(status)


    root.destroy()


def issuer():

    global issen;
    root = Tk()
    root.title("Issuer Name")
    root.geometry("350x250")

    

    # isslb = Label(root,text="Status(Avail/Issued) : ", bg='black', fg='white', font=("Century 15"))
    # isslb.pack(anchor="center")


    issfr = Frame(root, bg="black", bd=5)
    issfr.place(relx=0.17,rely=0.1,relwidth=0.66,relheight=0.66)

    isslb = Label(issfr, text="Name of Issuer: ",  bg="black", fg ="white", font=("Century 15"))
    isslb.place(relx=.1, rely=.1, relwidth=.8, relheight=.2)

    issen = Entry(issfr, bg="black", fg="white", font=('Century 14'))
    issen.place(relx=.5, rely=.5, relwidth=.65, relheight=.23, anchor="center")

    btun = Button(root,text="Submit",bg='#1f1f1f', bd=7, fg='orange', cursor="hand2", font=('Courier',15), command=lambda:[((bookRegisterIssued())), root.destroy()])
    btun.place(relx=.5, rely=.65, relwidth=.4, relheight=.15, anchor="center")


    root.mainloop();

def bookRegisterIssued():
    

    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = "Issued";
    issueto = issen.get()

    insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+author+"','"+status+"')"
    insertBooks1 = "insert into "+issueTable+" values ('"+bid+"','"+issueto+"')"
    try:
        cur.execute(insertBooks)
        # cur.execute(insertBooks1)
        con.commit()
        cur.execute(insertBooks1)
        con.commit();
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(bid)
    print(title)
    print(author)
    print(status)


    root.destroy()

    

# def issuerName():
#     issuer();
    
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,issueTable,root, var, output
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.attributes('-fullscreen', True);

    # Add your own database name and password here to reflect in the code
    mypass = "rootpass"
    mydatabase="db"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()


    # Enter Table Names here
    bookTable = "books" # Book Table
    issueTable = "books_issued"

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#5d1818")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white', font=("Century 15"))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame, font=("Century 15"))
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.13)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white', font=("Century 15"))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame, font=("Century 15"))
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.13)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white', font=("Century 15"))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame, font=("Century 15"))
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.13)
        
    # Book Status
    lb4 = Label(labelFrame,text="Status(Avail/Issued) : ", bg='black', fg='white', font=("Century 15"))
    lb4.place(relx=0.05,rely=0.75, relheight=0.08)
    # rb1 = Radiobutton(labelFrame, text="Science", variable=var, value=1)
    # rb1.place(relx=0.05,rely=0.65, relheight=0.08)

 
    var = IntVar()
    # Radiobutton(labelFrame, text="Avail",variable = var, value=1, bg='white', fg='black', font=("Century 15")).place(relx=0.4,rely=0.65, relheight=0.08)
    # Radiobutton(labelFrame, text="Issued",variable = var, value=2, bg='white', fg='black', font=("Century 15")).place(relx=0.8,rely=0.65, relheight=0.08)
    
    
    # Radiobutton(labelFrame, text="Avail",variable = var, value=1, bg='white', fg='black', font=("Century 15")).place(relx=0.4,rely=0.65, relheight=0.08)
    # Radiobutton(labelFrame, text="Issued",variable = var, value=2, bg='white', fg='black', font=("Century 15")).place(relx=0.8,rely=0.65, relheight=0.08)

  
    # bookInfo4 = Entry(labelFrame, font=("Century 15"))
    # bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.13)
        
    #Submit Button
    SubmitBtnAvail = Button(root,text="Available",bg='#1f1f1f', bd=7, fg='orange', cursor="hand2", font=('Courier',15), command=bookRegisterAvail)
    SubmitBtnAvail.place(relx=0.34,rely=0.68, relwidth=0.22,relheight=0.08,)

    SubmitBtnIssue = Button(root,text="Issued",bg='#1f1f1f', bd=7, fg='orange', cursor="hand2", font=('Courier',15),command=issuer)
    SubmitBtnIssue.place(relx=0.62,rely=0.68, relwidth=0.22,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#1f1f1f', bd=7, fg='orange', cursor="hand2", font=('Courier',15), command=root.destroy)

    quitBtn.place(relx=0.41, rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
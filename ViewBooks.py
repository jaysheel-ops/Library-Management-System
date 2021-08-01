from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "rootpass"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books"


def View():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.attributes('-fullscreen', True);

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#112b51")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    y = 0.25

    # Displaying columns in View Book List 
    # -40s means leaving 40 spaces on right (ljust)
    # +40s means leaving 40 spaces on left  (rjust)
    Label(labelFrame, text="BID", font=('Courier', 15), bg='black', fg='white').grid(row=1, column=1, padx=30, pady=10)
    Label(labelFrame, text="Title", font=('Courier', 15), bg='black', fg='white').grid(row=1, column=3, padx=30,
                                                                                       pady=10)
    Label(labelFrame, text="Author", font=('Courier', 15), bg='black', fg='white').grid(row=1, column=5, padx=30,
                                                                                        pady=10)
    Label(labelFrame, text="Status", font=('Courier', 15), bg='black', fg='white').grid(row=1, column=7, padx=30,
                                                                                        pady=10)
    # Label(labelFrame, text="%-40s%-50s%-50s%-40s"%('BID','Title','Author','Status'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    # Label(labelFrame, text="----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getBooks = "select * from " + bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        count = 0;

        for i in cur:
            Label(labelFrame, text=i[0], font=('Courier', 13), bg='black', fg='white').grid(row=count + 3, column=1,
                                                                                            padx=30, pady=10)
            Label(labelFrame, text=i[1], font=('Courier', 13), bg='black', fg='white').grid(row=count + 3, column=3,
                                                                                            padx=30, pady=10)
            Label(labelFrame, text=i[2], font=('Courier', 13), bg='black', fg='white').grid(row=count + 3, column=5,
                                                                                            padx=30, pady=10)
            Label(labelFrame, text=i[3], font=('Courier', 13), bg='black', fg='white').grid(row=count + 3, column=7,
                                                                                            padx=30, pady=10)

            count += 1;
            # Label(labelFrame, text="%-40s%-35s%-35s%-35s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.07,rely=y)
            # Label(labelFrame, text="%s"%(i[0]).ljust(38, " ") + "%s"%(i[1]).ljust(45, " ") + "%s"%(i[1]).ljust(45, " ") + "%s"%(i[1]).ljust(45, " "),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    # mylist = Listbox(root, yscrollcommand = scrollbar.set )

    quitBtn = Button(root, text="Quit", bg='#1f1f1f', bd=7, fg='orange', cursor="hand2", font=('Courier', 15),
                     command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

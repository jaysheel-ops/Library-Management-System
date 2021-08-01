from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

# Add your own databa  name and password here to reflect in the code
mypass = "rootpass"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=400, height=400)

root.state("zoomed")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.attributes('-fullscreen', True);

# Take n greater than 0.25 and less than 5
same = True
n = 0.25


# Adding a background image
# background_image =Image.open("lib.jpg")
# bg = ImageTk.PhotoImage(file="lib.jpg")
# root.create_image(10, 10, image=bg, anchor=NW);
# [imageSizeWidth, imageSizeHeight] = background_image.size

# newImageSizeWidth = int(imageSizeWidth*n)
# if same:
#     newImageSizeHeight = int(imageSizeHeight*n) 
# else:
#     newImageSizeHeight = int(imageSizeHeight/n) 

# background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
# img = ImageTk.PhotoImage(background_image)

# Canvas1 = Canvas(root)

# Canvas1.create_image(300,340,image = img)      
# Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)

class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.image = Image.open("lib.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


e = Example(root)
e.pack(fill=BOTH, expand=YES)

headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to AISSMS\n Library Management System", bg='#2e2e2e', fg='white',
                     font=('Courier', 22))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Add Book Details", bg='black', bd=7, fg='orange', command=addBook, cursor="hand2",
              font=('Courier', 15))
btn1.place(relx=0.30, rely=0.4, relwidth=.40, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='black', bd=7, fg='orange', command=delete, cursor="hand2",
              font=('Courier', 15))
btn2.place(relx=0.30, rely=0.515, relwidth=.40, relheight=0.1)

btn3 = Button(root, text="View Book List", bg='black', bd=7, fg='orange', command=View, cursor="hand2",
              font=('Courier', 15))
btn3.place(relx=0.30, rely=0.63, relwidth=.40, relheight=0.1)

btn4 = Button(root, text="Issue Book to Student", bg='black', bd=7, fg='orange', command=issueBook, cursor="hand2",
              font=('Courier', 15))
btn4.place(relx=0.30, rely=0.745, relwidth=.40, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='black', bd=7, fg='orange', command=returnBook, cursor="hand2",
              font=('Courier', 15))
btn5.place(relx=0.30, rely=0.86, relwidth=.40, relheight=0.1)

quitBtn = Button(root, text="Quit", bg='#1f1f1f', bd=7, fg='orange', cursor="hand2", font=('Courier', 15),
                 command=root.destroy)
quitBtn.place(relx=0.9, rely=0.90, relwidth=0.08, relheight=0.07)

root.mainloop()

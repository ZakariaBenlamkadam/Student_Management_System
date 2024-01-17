from tkinter import *
from tkinter import ttk,messagebox,filedialog
import pymysql as p
import pandas
from pathlib import Path
from tkinter.ttk import Treeview
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pc\Desktop\tkinter\loginregis\loginRegistrationSystem\student library\assets\frame0")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def student_page():
    window.destroy()
    import studentpage



def searchbooks():
    connectdb()
    sub=e2.get()
    y=0.25
    q = 'SELECT * FROM book WHERE title= %s '
    cur.execute(q,(sub,))
    con.commit()

    result = cur.fetchone()
    if result:
        win = Tk()
        win.title('View Books')
        win.geometry("800x300+270+180")
        win.resizable(False, False)

        treeview = Treeview(win, columns=("Subject", "Title", "Author", "Serial No"), show='headings')
        treeview.heading("Subject", text="Subject")
        treeview.heading("Title", text="Title")
        treeview.heading("Author", text="Author")
        treeview.heading("Serial No", text="Serial No")
        treeview.column("Subject", anchor='center')
        treeview.column("Title", anchor='center')
        treeview.column("Author", anchor='center')
        treeview.column("Serial No", anchor='center')
        index = 0
        iid = 0
        connectdb()
        q = 'SELECT * FROM Book where title= %s '
        cur.execute(q,(sub,))
        details = cur.fetchall()
        for row in details:
            treeview.insert("", index, iid, value=row)
            index = iid = index + 1
        treeview.pack()
        closedb()
    else:
        print("Book not found.")

def searchbook():
    global win
    #win.destroy()
    win=Tk()
    win.title('Search Book')
    win.geometry("400x400+480+180")
    win.resizable(False,False)
    ustitle=Label(win,text='Title')
    global e2
    e2=Entry(win)
    #e2=Entry(win)
    b1=Button(win, height=2,width=17,text=' SEARCH ',command=searchbooks)
    b2=Button(win, height=2,width=17,text=' CLOSE ')#,command=searchbooks)
    ustitle.place(x=80,y=100)
    #paswrd.place(x=70,y=140)
    e2.place(x=180,y=100)
    #e2.place(x=180,y=142)
    b1.place(x=180,y=180)
    b2.place(x=180,y=230)
    win.mainloop()


def closedb():
    global con,cur
    cur.close()
    con.close()

def closebooks():
    global win
    win.destroy()
    window()

def connectdb():
    global con,cur
    #Enter your username and password of MySQL
    con=p.connect(host="localhost",user="root",passwd="kkuunn123")
    cur=con.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS Library')
    cur.execute('USE Library')
    global enter
    #if enter==1:
    #l = 'CREATE TABLE IF NOT EXISTS Login(name varchar(20),userid varchar(10),branch varchar(20),mobile int(10))'
    b = 'CREATE TABLE IF NOT EXISTS Book(subject varchar(20),title varchar(20),author varchar(20),serial int(5))'
    #i = 'CREATE TABLE IF NOT EXISTS BookIssue(stdid varchar(20),serial varchar(10),issue date,exp date)'
    #cur.execute(l)
    cur.execute(b)
    #cur.execute(i)
    #enter = enter + 1
    query='SELECT * FROM Login'
    cur.execute(query)

def viewbook():
    win=Tk()
    win.title('View Books')
    win.geometry("800x300+270+180")
    win.resizable(False,False)

    treeview=Treeview(win,columns=("Subject","Title","Author","Serial No"),show='headings')
    treeview.heading("Subject", text="Subject")
    treeview.heading("Title", text="Title")
    treeview.heading("Author", text="Author")
    treeview.heading("Serial No", text="Serial No")
    treeview.column("Subject", anchor='center')
    treeview.column("Title", anchor='center')
    treeview.column("Author", anchor='center')
    treeview.column("Serial No", anchor='center')
    index=0
    iid=0
    connectdb()
    q='SELECT * FROM Book'
    cur.execute(q)
    details=cur.fetchall()
    for row in details:
        treeview.insert("",index,iid,value=row)
        index=iid=index+1
    treeview.pack()
    win.mainloop()
    closedb()


window = Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width/2) - (506/2)  # 990 is the window width
y_coordinate = (screen_height/2) - (458/2) -40 # 660 is the window height

window.geometry("506x458+{}+{}".format(int(x_coordinate), int(y_coordinate)))

window.configure(bg = "#A9B1C6")


canvas = Canvas(window,bg = "#A9B1C6",height = 458,width = 506,bd = 0,highlightthickness = 0,relief = "ridge")

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(100.0,229.0,image=image_image_1)

canvas.create_text(213.0,35.0,anchor="nw",text="Student Library",fill="#000000",font=("Larsseit ExtraBold", 40 * -1))

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=viewbook,relief="flat")
button_1.place(x=241.0,y=113.0,width=238.0,height=49.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=searchbook,relief="flat")
button_2.place(x=241.0,y=167.0,width=238.0,height=49.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=student_page,relief="flat")
button_3.place(x=241.0,y=272.0,width=238.0,height=49.0)

window.resizable(False, False)
window.mainloop()

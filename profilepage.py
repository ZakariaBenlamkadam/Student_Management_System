from tkinter import *
from tkinter import ttk,messagebox,filedialog
import pymysql as p
import pandas
from pathlib import Path
from tkinter.ttk import Treeview
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.font import Font
from signinpage1 import usernameEntry
def closedb():
    global con,cur
    cur.close()
    con.close()

def connectdb():
    global con,cur
    #Enter your username and password of MySQL
    con=p.connect(host="localhost",user="root",passwd="kkuunn123")
    cur=con.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS userdata')
    cur.execute('USE userdata')
    global usernameEntry
    query = 'SELECT * FROM data1 where email=%s'
    cur.execute(query, usernameEntry)
    details = cur.fetchall()

    # Loop through each book and display its details vertically using the grid method
    row = 0
    for book in details:
        firstname_label = Label(win, text="FirstName:           "+str(book[1]), font=montserrat_regular)
        firstname_label.grid(row=row, column=0, sticky=W)
        lastname_label = Label(win, text="LastName :           "+str(book[2]), font=montserrat_regular)
        lastname_label.grid(row=row+2, column=0, sticky=W)
        email_label = Label(win, text="Email:                     "+str(book[3]), font=montserrat_regular)
        email_label.grid(row=row+4, column=0, sticky=W)
        phone_label = Label(win, text="Phone Number:"+str(book[5]), font=montserrat_regular)
        phone_label.grid(row=row+6, column=0, sticky=W)

        cin_label = Label(win, text="CIN:           " + str(book[6]), font=montserrat_regular)
        cin_label.grid(row=row, column=5, sticky=W)
        cne_label = Label(win, text="CNE :           " + str(book[7]), font=montserrat_regular)
        cne_label.grid(row=row + 2, column=5, sticky=W)
        birth_label = Label(win, text="Birthday:                     " + str(book[9]), font=montserrat_regular)
        birth_label.grid(row=row + 4, column=5, sticky=W)

        row += 3

win=Tk()
win.title('View Profile')
win.geometry("800x600+270+180")
win.resizable(False,False)

# Set up the Montserrat Regular font
montserrat_regular = Font(family="Montserrat", size=12)

def openProfile(usernameEntry):
    connectdb()

# Call the function with the username value passed as an argument
openProfile(usernameEntry)

win.mainloop()
closedb()

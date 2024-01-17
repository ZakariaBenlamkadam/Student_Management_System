import re
from distutils.command.check import check
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pc\Desktop\tkinter\loginregis\loginRegistrationSystem\sign up\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def validate_phone_number(phone_number):
    pattern = r'^\+\d{11,}$'
    return re.match(pattern, phone_number)

def validate_cin(cin):
    pattern = r'^[a-zA-Z]{1,2}\d{5,6}$'
    return re.match(pattern, cin)

def validate_cne(cne):
    pattern = r'^[a-zA-Z]{1}\d{8,9}$'
    return re.match(pattern, cne)

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{5,}$'


    return re.match(pattern, password)

def validate_birth_date(birth_date):
    pattern = r'^\d{2}/\d{2}/\d{2}$'
    return re.match(pattern, birth_date)

def connect_database():
    if firstnameEntry.get()==''or lastnameEntry.get()=='' or passwordEntry.get()=='' or emailEntry.get()==''\
            or confirmpasswordEntry.get()=='' or phonenumberEntry.get()=='' or cinEntry.get()=='' or cneEntry.get()==''\
            or studentadminEntry.get()=='' or birthEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('Error','Password Missmatch')
    #elif check.get()==0:
        #messagebox.showerror('Error', 'Please accept terms and conditions')
    elif not validate_email(emailEntry.get()):
        messagebox.showerror('Error', 'Invalid Email Format')
    elif not validate_phone_number(phonenumberEntry.get()):
        messagebox.showerror('Error', 'Invalid Phone Number Format')
    elif not validate_cin(cinEntry.get()):
        messagebox.showerror('Error', 'Invalid CIN Format')
    elif not validate_cne(cneEntry.get()):
        messagebox.showerror('Error', 'Invalid CNE Format')
    elif not validate_password(passwordEntry.get()):
        messagebox.showerror('Error',
                             'Password must contain at least 8 characters including uppercase letters, lowercase letters, numbers, and special characters')
    elif not validate_birth_date(birthEntry.get()):
        messagebox.showerror('Error', 'Invalid Birth Date Format (YY/MM/DD)')
    elif studentadminEntry.get().lower() not in ['student', 'admin']:
        messagebox.showerror('Error', 'Student/Admin entry should be "student" or "admin"')
    else:
        try:
          con=pymysql.connect(host='localhost', user='root',password='kkuunn123')
          mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return

        try:
           query='create database userdata'
           mycursor.execute(query)
           query='use userdata'
           mycursor.execute(query)
           query='create table data1(id int auto_increment primary key not null , firstname varchar (100),lastname varchar (100)' \
                 ',email varchar(50),password varchar(20),phonenumber varchar (100),cin varchar (100),cne varchar (100),' \
                 'studentadmin varchar(50),birth varchar(50))'
           mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query='select*from data1 where email=%s'
        mycursor.execute(query,(emailEntry.get()))
        row=mycursor.fetchone()
        if row is not None:
            messagebox.showinfo('Success', 'email ALready existe')

        else:
            query='insert into data1 (firstname,lastname,email,password,phonenumber,cin,cne,studentadmin,birth) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(firstnameEntry.get(),lastnameEntry.get(),emailEntry.get(),passwordEntry.get(),\
                                    phonenumberEntry.get(),cinEntry.get(),cneEntry.get(),studentadminEntry.get(),birthEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is successful')
            clear()
            window.destroy()
            import signinpage

def clear():
    firstnameEntry.delete(0,END)
    lastnameEntry.delete(0,END)
    emailEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmpasswordEntry.delete(0,END)
    phonenumberEntry.delete(0,END)
    cinEntry.delete(0,END)
    cneEntry.delete(0,END)
    studentadminEntry.delete(0,END)
    birthEntry.delete(0,END)
    check.set(0)

def login_page():
    window.destroy()
    import signinpage1

window = Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width/2) - (990/2)  # 990 is the window width
y_coordinate = (screen_height/2) - (660/2) -40 # 660 is the window height

window.geometry("990x660+{}+{}".format(int(x_coordinate), int(y_coordinate)))


window.configure(bg = "#431380")


canvas = Canvas(window, bg = "#431380", height = 660, width = 990, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)
canvas.create_rectangle(373.0, 0.0,990.0, 660.0, fill="#431380", outline="")

canvas.create_rectangle( 373.0, 0.0, 990.0, 660.0, fill="#D9D9D9", outline="")
canvas.create_text( 47.0, 65.0, anchor="nw", text="Join SMS for", fill="#FFFFFF", font=("Larsseit ExtraBold", 40 * -1))
canvas.create_text(46.0, 112.0, anchor="nw", text="Free", fill="#FFFFFF", font=("Larsseit ExtraBold", 40 * -1))

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
button_1.place(x=46.0, y=189.0, width=162.0, height=11.0)

canvas.create_text(47.0, 449.0, anchor="nw", text="Explore our user-friendly", fill="#FFFFFF", font=("Poppins Medium", 24 * -1))
canvas.create_text( 47.0,483.0,anchor="nw",text="SMS to efficiently manage",fill="#FFFFFF",font=("Poppins Medium", 24 * -1))
canvas.create_text(47.0, 516.0, anchor="nw", text="academic data ,", fill="#FFFFFF", font=("Poppins Medium", 24 * -1))
canvas.create_text(46.0, 548.0, anchor="nw", text="and administrative tasks ", fill="#FFFFFF", font=("Poppins Medium", 24 * -1))
canvas.create_text( 46.0, 581.0, anchor="nw", text="with ease.", fill="#FFFFFF", font=("Poppins Medium", 24 * -1))

def on_enter1(event):
    if firstnameEntry.get()=='First name':
        firstnameEntry.delete(0,'end')

def on_enter2(event):
    if lastnameEntry.get()=='Last name':
       lastnameEntry.delete(0,'end')

def on_enter3(event):
    if emailEntry.get()=='Email address':
       emailEntry.delete(0,'end')



def on_enter4(event):
    if passwordEntry.get()=='Password':
       passwordEntry.delete(0,'end')


def on_enter5(event):
    if confirmpasswordEntry.get() == 'Confirm password':
        confirmpasswordEntry.delete(0, 'end')


def on_enter6(event):
    if cinEntry.get() == 'CIN':
        cinEntry.delete(0, 'end')


def on_enter7(event):
    if cneEntry.get() == 'CNE':
        cneEntry.delete(0, 'end')


def on_enter8(event):
    if phonenumberEntry.get() == 'Phone number':
        phonenumberEntry.delete(0, 'end')


def on_enter9(event):
    if studentadminEntry.get() == 'Student / Admin':
        studentadminEntry.delete(0, 'end')


def on_enter10(event):
    if birthEntry.get() == 'YY/MM/DD':
        birthEntry.delete(0, 'end')


my_font=("lionel Text Steam", 25 * -1)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(562.0, 45.0, image=entry_image_1)
firstnameEntry = Entry(bd=0, bg="#F5F5F5", fg="#000716", highlightthickness=0,font=my_font)
firstnameEntry.place( x=464.0, y=16.0, width=196.0, height=56.0)
firstnameEntry.insert('end','First name')
firstnameEntry.bind('<FocusIn>',on_enter1)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(796.0, 45.0, image=entry_image_2)
lastnameEntry = Entry(bd=0, bg="#F5F5F5", fg="#000716", highlightthickness=0,font=my_font)
lastnameEntry.place(x=698.0, y=16.0, width=196.0, height=56.0)
lastnameEntry.insert('end','Last name')
lastnameEntry.bind('<FocusIn>',on_enter2)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(679.0, 114.0, image=entry_image_3)
emailEntry = Entry(bd=0, bg="#F5F5F5", fg="#000716", highlightthickness=0,font=my_font)
emailEntry.place( x=464.0, y=85.0, width=430.0, height=56.0)
emailEntry.insert('end','Email address')
emailEntry.bind('<FocusIn>',on_enter3)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(679.0,185.0,image=entry_image_4)
passwordEntry = Entry(bd=0,bg="#F5F5F5",fg="#000716",highlightthickness=0,font=my_font)
passwordEntry.place(x=464.0,y=156.0,width=430.0,height=56.0)
passwordEntry.insert('end','Password')
passwordEntry.bind('<FocusIn>',on_enter4)

entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(679.0,256.0,image=entry_image_5)
confirmpasswordEntry = Entry(bd=0, bg="#F5F5F5", fg="#000716", highlightthickness=0,font=my_font)
confirmpasswordEntry.place( x=464.0,y=227.0,width=430.0,height=56.0)
confirmpasswordEntry.insert('end','Confirm password')
confirmpasswordEntry.bind('<FocusIn>',on_enter5)

entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(679.0,328.0,image=entry_image_6)
phonenumberEntry= Entry(bd=0,bg="#F5F5F5",fg="#000716",highlightthickness=0,font=my_font)
phonenumberEntry.place(x=464.0,y=299.0,width=430.0,height=56.0)
phonenumberEntry.insert('end','Phone number')
phonenumberEntry.bind('<FocusIn>',on_enter8)

entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(562.0,398.0,image=entry_image_7)
cinEntry = Entry(bd=0,bg="#F5F5F5",fg="#000716",highlightthickness=0,font=my_font)
cinEntry.place(x=464.0,y=369.0,width=196.0,height=56.0)
cinEntry.insert('end','CIN')
cinEntry.bind('<FocusIn>',on_enter6)

entry_image_8 = PhotoImage(file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(796.0,398.0,image=entry_image_8)
cneEntry= Entry(bd=0,bg="#F5F5F5",fg="#000716",highlightthickness=0,font=my_font)
cneEntry.place(x=698.0,y=369.0,width=196.0,height=56.0)
cneEntry.insert('end','CNE')
cneEntry.bind('<FocusIn>',on_enter7)

entry_image_9 = PhotoImage(file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(562.0,467.0,image=entry_image_9)
studentadminEntry = Entry(bd=0,bg="#F5F5F5",fg="#000716",highlightthickness=0,font=my_font)
studentadminEntry.place(x=464.0, y=438.0,width=196.0, height=56.0)
studentadminEntry.insert('end','Student / Admin')
studentadminEntry.bind('<FocusIn>',on_enter9)

entry_image_10 = PhotoImage(file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(796.0,467.0,image=entry_image_10)
birthEntry = Entry(bd=0,bg="#F5F5F5",fg="#000716",highlightthickness=0,font=my_font)
birthEntry.place(x=698.0,y=438.0,width=196.0,height=56.0)
birthEntry.insert('end','YY/MM/DD')
birthEntry.bind('<FocusIn>',on_enter10)

def move_to_lastnameentry(event):
    lastnameEntry.focus()

firstnameEntry.bind('<Return>', move_to_lastnameentry)

def move_to_email(event):
    emailEntry.focus()

lastnameEntry.bind('<Return>', move_to_email)

def move_to_password(event):
    passwordEntry.focus()

emailEntry.bind('<Return>', move_to_password)

def move_to_confirm(event):
    confirmpasswordEntry.focus()

passwordEntry.bind('<Return>', move_to_confirm)

def move_to_phone(event):
    phonenumberEntry.focus()

confirmpasswordEntry.bind('<Return>', move_to_phone)

def move_to_cin(event):
    cinEntry.focus()

phonenumberEntry.bind('<Return>', move_to_cin)

def move_to_cne(event):
    cneEntry.focus()

cinEntry.bind('<Return>', move_to_cne)

def move_to_sadmin(event):
    studentadminEntry.focus()

cneEntry.bind('<Return>', move_to_sadmin)

def move_to_birth(event):
    birthEntry.focus()

studentadminEntry.bind('<Return>', move_to_birth)

def last_enter(event):
    signupButton.focus_set()
    signupButton.invoke()

birthEntry.bind('<Return>', last_enter)


button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
signupButton = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=connect_database,relief="flat")
signupButton.place(x=454.0,y=508.0,width=450.0,height=60.0)


canvas.create_text(564.0,594,anchor="nw",text="Already a member?",fill="#000000",font=("lionel Text Steam", 20 * -1))

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
signinButton = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=login_page,relief="flat")
signinButton.place(x=700.0,y=590.0,width=93.0,height=36.0)

canvas.create_rectangle(454.0,626.0,904.0,627.0,fill="#000000",outline="")
canvas.create_text(492.0,633.0,anchor="nw",text="By signing up you agree to SMS’s Terms Of Service and ",fill="#000000",font=("lionel Text Steam", 15 * -1))
canvas.create_text(780.0,633.0,anchor="nw",text="Privacy Policy",fill="#431380",font=("lionel Text Steam", 15 * -1))

canvas.create_text(476.0,27.0,anchor="nw",text="First name",fill="#000000",font=("lionel Text Steam", 25 * -1))
canvas.create_text(707.0,27.0,anchor="nw",text="Last name",fill="#000000",font=("lionel Text Steam", 25 * -1))
canvas.create_text(476.0,99.0, anchor="nw", text="Email address", fill="#000000", font=("lionel Text Steam", 25 * -1))
canvas.create_text(476.0,170.0,anchor="nw",text="Password",fill="#000000",font=("lionel Text Steam", 25 * -1))
canvas.create_text(476.0,238.0,anchor="nw",text="Confirm password",fill="#000000",font=("lionel Text Steam", 25 * -1))
canvas.create_text(476.0,309.0,anchor="nw",text="Phone number ",fill="#000000",font=("lionel Text Steam", 25 * -1))
canvas.create_text(476.0,382.0,anchor="nw", text="CIN", fill="#000000", font=("lionel Text Steam", 25 * -1))
canvas.create_text(707.0,382.0,anchor="nw",text="CNE",fill="#000000",font=("lionel Text Steam", 25 * -1))
canvas.create_text(476.0,450.0,anchor="nw",text="Level",fill="#000000",font=("lionel Text Steam", 25 * -1))
canvas.create_text(707.0,450.0,anchor="nw",text="YY/MM/DD",fill="#000000",font=("lionel Text Steam", 25 * -1))

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(307.0,260.0,image=image_image_1)
window.resizable(False, False)
window.mainloop()

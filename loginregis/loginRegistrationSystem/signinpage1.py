from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
import row as row
from PIL import ImageTk
from PIL.ImageTk import PhotoImage
from tkinter import messagebox
import pymysql
import re
import tkinter.messagebox as messagebox


global current_user
current_user = ""

def login_user():
    global usernameEntry, current_user
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields Are Required ')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='kkuunn123')
            mycursor = con.cursor()


        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select * from data1 where email=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row is None:
            messagebox.showerror('Error','Invalid email or password')
        else:
            current_user = usernameEntry.get()  # save the current user's username
            if row[8] == 'admin':
                # Open admin window here
                messagebox.showinfo('Welcome', 'Admin login successful')
                window.destroy()
                import adminpage
            elif row[8] == 'student':
                # Open student window here
                messagebox.showinfo('Welcome', 'student login successful')
                window.destroy()
                import studentpage

            else:
                # Open regular user window here
                messagebox.showinfo('Welcome', 'Login successful')


def forgot_pass():
    if usernameEntry.get() == "":
        messagebox.showerror("Error", "Please enter your email address to reset your password", parent=window)
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='kkuunn123', database='userdata')
            cur = con.cursor()
            cur.execute("SELECT * FROM data1 WHERE email=%s", usernameEntry.get())
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please enter a valid email address to reset your password", parent=window)
            else:
                con.close()
                global root2
                root2 = Toplevel()

                root2.title("Forgot Password")
                root2.geometry("350x400+495+150")
                root2.config(bg="white")
                root2.focus_force()
                root2.grab_set()
                t = Label(root2, text="Forgot Password", font=("Times mew roman", 20, "bold"), bg="white", fg="red")
                t.place(x=0, y=10, relwidth=1)
                question = Label(root2, text="Security Question", font=("Times mew roman", 15, "bold"), bg="white", fg="gray")
                question.place(x=50, y=100)
                cmd_quest = ttk.Combobox(root2, font=("Times mew roman", 13), state="readonly", justify=CENTER)
                cmd_quest['values'] = ("Select", "Your first pet's name", "Your birthplace", "Your best friend's name")
                cmd_quest.place(x=50, y=130, width=250)
                cmd_quest.current(0)
                answer = Label(root2, text="Answer", font=("times new romam", 15, "bold"), bg="white", fg="gray")
                answer.place(x=50, y=180)
                txt_answer = Entry(root2, font=("times new roman", 15), bg="lightgray")
                txt_answer.place(x=50, y=210, width=250)
                new_password = Label(root2, text="New password", font=("times new roman", 15, "bold"), bg="white", fg="gray")
                new_password.place(x=50, y=250)
                txt_new_pass = Entry(root2, font=("times new roman", 15), bg="lightgray")
                txt_new_pass.place(x=50, y=280, width=250)
                btn_reset_password = Button(root2, text="Reset Password", command=lambda: reset_password(usernameEntry.get(), cmd_quest.get(), txt_answer.get(), txt_new_pass.get()), bg="green", fg="white", font=("times new roman", 15, "bold"))
                btn_reset_password.place(x=90, y=340)
        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=window)

def reset_password(email, question, answer, new_password):
    try:
        con = pymysql.connect(host='localhost', user='root', password='kkuunn123', database='userdata')
        cur = con.cursor()
        cur.execute("SELECT * FROM data1 WHERE email=%s and question=%s and answer=%s", (email, question, answer))
        row = cur.fetchone()
        if row is None:
            messagebox.showerror("Error", "Incorrect security question or answer", parent=root2)
        else:
            cur.execute("UPDATE data1 SET password=%s WHERE email=%s", (new_password, email))
            con.commit()
            messagebox.showinfo("Success", "Password reset successful", parent=root2)
            root2.destroy()
    except Exception as es:
        messagebox.showerror("Error", f"Error due to: {str(es)}", parent=root2)
    finally:
        con.close()


def signup_page():
    window.destroy()
    import signupfinal

def hide():

    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def on_enter(event):
    if usernameEntry.get()=='Email address':
       usernameEntry.delete(0,'end')
def password_enter(event):
    if passwordEntry.get()=='Password':
       passwordEntry.delete(0,'end')


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pc\Desktop\tkinter\loginregis\loginRegistrationSystem\sign in\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width/2) - (990/2)  # 990 is the window width
y_coordinate = (screen_height/2) - (660/2) -40 # 660 is the window height

window.geometry("990x660+{}+{}".format(int(x_coordinate), int(y_coordinate)))


window.configure(bg = "#7129B3")


canvas = Canvas(window, bg = "#7129B3", height = 660, width = 990, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(831.0, 400.0, image=image_image_1)
canvas.create_rectangle(0.0, 0.0, 618.0, 660.0, fill="#F5F5F5", outline="")

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=signup_page,relief="flat")
button_1.place(x=705.0, y=421.0, width=199.0, height=48.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=login_user, relief="flat")
button_2.place(x=200.0, y=421.0, width=210.0, height=48.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=forgot_pass,relief="flat")
button_3.place(x=361.0, y=387.0, width=129.0, height=19.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0, command=signup_page , relief="flat")
button_4.place(x=331.0, y=517.5, width=54.0, height=19.0)


openeye=PhotoImage(file='openeye.png')
eyeButton=Button(window,image=openeye,bd=0 ,bg='#D9D9D9',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=470,y=350)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(101.0, 61.0, image=image_image_2)

canvas.create_text(107.0, 40.0, anchor="nw", text="SMS ", fill="#7129B3", font=("Biko_Black", 28 * -1))
canvas.create_text(47.0, 166.0, anchor="nw", text="Welcome Back To SMS ", fill="#000000", font=("Stem-Bold", 45 * -1))
canvas.create_text(685.0, 246.0, anchor="nw", text="New Here?", fill="#F5F5F5" ,font=("Stem-Bold", 45 * -1))
canvas.create_text(166.0, 224.0, anchor="nw", text="sign in to continue to your account  ", fill="#000000", font=("Lionel Text Steam", 25 * -1))
canvas.create_text( 685.0, 321.0, anchor="nw", text="sign up and discover our ", fill="#F5F5F5", font=("Lionel Text Steam", 30 * -1))
canvas.create_text(730.0, 353.0, anchor="nw", text="great services ", fill="#F5F5F5", font=("Lionel Text Steam", 30 * -1))


my_font = ("Stem-Regular", 12 * -1)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(305.0, 302.0, image=entry_image_1)
usernameEntry= Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, font=my_font)
usernameEntry.place(x=117.0, y=281.0+12, width=376.0, height=20.0)
usernameEntry.insert('end','Email address')
usernameEntry.bind('<FocusIn>',on_enter)




def move_to_password_entry(event):
    passwordEntry.focus()


usernameEntry.bind('<Return>', move_to_password_entry)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(305.0, 362.0, image=entry_image_2)
passwordEntry= Entry( bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, font=my_font)
passwordEntry.place(x=117.0, y=341.0+12 , width=330.0, height=20.0)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

def password_enter(event):
    button_2.focus_set()
    button_2.invoke()

passwordEntry.bind('<Return>', password_enter)

canvas.create_text(219.0, 520.0, anchor="nw", text="Not a member yet? ", fill="#000000", font=("Stem-Regular", 12 * -1))

canvas.create_text(212.0, 606.0, anchor="nw", text="© 2023 SMS , All Rights Reserved", fill="#000000", font=("Montserrat Regular", 11 * -1))

canvas.create_text(214.0, 619.0, anchor="nw", text="  By signing up, I agree to SMS’s ", fill="#000000", font=("Montserrat Regular", 11 * -1))

canvas.create_text(250.0, 632.0, anchor="nw", text="Terms of Service", fill="#242371", font=("Montserrat Regular", 11 * -1))
window.resizable(False, False)
window.mainloop()

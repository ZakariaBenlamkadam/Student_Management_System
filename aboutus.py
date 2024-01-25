
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pc\Desktop\tkinter\loginregis\loginRegistrationSystem\aboutus\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def signup_page():
    window.destroy()
    import signupfinal
def signin_page():
    window.destroy()
    import signinpage1
def home_page():
    window.destroy()
    import homepage
def contactus_page():
    window.destroy()
    import contactus

window = Tk()


screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width/2) - (990/2)  # 990 is the window width
y_coordinate = (screen_height/2) - (660/2) -30 # 660 is the window height

window.geometry("990x660+{}+{}".format(int(x_coordinate), int(y_coordinate)))

window.configure(bg = "#DDDEE2")


canvas = Canvas(window,bg = "#DDDEE2",height = 660,width = 990,bd = 0,highlightthickness = 0,relief = "ridge")

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(70.0,64.0,image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(293.0,225.0,image=image_image_2)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=home_page,relief="flat")
button_1.place(x=253.0,y=36.0,width=84.0,height=37.0)

canvas.create_rectangle(559.0,0.0,990.0,313.0,fill="#DDDEE2",outline="")

canvas.create_rectangle(559.0,0.0,990.0,313.0,fill="#4F6576",outline="")

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=signup_page,relief="flat")
button_2.place(x=381.0,y=36.0,width=84.0,height=37.0)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(160.0,51.0,image=image_image_3)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=contactus_page,relief="flat")
button_3.place(x=716.0, y=27.0,width=125.0,height=44.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4, borderwidth=0,highlightthickness=0,command=signin_page,relief="flat")
button_4.place(x=204.0, y=322.0, width=133.0, height=45.0)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(832.0,331.0,image=image_image_4)

canvas.create_text(65.0,145.0,anchor="nw",text="Manage Your Academic ",fill="#000000",font=("Larsseit ExtraBold", 40 * -1))

canvas.create_text(137.0,195.0,anchor="nw",text="Life With EASE:",fill="#000000",font=("Larsseit ExtraBold", 40 * -1))

canvas.create_text(175.0,259.0,anchor="nw",text="try our system today",fill="#000000",font=("Larsseit Medium", 22 * -1))

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(image=button_image_5,borderwidth=0,highlightthickness=0,command=lambda: print("button_5 clicked"),relief="flat")
button_5.place(x=229.0,y=476.0,width=91.0,height=84.0)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(image=button_image_6,borderwidth=0,highlightthickness=0,command=lambda: print("button_6 clicked"),relief="flat")
button_6.place(x=37.0,y=472.0,width=94.0,height=91.0)

button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
button_7 = Button(image=button_image_7,borderwidth=0,highlightthickness=0,command=lambda: print("button_7 clicked"),relief="flat")
button_7.place(x=422.0,y=472.0,width=103.0,height=88.0)

button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
button_8 = Button(image=button_image_8,borderwidth=0,highlightthickness=0,command=lambda: print("button_8 clicked"),relief="flat")
button_8.place(x=131.0,y=481.0,width=98.0,height=86.0)

button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
button_9 = Button(image=button_image_9,borderwidth=0,highlightthickness=0,command=lambda: print("button_9 clicked"),relief="flat")
button_9.place(x=328.0, y=476.0, width=79.0, height=91.0)

canvas.create_text(59.0,563.0,anchor="nw",text="Course \n",fill="#000000",font=("Larsseit Medium", 18 * -1))

canvas.create_text(39.0,563.0,anchor="nw",text="\nManagement",fill="#000000",font=("Larsseit Medium", 18 * -1))

canvas.create_text(153.0,432.0,anchor="nw",text="Library \n",fill="#000000",font=("Larsseit Medium", 18 * -1))

canvas.create_text(131.0,432.0,anchor="nw",text=" \nManagement",fill="#000000",
font=("Larsseit Medium", 18 * -1))

canvas.create_text(343.0,432.0,anchor="nw",text="Profile \n",fill="#000000",font=("Larsseit Medium", 18 * -1))

canvas.create_text(320.0,432.0,anchor="nw",text=" \nManagement",fill="#000000",font=("Larsseit Medium", 18 * -1))

canvas.create_text(454.0,559.0,anchor="nw",text="Easy\n\n",fill="#000000",font=("Larsseit Medium", 18 * -1))

canvas.create_text(431.0,559.0,anchor="nw",text="\nNavigation\n",fill="#000000",font=("Larsseit Medium", 18 * -1))

canvas.create_text(245.0,565.0,anchor="nw",text="Chatting",fill="#000000",font=("Larsseit Medium", 18 * -1))

canvas.create_text(679.0,622.0,anchor="nw",text="©️ 2023 SMS. All Rights Reserved   ",fill="#000000",font=("Montserrat Regular", 14 * -1))

canvas.create_text(68.0,379.0,anchor="nw",text="Our student management system provides many benefits and features to make ",fill="#000000",font=("lionel Text Steam", 18 * -1))

canvas.create_text(68.0,395.0, anchor="nw", text="student's lives easier. Here are some of the main benefits and features:",fill="#000000",font=("lionel Text Steam", 18 * -1))
window.resizable(False, False)
window.mainloop()

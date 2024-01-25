
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pc\Desktop\tkinter\loginregis\loginRegistrationSystem\student page\assets\frame0")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def chat_page():
    window.destroy()
    import server
    import student

def courses_page():

    import courses

def library_page():

    import studentlibrary

def logut_page():
    window.destroy()
    import homepage
def profile():
    window.destroy()
    import profilepage



window = Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width/2) - (990/2)  # 990 is the window width
y_coordinate = (screen_height/2) - (660/2) -40 # 660 is the window height

window.geometry("990x660+{}+{}".format(int(x_coordinate), int(y_coordinate)))


window.configure(bg = "#2D2A33")


canvas = Canvas( window, bg = "#2D2A33", height = 660, width = 990, bd = 0, highlightthickness = 0, relief = "ridge")

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(447.5,  325.0,image=image_image_1)

canvas.create_text( 342.0, 58.0, anchor="nw", text="Student Page ", fill="#000000", font=("Poppins ExtraBold", 40 * -1))

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(478.0,397.0,image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(86.0,88.0,image=image_image_3)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=profile,relief="flat")
button_1.place(x=76.0,y=230.0,width=130.0,height=111.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button( image=button_image_2, borderwidth=0, highlightthickness=0, command=courses_page, relief="flat")
button_2.place(x=76.0,y=457.0,width=123.0,height=119.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=library_page,relief="flat")
button_3.place(x=766.0,y=457.0,width=131.0,height=113.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4,borderwidth=0, highlightthickness=0,command=chat_page,relief="flat")
button_4.place(x=766.0,y=239.0,width=118.0,height=108.0)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(image=button_image_5,borderwidth=0,highlightthickness=0,relief="flat")
button_5.place(x=879.0,y=47.0,width=79.0,height=91.0)
canvas.create_text(809.0,352.0,anchor="nw",text="Chat",fill="#DBC6C6",font=("Larsseit Medium", 18 * -1))
canvas.create_text(117.0,352.0,anchor="nw",text="Profile",fill="#DBC6C6",font=("Larsseit Medium", 18 * -1))

canvas.create_text(111.0,581.0, anchor="nw",text="Courses",fill="#DBC6C6",font=("Larsseit Medium", 18 * -1))

canvas.create_text(802.0,581.0,anchor="nw",text="Library",fill="#DBC6C6",font=("Larsseit Medium", 18 * -1))

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(image=button_image_6,borderwidth=0,highlightthickness=0,command=logut_page,relief="flat")
button_6.place(x=680.0,y=67.0,width=143.0,height=44.0)
window.resizable(False, False)
window.mainloop()

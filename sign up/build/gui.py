
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pc\Desktop\tk\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("990x660")
window.configure(bg = "#431380")


canvas = Canvas(
    window,
    bg = "#431380",
    height = 660,
    width = 990,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    373.0,
    0.0,
    990.0,
    660.0,
    fill="#431380",
    outline="")

canvas.create_rectangle(
    373.0,
    0.0,
    990.0,
    660.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    47.0,
    65.0,
    anchor="nw",
    text="Join SMS for",
    fill="#FFFFFF",
    font=("Larsseit ExtraBold", 40 * -1)
)

canvas.create_text(
    46.0,
    112.0,
    anchor="nw",
    text="Free",
    fill="#FFFFFF",
    font=("Larsseit ExtraBold", 40 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=46.0,
    y=189.0,
    width=162.0,
    height=11.0
)

canvas.create_text(
    47.0,
    449.0,
    anchor="nw",
    text="Explore our user-friendly",
    fill="#FFFFFF",
    font=("Poppins Medium", 24 * -1)
)

canvas.create_text(
    47.0,
    483.0,
    anchor="nw",
    text="SMS to efficiently manage",
    fill="#FFFFFF",
    font=("Poppins Medium", 24 * -1)
)

canvas.create_text(
    47.0,
    516.0,
    anchor="nw",
    text="academic data ,",
    fill="#FFFFFF",
    font=("Poppins Medium", 24 * -1)
)

canvas.create_text(
    46.0,
    548.0,
    anchor="nw",
    text="and administrative tasks ",
    fill="#FFFFFF",
    font=("Poppins Medium", 24 * -1)
)

canvas.create_text(
    46.0,
    581.0,
    anchor="nw",
    text="with ease.",
    fill="#FFFFFF",
    font=("Poppins Medium", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    562.0,
    45.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=464.0,
    y=16.0,
    width=196.0,
    height=56.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    796.0,
    45.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=698.0,
    y=16.0,
    width=196.0,
    height=56.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    679.0,
    114.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=464.0,
    y=85.0,
    width=430.0,
    height=56.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    679.0,
    185.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=464.0,
    y=156.0,
    width=430.0,
    height=56.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    679.0,
    256.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=464.0,
    y=227.0,
    width=430.0,
    height=56.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    679.0,
    328.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=464.0,
    y=299.0,
    width=430.0,
    height=56.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=454.0,
    y=508.0,
    width=450.0,
    height=60.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    562.0,
    398.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=464.0,
    y=369.0,
    width=196.0,
    height=56.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    796.0,
    398.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=698.0,
    y=369.0,
    width=196.0,
    height=56.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    562.0,
    467.0,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=464.0,
    y=438.0,
    width=196.0,
    height=56.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    796.0,
    467.0,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#F5F5F5",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=698.0,
    y=438.0,
    width=196.0,
    height=56.0
)

canvas.create_text(
    564.0,
    597.0,
    anchor="nw",
    text="Already a member?",
    fill="#000000",
    font=("LionelTextSteam", 20 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=711.0,
    y=593.0,
    width=93.0,
    height=36.0
)

canvas.create_rectangle(
    454.0,
    626.0,
    904.0,
    627.0,
    fill="#000000",
    outline="")

canvas.create_text(
    457.0,
    633.0,
    anchor="nw",
    text="By signing up you agree to SMS’s Terms Of Service and ",
    fill="#000000",
    font=("LionelTextSteam", 15 * -1)
)

canvas.create_text(
    796.0,
    633.0,
    anchor="nw",
    text="Privacy Policy",
    fill="#431380",
    font=("LionelTextSteam", 15 * -1)
)

canvas.create_text(
    476.0,
    27.0,
    anchor="nw",
    text="First name",
    fill="#000000",
    font=("LionelTextSteam", 25 * -1)
)

canvas.create_text(
    707.0,
    27.0,
    anchor="nw",
    text="Last name",
    fill="#000000",
    font=("LionelTextSteam", 25 * -1)
)

canvas.create_text(
    476.0,
    99.0,
    anchor="nw",
    text="Email adress",
    fill="#000000",
    font=("LionelTextSteam", 25 * -1)
)

canvas.create_text(
    476.0,
    170.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("LionelTextSteam", 25 * -1)
)

canvas.create_text(
    476.0,
    238.0,
    anchor="nw",
    text="Confirm password",
    fill="#000000",
    font=("LionelTextSteam", 25 * -1)
)

canvas.create_text(
    476.0,
    309.0,
    anchor="nw",
    text="Phone number ",
    fill="#000000",
    font=("LionelTextSteam", 25 * -1)
)

canvas.create_text(
    476.0,
    382.0,
    anchor="nw",
    text="CIN",
    fill="#000000",
    font=("LionelTextSteam", 25 * -1)
)

canvas.create_text(
    707.0,
    382.0,
    anchor="nw",
    text="CNE",
    fill="#000000",
    font=("LionelTextSteam", 25 * -1)
)

canvas.create_text(
    476.0,
    450.0,
    anchor="nw",
    text="Level",
    fill="#000000",
    font=("LionelTextSteam", 25 * -1)
)

canvas.create_text(
    707.0,
    450.0,
    anchor="nw",
    text="YY/MM/DD",
    fill="#000000",
    font=("LionelTextSteam", 25 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    307.0,
    260.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()

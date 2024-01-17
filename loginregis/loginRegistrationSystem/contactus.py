
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pc\Desktop\tkinter\loginregis\loginRegistrationSystem\contact us\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("990x660")
window.configure(bg = "#DDDEE2")


canvas = Canvas(
    window,
    bg = "#DDDEE2",
    height = 660,
    width = 990,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    130.0,
    100.0,
    image=image_image_1
)

canvas.create_rectangle(
    787.0,
    0.0,
    990.0,
    660.0,
    fill="#DFD842",
    outline="")

canvas.create_rectangle(
    559.0,
    105.0,
    990.0,
    559.0,
    fill="#0C5389",
    outline="")

canvas.create_rectangle(
    531.0,
    94.0,
    587.0,
    137.0,
    fill="#DFD943",
    outline="")

canvas.create_rectangle(
    0.0,
    310.0,
    56.0,
    353.0,
    fill="#DFD943",
    outline="")

canvas.create_text(
    153.0,
    216.0,
    anchor="nw",
    text="Contact Us",
    fill="#000000",
    font=("Larsseit ExtraBold", 50 * -1)
)

canvas.create_text(
    608.0,
    154.0,
    anchor="nw",
    text="Info",
    fill="#F5E7E7",
    font=("Larsseit ExtraBold", 40 * -1)
)

canvas.create_text(
    89.0,
    300.0,
    anchor="nw",
    text="Feel free to contact us any time , We will ",
    fill="#000000",
    font=("Poppins Regular", 20 * -1)
)

canvas.create_text(
    89.0,
    300.0,
    anchor="nw",
    text="\nget back to you as soon as we can! ",
    fill="#000000",
    font=("Poppins Regular", 20 * -1)
)

canvas.create_text(
    657.0,
    225.0,
    anchor="nw",
    text="sms@getintouch.we",
    fill="#FFFFFF",
    font=("Poppins Regular", 20 * -1)
)

canvas.create_text(
    656.0,
    303.0,
    anchor="nw",
    text="+212 66 66 66 66",
    fill="#FFFFFF",
    font=("Poppins Regular", 20 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    284.0,
    451.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    626.0,
    401.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    626.0,
    317.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    622.0,
    244.0,
    image=image_image_5
)

canvas.create_text(
    656.0,
    386.0,
    anchor="nw",
    text="BP 03, Ajdir Al-Hoceima",
    fill="#FFFFFF",
    font=("Poppins Regular", 20 * -1)
)
window.resizable(False, False)
window.mainloop()

import functionality as fxn
import sys
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("600x800")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    600.0,
    800.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    0.0,
    166.0,
    600.0,
    800.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    33.0,
    330.0,
    273.0,
    773.0,
    fill="#B1DDFD",
    outline="")

canvas.create_rectangle(
    116.0,
    177.0,
    485.0,
    301.00000000000006,
    fill="#B1DDFD",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: fxn.Add_Gui(window),
    relief="flat"
)
button_1.place(
    x=55.0,
    y=355.0,
    width=199.0,
    height=44.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: fxn.Read_Gui(window),
    relief="flat"
)
button_2.place(
    x=55.0,
    y=448.0,
    width=199.0,
    height=40.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: fxn.Modify_Gui(window),
    relief="flat"
)
button_3.place(
    x=55.0,
    y=539.0,
    width=199.0,
    height=44.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: fxn.Delete_Gui(window),
    relief="flat"
)
button_4.place(
    x=55.0,
    y=627.0,
    width=199.0,
    height=44.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: sys.exit(0),
    relief="flat"
)
button_5.place(
    x=55.0,
    y=710.0,
    width=199.0,
    height=44.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    300.0,
    83.00001525878895,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    439.0,
    471.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    304.0,
    244.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()

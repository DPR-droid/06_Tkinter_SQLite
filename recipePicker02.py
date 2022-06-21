from multiprocessing import connection
from tkinter import Tk, Label
import tkinter
from PIL import ImageTk
from isort import file
import sqlite3


# set background color
bg_colour = "#3d6466"


#Function for Widget button
def load_frame1():
    # Keep background
    frame1.pack_propagate(False)
    # frame1 widgets
    logo_img = ImageTk.PhotoImage(file="RRecipe_logo.png")
    logo_widget = tkinter.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image_names = logo_img
    logo_widget.pack()

    # Create Widget label 
    tkinter.Label(frame1,
            text="ready for your random recipe?",
            bg=bg_colour,
            fg="white",
            font=("TkMenuFont", 14)
            ).pack()

    # Create Widget button
    tkinter.Button(
        frame1,
        text="SHUFFLE",
        font=("TkHeadingFont", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame2()
        ).pack(pady=20)

#Function for Widget button
def load_frame2():
    print("Hello World")


root = Tk()
# Window title
root.title("Recipe Picker")
# Place window in middle of screen
root.eval("tk::PlaceWindow . center")

# Frame widget to group.
frame1 = tkinter.Frame(root, width=500, height=600, bg=bg_colour)
# Frame 2
frame2 = tkinter.Frame(root, bg=bg_colour)



for frame in (frame1, frame2):
    frame.grid(row=0, column=0)

# call frame1 to run   
load_frame1()

root.mainloop()

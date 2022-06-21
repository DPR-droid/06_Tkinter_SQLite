import imp
from multiprocessing import connection
from tkinter import Tk, Label
import tkinter
from PIL import ImageTk
from isort import file
import sqlite3
from numpy import random
import pyglet


# set background color
bg_colour = "#3d6466"

# Add fonts
pyglet.font.add_file("Ubuntu-Bold.ttf")
pyglet.font.add_file("Shanti-Regular.ttf")

def clear_widget(frame):
    for widget in frame.winfo_children():
        widget.destroy()

#Function for Widget button
def load_frame1():
    clear_widget(frame2)
    frame1.tkraise()
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
            font=("Ubuntu", 14)
            ).pack()

    # Create Widget button
    tkinter.Button(
        frame1,
        text="SHUFFLE",
        font=("Shanti", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame2()
        ).pack(pady=20)


# Connect to SQLite table
def fetch_db():
    connection = sqlite3.connect("recipes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()

    # Create a random number
    idx = random.randint(0, len(all_tables)-1)

    # Fetch ingredients
    table_name = all_tables[idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall()


    """ print(ingredients)
    print(table_name) """
    connection.close
    return table_name, table_records

def pre_process(table_name, table_records):
    title = table_name[:-6]
    title = "".join([char if char.islower() else " " +  char for char in title])
    # print(title)

    ingredients = []

    # process the ingredients
    for i in table_records:
        name = i[1]
        qty = i[2]
        unit = i[3]
        ingredients.append(qty + " " + unit + " of " + name)

    #print(ingredients)
    return title, ingredients


#Function for Widget button
def load_frame2():
    clear_widget(frame1)
    frame2.tkraise()
    table_name, table_records = fetch_db()
    title, ingredients = pre_process(table_name, table_records)

    logo_img = ImageTk.PhotoImage(file="RRecipe_logo_bottom.png")
    logo_widget = tkinter.Label(frame2, image=logo_img, bg=bg_colour)
    logo_widget.image_names = logo_img
    logo_widget.pack(pady=20)

    # Create Widget label 
    tkinter.Label(frame2,
            text=title,
            bg=bg_colour,
            fg="white",
            font=("Shanti", 20)
            ).pack(pady=25)

    for i in ingredients:
        # Create Widget label 
        tkinter.Label(frame2,
                text=i,
                bg="#28393a",
                fg="white",
                font=("Ubuntu", 14)
                ).pack(fill="both")

    
    # Create Widget button
    tkinter.Button(
        frame2,
        text="BACK",
        font=("Shanti", 18),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame1()
        ).pack(pady=20)



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
    frame.grid(row=0, column=0, sticky="news")

# call frame1 to run   
load_frame1()

root.mainloop()

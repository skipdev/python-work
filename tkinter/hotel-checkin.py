#the class is a blueprint to describe what the gui looks and behaves like
from tkinter import *
def run():
    window = Tk()

    name_frame = Frame(window)
    name_label = Label(name_frame, text = "Name", width = 50)
    name_label.pack(side = LEFT)
    name_entry = Entry(name_frame, width = 50)
    name_entry.pack(side = RIGHT)
    name_frame.pack()

    passport_frame = Frame(window)
    passport_label = Label(passport_frame, text = "Passport Number", width = 50)
    passport_label.pack(side = LEFT)
    passport_entry = Entry(passport_frame, width = 50)
    passport_entry.pack(side = RIGHT)
    passport_frame.pack()

    nights_frame = Frame(window)
    nights_label = Label(nights_frame, text = "No of Nights", width = 50)
    nights_label.pack(side = LEFT)
    nights_entry = Entry(nights_frame, width = 50)
    nights_entry.pack(side = RIGHT)
    nights_frame.pack()

    checkin_button = Button(text="Check In")
    checkin_button.pack()
    
run()

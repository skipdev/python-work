#the class is a blueprint to describe what the gui looks and behaves like
from tkinter import *
class Travel(Tk):
    def __init__(self):
        Tk.__init__(self)
        #display default image
        self.map_img = PhotoImage(file="map.gif", width=1200, height=535)
        self.bus_img = PhotoImage(file="bus.gif", width=150, height=150)
        
        self.map_label = Label(image=self.map_img)
        self.map_label.place(x=5, y=5)

        self.bus_label = Label(image=self.bus_img)
        self.bus_label.place(x=5, y=5)
        self.bus_label.bind("<B1-Motion>", self.movement)

    def movement(self, event):
        self.bus_label.place(x=event.x, y=event.y)
#the object is the actual GUI
gui = Travel()
gui.mainloop

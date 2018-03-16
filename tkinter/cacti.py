#the class is a blueprint to describe what the gui looks and behaves like
from tkinter import *
class Cacti(Tk):
    def __init__(self):
        Tk.__init__(self)
        #display default image
        self.cacti_image = PhotoImage(file="cactus.gif", width=220, height=220)
        self.cacti_image2 = PhotoImage(file="cactus2.gif", width=225, height=300)
        
        self.cacti_label = Label(image=self.cacti_image)
        self.cacti_label.grid(row=1, column=1)
        
        self.flip_button = Button(text="Flip Button")
        self.flip_button.grid(row=2, column=1)
        self.flip_button.bind("<Button-1>", self.flip_button_1_clicked)
        
    def flip_button_1_clicked(self, event):   
        self.cacti_label.configure(image = self.cacti_image2)
        self.flip_button.bind("<Button-3>", self.flip_button_3_clicked)
        
    def flip_button_3_clicked(self, event):   
        self.cacti_label.configure(image = self.cacti_image)
        self.flip_button.bind("<Button-1>", self.flip_button_1_clicked)
        
#the object is the actual GUI
gui = Cacti()
gui.mainloop

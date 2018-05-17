from tkinter import *
from tkinter import messagebox

#the class
class Newsletter(Tk):

    def __init__(self):
        Tk.__init__(self)

        #load images
        self.default = PhotoImage(file="default.gif")
        self.filled = PhotoImage(file="filled.gif")
        self.empty = PhotoImage(file="empty.gif")

        #style the window
        self.configure(padx=10, pady=10, bg='#eee')

        #add components
        self.add_heading_label()
        self.add_instructional_label()
        self.add_email_frame()
        self.add_type_frame()
        self.add_subscribe_button()

    def add_heading_label(self):
        #create component
        self.heading_label = Label(text="RECEIVE OUR NEWSLETTER")
        self.heading_label.pack(fill=X)
        self.heading_label.configure(font="Arial 14", pady=10)

    def add_instructional_label(self):
        #create component
        self.instructional_label = Label(text="Please enter your email below to receive our newsletter.")
        self.instructional_label.pack(fill=X)
        #style component
        self.instructional_label.configure(padx=10, pady=10, justify=LEFT)

    def add_email_frame(self):
        #create frame
        self.email_frame = Frame()
        self.email_frame.pack()
        #create label
        self.email_label = Label(self.email_frame, text="Email: ")
        self.email_label.pack(side=LEFT)
        #create entry
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side=LEFT)
        #create image label
        self.image_label = Label(self.email_frame, image=self.default)
        self.image_label.pack(side=LEFT)
        #style
        self.email_frame.configure()
        self.email_label.configure(padx=10, pady=10)
        self.email_entry.configure(bd=2, fg="#f00", width=30)
        self.image_label.configure(padx=10)
        #events
        self.email_entry.bind("<KeyRelease>", self.validation)

    def add_type_frame(self):
        #create frame
        self.type_frame = Frame()
        self.type_frame.pack()
        #create label
        self.type_label = Label(self.type_frame, text="Type: ")
        self.type_label.pack(side=LEFT)
        #create dropdown
        self.type_choices = ['Weekly', 'Monthly', 'Yearly']
        self.type_selected = StringVar()
        self.type_selected.set('Weekly')
        self.type_optionmenu = OptionMenu(self.type_frame, self.type_selected, *self.type_choices)
        self.type_optionmenu.pack()
        #style
        self.type_frame.configure()
        self.type_label.configure(padx=10, pady=10)
        self.type_optionmenu.configure(bd=2, width=30)

    def add_subscribe_button(self):
        #create
        self.subscribe_button = Button(text="Subscribe")
        self.subscribe_button.pack(fill=X)
        #style
        self.subscribe_button.configure()
        #events
        self.subscribe_button.bind("<ButtonRelease-1>", self.message_box)

    def message_box(self, event):
        if (self.email_entry.get() == ""):
            messagebox.showinfo("Newsletter", "Please enter your email!")
        elif (self.type_selected.get() == "Weekly"):
            messagebox.showinfo("Newsletter", "You have subscribed to the weekly newsletter! You will receive this every Monday.")
        elif (self.type_selected.get() == "Monthly"):
            messagebox.showinfo("Newsletter", "You have subscribed to the monthly newsletter! You will receive this on the first day of each month.")
        elif (self.type_selected.get() == "Yearly"):
            messagebox.showinfo("Newsletter", "You have subscribed to the yearly newsletter! You will receive this at the start of each year.")
        else:
            messagebox.showinfo("Newsletter", "Subscribed")

    def validation(self, event):
        if (self.email_entry.get() == ""):
            self.image_label.configure(image=self.empty)
        else:
            self.image_label.configure(image=self.filled)




        
#the object
gui = Newsletter()
gui.title("Newsletter")
gui.mainloop()

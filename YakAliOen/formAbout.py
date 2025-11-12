from tkinter import *
import tkinter.messagebox as messagebox
class FormAbout(Toplevel):
    def __init__(self, main):
        Toplevel.__init__(self, main)
        self.title("About")
        self.geometry("300x200")
        self.create_widgets()
        self.resizable(width=False, height=False)
    def home(self):
        mainframe = Frame(self, width=400, height=200)
        mainframe.pack(fill=BOTH, expand=YES)
        fr = Frame(mainframe, bg="white", bd=5)
        fr.pack(fill=BOTH, expand=YES)
        Label(fr, text="This is the About form.", bg="white").pack(pady=20)
        Label(fr, text="Copyright @ yakobus_12sa", font=("Arial", 16)).pack(pady=5)
        Frame(fr, bg="white", height=2).pack(fill=X, pady=10, expand=YES)
        #frame bawah
        fr_bawah = Frame(mainframe, bg="white", bd=5)
        fr_bawah.pack(fill=BOTTOM, pady=5, expand=YES)

    def create_widgets(self):
        label = Label(self, text="This is the About form.")
        label.pack(pady=20)

        button = Button(self, text="OK", command=self.on_ok)
        button.pack(pady=10)

    def on_ok(self):
        self.destroy()
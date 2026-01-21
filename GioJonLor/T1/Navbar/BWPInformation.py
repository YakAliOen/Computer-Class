from tkinter import *
import tkinter.messagebox as TKM
class BWPInfo(Toplevel):
    def __init__(self, main):
        Toplevel.__init__(self,main)
        self.geometry("300x150")
        self.resizable(width=False, height=False)
        self.title("About BWP")
        self.home()
    def home(self):
        MainFrame = Frame(self,width=400,height=200)
        MainFrame.pack(fill=BOTH, expand=YES)
        fr = Frame(MainFrame, bg="white", bd=5)
        fr.pack(fill=BOTH,expand=YES)
        Label(fr,text="This is an app created by Rowan Wissen to display his proudest work for fun and for no other reason", wraplength=200).pack()
        Frame(fr,borderwidth=2,height=2,bg="black").pack(pady=5,expand=YES)

        fr_lower = Frame(MainFrame)
        fr_lower.pack(side=BOTTOM, pady=5)

if __name__ == '__main__':
    root=Tk()
    root.mainloop()



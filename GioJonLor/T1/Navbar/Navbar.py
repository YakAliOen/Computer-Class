from tkinter import *
from BWPInformation import BWPInfo
class MainMenu():
    def __init__(self, main, title):
        self.main = main
        main.title(title)
        main.geometry("500x250")
        self.navbar()
        # setting awal
        
    def navbar(self):
        # atur main frame 
        MainFrame = Frame(self.main)
        MainFrame.pack(fill=BOTH, expand=YES)
        TestLabel = Label(MainFrame, text="Test")
        TestLabel.pack()
        
        # setting tampilan menu
        self.mainMenu = Menu(self.main)
        self.main.config(menu=self.mainMenu)      

        # sub menu :: first
        self.first = Menu(self.mainMenu)
        self.first.add_command(label="LogIn", underline=0)
        self.first.add_command(label="LogOut", underline=1)
        self.first.add_command(label="Register", underline=2)
        self.first.add_separator()
        self.mainMenu.add_cascade(label='Home', menu=self.first, underline=0)
        
        # sub menu :: Input Data
        self.input = Menu(self.mainMenu)
        self.input.add_command(label="Books", underline=0)
        self.input.add_command(label="Art", underline=1)
        self.input.add_command(label="Fandoms", underline=2)
        self.input.add_separator()
        self.mainMenu.add_cascade(label='Product', menu=self.input, underline=0) 

        # sub menu :: Sistem
        self.system = Menu(self.mainMenu)
        self.system.add_command(label="Information",underline=0, command=self.Information)
        self.system.add_cascade(label="Settings", underline=1)
        self.system.add_separator()
        self.mainMenu.add_cascade(label="System", menu=self.system, underline=0)

    def Information(self):
        BWPInfo(self.main)


        
   
        
if __name__ == '__main__':
    root = Tk()
    aplikasi = MainMenu(root, "Brief Weird Portfolio (BWP)")
    root.mainloop()

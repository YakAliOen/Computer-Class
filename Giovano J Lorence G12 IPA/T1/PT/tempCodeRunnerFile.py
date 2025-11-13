from tkinter import *

class MainMenu():
    def __init__(self, main):
        self.main = main
        main.title("Rowisia Airport Database Terminal (RADT)")
        main.geometry("500x250")
        self.navbar()
        # setting awal
        
    def navbar(self):
        # atur main frame 
        MainFrame = Frame(self.main)
        MainFrame.pack(fill=BOTH, expand=YES)
        TestLabel = Label(MainFrame, text="Welcome to Rowisia Airport Database Terminal")
        TestLabel.pack()
        
        # setting tampilan menu
        self.mainMenu = Menu(self.main)
        self.main.config(menu=self.mainMenu)      

        # sub menu :: first
        self.mainMenu.add_command(label="LogIn")
        self.mainMenu.add_command(label="LogOut")
        self.mainMenu.add_command(label="Register")
        self.mainMenu.add_separator()  # Add a separator between groups

if __name__ == '__main__':
    root = Tk()
    aplikasi = MainMenu(root)
    root.mainloop()

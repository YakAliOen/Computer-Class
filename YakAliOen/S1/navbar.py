from tkinter import *
import formAbout

class MenuUtama():
    def __init__(self, main, title):
        self.main = main
        main.title(title)
        main.geometry("500x500")
        self.navbar()
        # setting awal
        
    def navbar(self):
        # atur main frame 
        MainFrame = Frame(self.main)
        MainFrame.pack(fill=BOTH, expand=YES)
        
        # setting tampilan menu
        self.mainMenu = Menu(self.main)
        self.main.config(menu=self.mainMenu)      

        # sub menu :: Utama
        self.utama = Menu(self.mainMenu, tearoff=0)
        self.utama.add_command(label='Login', underline=0)
        self.utama.add_command(label='Logout', underline=1)
        self.utama.add_separator()
        self.mainMenu.add_cascade(label='Home', 
            menu=self.utama, underline=0)

        # sub menu :: Input Data
        self.input = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label='Product', 
            menu=self.input, underline=0) 

        # sub menu :: Sistem
        self.sistem = Menu(self.mainMenu, tearoff=0)
        self.sistem.add_command(label='Tentang Program', underline=0, command=self.about)
        self.mainMenu.add_cascade(label='Sistem', 
            menu=self.sistem, underline=0) 
    
    def about(self):   # <-- fixed: moved outside navbar()
        formAbout.FormAbout(self.main)


if __name__ == '__main__':
    root = Tk()
    aplikasi = MenuUtama(root, ":: py ;; ")
    root.mainloop()

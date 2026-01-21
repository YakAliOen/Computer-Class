from tkinter import *
import mysql.connector

class AddInfo():
    def __init__(self, main):
        self.main = main
        main.title("Add Pilot Info")
        main.geometry("400x400")
        self.navbar()

    def navbar(self):
        # Setup 
        MainFrame = Frame(self.main)
        MainFrame.grid(row=0, column=0, sticky="nsew")
        Connection = mysql.connector.connect(host="localhost", user="root", password="", port="3306", database="giovano_g12sca")
        c = Connection.cursor()

        #Label
        NameLabel = Label(MainFrame, text="Name: ", font=("Arial", 10, "bold"))
        MaskapaiLabel = Label(MainFrame, text="Maskapai: ", font=("Arial", 10, "bold"))
        AgeLabel = Label(MainFrame, text="Age: ", font=("Arial", 10, "bold"))
        ToeflLabel = Label(MainFrame, text="TOEFL Score: ", font=("Arial", 10, "bold"))
        HeightLabel = Label(MainFrame, text="Height: ", font=("Arial", 10, "bold"))
        WeightLabel = Label(MainFrame, text="Weight: ", font=("Arial", 10, "bold"))


        #Inputs
        NameInput = Entry(MainFrame)
        MaskapaiInput = Entry(MainFrame)
        AgeInput = Entry(MainFrame)
        ToeflInput = Entry(MainFrame)
        HeightInput = Entry(MainFrame)
        WeightInput = Entry(MainFrame)


        #Gridding
        #Labels
        NameLabel.grid(row= 0, column= 0, sticky='W')
        MaskapaiLabel.grid(row= 1, column=0, sticky='W')
        AgeLabel.grid(row= 2, column= 0, sticky='W') 
        ToeflLabel.grid(row= 3, column= 0, sticky='W') 
        HeightLabel.grid(row= 4, column= 0, sticky='W') 
        WeightLabel.grid(row= 5, column= 0, sticky='W')
        #Entries
        NameInput.grid(row= 0, column= 1)
        MaskapaiInput.grid(row= 1, column= 1)
        AgeInput.grid(row= 2, column= 1)
        ToeflInput.grid(row= 3, column= 1)
        HeightInput.grid(row= 4, column= 1)
        WeightInput .grid(row= 5, column= 1)
        #Submit Function
        def insertData():
            #Call past vars
            Name = NameInput.get().upper()
            Maskapai = MaskapaiInput.get()
            Age = AgeInput.get()
            Toefl = ToeflInput.get()
            Height = HeightInput.get()
            Weight = WeightInput.get()
            insert_query = "INSERT INTO `pilot` (`NAME`, `MASKAPAI`, `AGE`,`TOEFL_SCORE`,`HEIGHT`,`WEIGHT` ) VALUES (%s, %s, %s, %s, %s, %s)"

            data = (Name, Maskapai, Age, Toefl, Height, Weight)
            c.execute(insert_query, data)
            #execute runs query database
            Connection.commit()
            #Commit saves changes to database

            NameInput.delete(0, END)
            MaskapaiInput.delete(0, END)
            AgeInput.delete(0, END)
            ToeflInput.delete(0, END)
            HeightInput.delete(0, END)
            WeightInput.delete(0, END)

            # Create a Toplevel window
            popup_window = Toplevel()
            popup_window.wm_title("Data Inputted")
            popup_window.geometry("300x200") # Set the size of the popup

            # Add widgets to the popup window
            label = Label(popup_window, text="Your data has been saved!")
            label.pack(pady=20)

            # Button to close the popup
            close_button = Button(popup_window, text="Close", command=popup_window.destroy)
            close_button.pack(pady=10)

        
        #Buttons
        submit_button = Button(MainFrame, text="Submit Data", command= insertData)
        submit_button.grid(row=6, column=0, columnspan= 2, pady=10, padx=10, sticky="nsew")


        self.mainMenu = Menu(self.main)
        self.main.config(menu=self.mainMenu)      

        # SImple MEnu
        self.mainMenu.add_command(label="Add Info")
        self.mainMenu.add_command(label="Delete Info", command= self.DeleteInfo)

    def DeleteInfo(self):
        from Del import Delinfo
        Delinfo (self.main)




if __name__ == '__main__':
    root = Tk()
    aplikasi = AddInfo(root)
    root.mainloop()

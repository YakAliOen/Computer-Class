from tkinter import *
import mysql.connector


class Delinfo():
    def __init__(self, main):
        self.main = main
        main.title("Delete Pilot Info")
        main.geometry("400x400")
        self.Delete()
    def Delete(self):
        MainFrame = Frame(self.main)
        MainFrame.grid(row=0, column=0, sticky="nsew")
        Connection = mysql.connector.connect(host="localhost", user="root", password="", port="3306", database="giovano_g12sca")
        c = Connection.cursor()
        fr_lower = Frame(MainFrame)
        fr_lower.grid(row=99, column=0, sticky="ew", pady=5)

        DelNameLabel = Label(MainFrame, text= "Delete this Name: ", font=("Arial", 10, "bold"))
        DelNameEntry = Entry(MainFrame)
        DelNameLabel.grid(row= 8, column= 0, sticky='W')
        DelNameEntry.grid(row= 8, column=1)
        def DeleteData():
                DelName = DelNameEntry.get().upper()
                c.execute("DELETE FROM `pilot` WHERE `Name`= %s ", (DelName,))
                Connection.commit()
                DelNameEntry.delete(0, END)

                # Create a Toplevel window
                popup_window = Toplevel()
                popup_window.wm_title("Data Deleted")
                popup_window.geometry("300x200") # Set the size of the popup

                # Add widgets to the popup window
                label = Label(popup_window, text="Your data has been deleted!")
                label.pack(pady=20)

                # Button to close the popup
                close_button = Button(popup_window, text="Close", command=popup_window.destroy)
                close_button.pack(pady=10)
        DeleteButton = Button(MainFrame, text="Delete Data", command= DeleteData)
        DeleteButton.grid(row=11, column=0, columnspan= 2, pady=10, padx=10, sticky="nsew")

        self.mainMenu = Menu(self.main)
        self.main.config(menu=self.mainMenu)      

        self.mainMenu.add_command(label="Add Info", command= self.AddInfo)
        self.mainMenu.add_command(label="Delete Info")

    def AddInfo(self):
        from Add import AddInfo
        AddInfo(self.main)

if __name__ == '__main__':
    root=Tk()
    root.mainloop()


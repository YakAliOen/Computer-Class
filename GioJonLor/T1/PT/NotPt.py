#### NOT THE PT BUKAN PT
#### USE ADD.PY
#### THIS FILE IS NOT THE PT
from tkinter import *
import mysql.connector
#### USE ADD.PY
#Layout
main = Tk()
main.geometry("400x400")
main.title("Pilot Database")
Connection = mysql.connector.connect(host="localhost", user="root", password="", port="3306", database="giovano_g12sca")
c = Connection.cursor()


#Label
NameLabel = Label(main, text="Name: ", font=("Arial", 10, "bold"))
MaskapaiLabel = Label(main, text="Maskapai: ", font=("Arial", 10, "bold"))
AgeLabel = Label(main, text="Age: ", font=("Arial", 10, "bold"))
ToeflLabel = Label(main, text="TOEFL Score: ", font=("Arial", 10, "bold"))
HeightLabel = Label(main, text="Height: ", font=("Arial", 10, "bold"))
WeightLabel = Label(main, text="Weight: ", font=("Arial", 10, "bold"))
DelNameLabel = Label(main, text= "Delete this Name: ", font=("Arial", 10, "bold"))


#Inputs
NameInput = Entry()
MaskapaiInput = Entry()
AgeInput = Entry()
ToeflInput = Entry()
HeightInput = Entry()
WeightInput = Entry()
DelNameEntry = Entry()


#Gridding
#Labels
NameLabel.grid(row= 0, column= 0, sticky='W')
MaskapaiLabel.grid(row= 1, column=0, sticky='W')
AgeLabel.grid(row= 2, column= 0, sticky='W') 
ToeflLabel.grid(row= 3, column= 0, sticky='W') 
HeightLabel.grid(row= 4, column= 0, sticky='W') 
WeightLabel.grid(row= 5, column= 0, sticky='W')
DelNameLabel.grid(row= 8, column= 0, sticky='W')
#Entries
NameInput.grid(row= 0, column= 1)
MaskapaiInput.grid(row= 1, column= 1)
AgeInput.grid(row= 2, column= 1)
ToeflInput.grid(row= 3, column= 1)
HeightInput.grid(row= 4, column= 1)
WeightInput .grid(row= 5, column= 1)
DelNameEntry.grid(row= 8, column=1)
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


#Buttons
submit_button = Button(main, text="Submit Data", command= insertData)
submit_button.grid(row=6, column=0, columnspan= 2, pady=10, padx=10, sticky="nsew")

DeleteButton = Button(main, text="Delete Data", command= DeleteData)
DeleteButton.grid(row=11, column=0, columnspan= 2, pady=10, padx=10, sticky="nsew")

#Run
main.mainloop()
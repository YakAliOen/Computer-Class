from tkinter import *
import mysql.connector    

#Layout
main = Tk()
main.geometry("300x300")
main.title("STUCO Database")
Connection = mysql.connector.connect(host="localhost", user="root", password="", port="3306", database="giovano_g12sca")
c = Connection.cursor()

#Label
NameLabel = Label(main, text="Name: ", font=("Arial", 10, "bold"))
GradeLabel = Label(main, text="Grade: ", font=("Arial", 10, "bold"))
GenderLabel = Label(main, text="Gender: ", font=("Arial", 10, "bold"))
VisionLabel = Label(main, text= "Vision: ", font=("Arial", 10, "bold"))
MissionLabel = Label(main, text="Mission: ", font=("Arial", 10, "bold"))

DelNameLabel = Label(main, text= "Delete this Name: ", font=("Arial", 10, "bold"))

#Grid
NameLabel.grid(row= 0, column= 0, sticky='W')
GradeLabel.grid(row= 1, column=0, sticky='W')
GenderLabel.grid(row= 2, column= 0, sticky='W') 
VisionLabel.grid(row= 4, column= 0, sticky='W') 
MissionLabel.grid(row= 5, column= 0, sticky='W')
DelNameLabel.grid(row= 8, column= 0, sticky='W')

#Input
NameEntry = Entry()
GradeEntry = Entry()
GenderEntry = StringVar()
GenderEntry.set("Male")
VisionEntry = Entry()
MissionEntry = Entry()
DelNameEntry = Entry()

#Grid Input
NameEntry.grid(row=0, column=1) 
GradeEntry.grid(row=1, column=1)
Radiobutton(main, text='Male', variable=GenderEntry, value="Male").grid(row=2, column=1, sticky='W')
Radiobutton(main, text='Female', variable=GenderEntry, value="Female").grid(row=3, column=1, sticky='W')
VisionEntry.grid(row=4, column=1)
MissionEntry.grid(row=5, column=1)
DelNameEntry.grid(row= 8, column=1)
#Submit
def InsertData():
    Name = NameEntry.get().upper()
    Grade = GradeEntry.get()
    Gender = GenderEntry.get()
    Vision = VisionEntry.get().upper()
    Mission = MissionEntry.get().upper()

    insert_query = "INSERT INTO `STUCO` (`Name`, `Grade`, `Gender`, `Vision`, `Mission` ) VALUES (%s, %s, %s, %s, %s)"

    data = (Name, Grade, Gender, Vision, Mission)
    c.execute(insert_query, data)

    Connection.commit()
    NameEntry.delete(0, END)
    GradeEntry.delete(0, END)
    VisionEntry.delete(0, END)
    MissionEntry.delete(0, END)

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
    c.execute("DELETE FROM `STUCO` WHERE `Name`= %s ", (DelName,))
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


#Button
SubmitButton = Button(main, text="Submit Data", command= InsertData)
SubmitButton.grid(row=7, column=0, columnspan= 2, pady=10, padx=10, sticky="nsew")

#Button
DeleteButton = Button(main, text="Delete Data", command= DeleteData)
DeleteButton.grid(row=11, column=0, columnspan= 2, pady=10, padx=10, sticky="nsew")

#RUN
main.mainloop()

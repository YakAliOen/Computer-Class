#NOT THE CLASSWORK NOT THE CLASSWORK

from tkinter import *
import mysql.connector

#Layout
main = Tk()
main.geometry("400x400")
main.title("STUCO Database")
Connection = mysql.connector.connect(host="localhost", user="root", password="", port="3306", database="giovano_g12sca")
c = Connection.cursor()

#Label
NameLabel = Label(main, text="Name")
GradeLabel = Label(main, text="Grade(In integer, for example g11 = 11)")
GenderLabel = Label(main, text="Gender")
VisionLabel = Label(main, text= "Vision")
MissionLabel = Label(main, text="Mission")

#Grid
NameLabel.grid(row= 0, column= 0)
GradeLabel.grid(row= 1, column=0)
GenderLabel.grid(row= 2, column= 0) 
VisionLabel.grid(row= 3, column= 0) 
MissionLabel.grid(row= 4, column= 0)

#Input
NameEntry = Entry()
GradeEntry = Entry()
GenderEntry = Entry()
VisionEntry = Entry()
MissionEntry = Entry()

#Grid Input
NameEntry.grid(row=0, column=1)
GradeEntry.grid(row=1, column=1)
GenderEntry.grid(row=2, column=1)
VisionEntry.grid(row=3, column=1)
MissionEntry.grid(row=4, column=1)

#Submit
def insertData():
    Name = NameEntry.get()
    Grade = GradeEntry.get()
    Gender = GenderEntry.get()
    Vision = VisionEntry.get()
    Mission = MissionEntry.get()

    insert_query = "INSERT INTO `STUCO` (`Name`, `Grade`, `Gender`, `Vision`, `Mission` ) VALUES (%s, %s, %s, %s, %s)"

    data = (Name, Grade, Gender, Vision, Mission)
    c.execute(insert_query, data)

    Connection.commit()

#Button
SubmitButton = Button(main, text="Submit Data", command= insertData)
SubmitButton.grid(row=6, column=0, columnspan= 2, pady=10, padx=10, sticky="nsew")

#RUN
main.mainloop()

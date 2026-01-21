from tkinter import *
import mysql.connector

#Layout
main = Tk()
main.geometry("400x400")
main.title("TKinter Database")
Connection = mysql.connector.connect(host="localhost", user="root", password="", port="3306", database="giovano_g12sca")
c = Connection.cursor()

#Label
EmailLabel = Label(main, text="Email")
UserLabel = Label(main, text="Username")
PassLabel = Label(main, text="Password")

#Grid
EmailLabel.grid(row= 0, column= 0)
UserLabel.grid(row= 1, column=0)
PassLabel.grid(row= 2, column= 0) 

#Input
EmailEntry = Entry()
UserEntry = Entry()
PassEntry = Entry()

#Grid Input
EmailEntry.grid(row=0, column=1)
UserEntry.grid(row=1, column=1)
PassEntry.grid(row=2, column=1)

#Submit Function
def insertData():
    #Call past vars
    Email = EmailEntry.get()
    User = UserEntry.get()
    Pass = PassEntry.get()
    insert_query = "INSERT INTO `user` (`Email`, `Username`, `Password` ) VALUES (%s, %s, %s)"
    #Register_user is the table name in the database
    #Email, Username, Password is the data names in the table
    data = (Email, User, Pass)
    c.execute(insert_query, data)
    #execute runs query database
    Connection.commit()
    #Commit saves changes to database


#Submit
submit_button = Button(main, text="Submit Data", command= insertData)
submit_button.grid(row=4, column=0, columnspan= 2, pady=10, padx=10, sticky="nsew")

#Run
main.mainloop()
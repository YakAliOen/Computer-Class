from tkinter import *
import mysql.connector

app = Tk()
app.geometry("400x400")
app.title("Tkinter database")

connection = mysql.connector

label_email = Label(app, text = "Email", padx = 25, pady = 25)
label_username = Label(app, text = "Username", padx = 25, pady = 25)
label_password = Label(app, text = "Password", padx = 25, pady = 25)

label_email.grid(row = 0, column = 0)
label_username.grid(row = 1, column = 0)
label_password.grid(row = 2, column = 0)

entry_email = Entry()
entry_username = Entry()
entry_password = Entry()

entry_email.grid(row = 0, column = 1)
entry_username.grid(row = 1, column = 1)
entry_password.grid(row = 2, column = 1)

submit_button = Button(app, text = "Submit", command = submit)
submit_button.grid(columnspan = 2)

app.mainloop()
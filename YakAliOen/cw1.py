from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import mysql.connector

app = Tk()
app.geometry("400x500")
app.title("STUCO")

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    port = "3306",
    database = "yakobus_12sa"
)

def insertstuco():
    try:
        name = entry_name.get()
        grade = entry_grade.get()
        gender = entry_gender.get()
        visi = entry_visi.get()
        misi = entry_misi.get()
        cursor = connection.cursor()
        sql = "INSERT INTO stuco (name, grade, gender, visi, misi) VALUES (%s, %s, %s, %s, %s)"
        values = (name, grade, gender, visi, misi)
        cursor.execute(sql, values)
        connection.commit()
        print("Insert successful!")
        messagebox.showinfo("Success", "Insert successful!")
    except Exception as e:
        print("Error: ", e)

def deletestuco():
    try:
        name = entry_name.get()
        grade = entry_grade.get()
        gender = entry_gender.get()
        visi = entry_visi.get()
        misi = entry_misi.get()
        cursor = connection.cursor()
        sql = "DELETE FROM stuco WHERE name = %s AND grade = %s AND gender = %s AND visi = %s AND misi = %s"
        values = (name, grade, gender, visi, misi)
        cursor.execute(sql, values)
        connection.commit()
        print("Delete successful!")
        messagebox.showinfo("Success", "Delete successful!")
    except Exception as e:
        print("Error: ", e)


label_name = Label(app, text = "Name", font = "Helvetica 12 bold", padx = 25, pady = 15)
label_grade = Label(app, text = "Grade", font = "Helvetica 12 bold", padx = 25, pady = 15)
label_gender = Label(app, text = "Gender", font = "Helvetica 12 bold", padx = 25, pady = 15)
label_visi = Label(app, text = "Visi", font = "Helvetica 12 bold", padx = 25, pady = 15)
label_misi = Label(app, text = "Misi", font = "Helvetica 12 bold", padx = 25, pady = 15)

label_name.grid(row = 0, column = 0)
label_grade.grid(row = 1, column = 0)
label_gender.grid(row = 2, column = 0)
label_visi.grid(row = 3, column = 0)
label_misi.grid(row = 4, column = 0)

entry_name = Entry()
entry_grade = Entry()
entry_gender = Entry()
entry_visi = Entry()
entry_misi = Entry()

entry_name.grid(row = 0, column = 1)
entry_grade.grid(row = 1, column = 1)
entry_gender.grid(row = 2, column = 1)
entry_visi.grid(row = 3, column = 1)
entry_misi.grid(row = 4,  column = 1)

insert_button = Button(
    app,
    text = "Insert",
    command = insertstuco,
    bg = "#4CAF50",
    fg = "white",
    font = ("Arial", 12, "bold"),
    padx = 20,
    pady = 10,
    relief = "raised",  
    bd = 3
)
insert_button.grid(columnspan=2, pady=20)

delete_button = Button(
    app,
    text = "Delete",
    command = deletestuco,
    bg = "#4CAF50",
    fg = "white",
    font = ("Arial", 12, "bold"),
    padx = 20,
    pady = 10,
    relief = "raised",  
    bd = 3
)
delete_button.grid(columnspan=2, pady=20)

app.mainloop()
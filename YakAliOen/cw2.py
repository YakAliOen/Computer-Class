import tkinter as tk
from tkinter import messagebox
import mysql.connector

connection = mysql.connector.connect
(
    host="localhost",
    user="root",
    port="3306",
    database="yakobus_12sa"
)

app = tk.Tk()
app.title("School Management")
app.geometry("600x500")

nav_frame = tk.Frame(app, bg = "#333333", height=50)
nav_frame.pack(fill="x")

content_frame = tk.Frame(app, bg = "white")
content_frame.pack(expand=True, fill="both")

pages = {}

def show_page(page_name):
    frame = pages[page_name]
    frame.tkraise()

home_page = tk.Frame(content_frame, bg = "white")
tk.Label(home_page, text = "Navbar Tkinter GUI", font = ("Arial", 16), bg = "white").pack(expand=True)
pages["Home"] = home_page

students_page = tk.Frame(content_frame, bg = "white")
pages["Students"] = students_page

tk.Label(students_page, text = "Name", font = ("Arial", 12), pady = 5).grid(row = 0, column = 0, padx = 10, sticky = "w")
tk.Label(students_page, text = "Grade", font = ("Arial", 12), pady = 5).grid(row = 1, column = 0, padx = 10, sticky = "w")
tk.Label(students_page, text = "Gender", font = ("Arial", 12), pady = 5).grid(row = 2, column = 0, padx = 10, sticky = "w")
tk.Label(students_page, text = "Visi", font = ("Arial", 12), pady = 5).grid(row = 3, column = 0, padx = 10, sticky = "w")
tk.Label(students_page, text = "Misi", font = ("Arial", 12), pady = 5).grid(row = 4, column = 0, padx = 10, sticky = "w")

entry_name = tk.Entry(students_page)
entry_grade = tk.Entry(students_page)
entry_gender = tk.Entry(students_page)
entry_visi = tk.Entry(students_page)
entry_misi = tk.Entry(students_page)

entry_name.grid(row = 0, column = 1, pady = 5)
entry_grade.grid(row = 1, column = 1, pady = 5)
entry_gender.grid(row = 2, column = 1, pady = 5)
entry_visi.grid(row = 3, column = 1, pady = 5)
entry_misi.grid(row = 4, column = 1, pady = 5)

def insert_student():
    try:
        name = entry_name.get()
        grade = entry_grade.get()
        gender = entry_gender.get()
        visi = entry_visi.get()
        misi = entry_misi.get()
        cursor = connection.cursor()
        sql = "INSERT INTO stuco (name, grade, gender, visi, misi) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (name, grade, gender, visi, misi))
        connection.commit()
        messagebox.showinfo("Success", "Student inserted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_student():
    try:
        name = entry_name.get()
        cursor = connection.cursor()
        sql = "DELETE FROM stuco WHERE name = %s"
        cursor.execute(sql, (name,))
        connection.commit()
        messagebox.showinfo("Success", f"Student '{name}' deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

tk.Button(students_page, text = "Insert", bg = "#4CAF50", fg = "white", font = ("Arial", 12, "bold"), command = insert_student).grid(row = 5, column = 0, pady = 15, padx = 10)

tk.Button(students_page, text = "Delete", bg = "#F44336", fg = "white", font = ("Arial", 12, "bold"), command = delete_student).grid(row = 5, column = 1, pady = 15, padx = 10)

teachers_page = tk.Frame(content_frame, bg = "white")
tk.Label(teachers_page, text = "👨‍🏫 Teachers Page (coming soon)", font = ("Arial", 16), bg = "white").pack(expand=True)
pages["Teachers"] = teachers_page

for page in pages.values(): page.place(in_ = content_frame, relwidth = 1, relheight = 1)

btn_home = tk.Button(nav_frame, text = "Home", fg = "white", bg = "#444444", command = lambda: show_page("Home"))
btn_students = tk.Button(nav_frame, text = "Students", fg = "white", bg = "#444444", command = lambda: show_page("Students"))
btn_teachers = tk.Button(nav_frame, text = "Teachers", fg = "white", bg = "#444444", command = lambda: show_page("Teachers"))

btn_home.pack(side = "left", padx = 10, pady = 10)
btn_students.pack(side = "left", padx = 10, pady = 10)
btn_teachers.pack(side = "left", padx = 10, pady = 10)

show_page("Home")

app.mainloop()
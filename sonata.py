from tkinter import *
import tkinter as tk
import mysql.connector
from PIL import Image, ImageTk
from tkinter import messagebox

main = Tk()
main.geometry("700x1100")
main.title("Aplikasi Fast Food Drive Thru")
connection = mysql.connector.connect(host = 'localhost', user = 'root', password = '', port = '3306', database = 'katherine_sonata_12sca')

c = connection.cursor()

logo_img = Image.open("pilot.gif")
logo_img = ImageTk.PhotoImage(logo_img)
logo_1 = Label(main, image = logo_img)
logo_1.pack()

#list nama restaurants
RESTAURANTS = ("MCDONALD'S", "KFC", "BURGER KING", "PIZZA HUT", "DOMINO'S PIZZA")

#register
login = False

#function untuk open login
def open_login():
    login_win = Toplevel(main) 
    login_win.title("Login")
    login_win.geometry("300x180")

    Label(login_win, text="Username").pack(pady=5)
    user_entry = Entry(login_win)
    user_entry.pack()

    Label(login_win, text="Password").pack(pady=5)
    pass_entry = Entry(login_win, show="*")
    pass_entry.pack()

    def check_login():
        username = user_entry.get().strip()
        password = pass_entry.get().strip()

        # Contoh login sederhana (bisa disesuaikan dengan tabel MySQL)
        if username == "admin" and password == "123":
            global logged_in
            logged_in = True
            messagebox.showinfo("Login", "Login successful!")
            user.entryconfig("Users", state="normal")
            login_win.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    Button(login_win, text="Login", command=check_login, bg="green", fg="white").pack(pady=10)

#halaman register
page1 = Frame(main)
title_label = Label(page1, text = "Resgister Fast Food Drive Thru Employee")
title_label.pack(pady=10)


name_label = Label(page1, text="Name")
name_label.pack()
name_entry = Entry(page1)
name_entry.pack()

language_label = Label(page1, text="Language")
language_label.pack()
language_entry = Entry(page1)
language_entry.pack()

experience_label = Label(page1, text="Experience")
experience_label.pack()
experience_entry = Entry(page1)
experience_entry.pack()

age_label = Label(page1, text="Age")
age_label.pack()
age_entry = Entry(page1)
age_entry.pack()

team_label = Label(page1, text="Team")
team_label.pack()
team_entry = Entry(page1)
team_entry.pack()

page1.pack()
#halaman users
page2 = Frame(main)

#ambil dara dari form
def get_data():
    user_name = name_entry.get().upper().strip()
    if not user_name:
        messagebox.showinfo("Missing Name")
        return None
    
    try:
        user_age = int(age_entry.get())
    except ValueError:
        messagebox.showinfo("Invalid Age")
        return None
    
    try:
        user_experience = int(experience_entry.get())
    except ValueError:
        messagebox.showinfo("Invalid Years of Experience")
        return None
    
    try:
        user_language = (language_entry.get())
    except ValueError:
        messagebox.showinfo("Invalid Language")
        return None
    
    user_restaurant = team_entry.get().upper().strip()
    if user_restaurant not in RESTAURANTS:
        messagebox.showinfo("Couldn't Register", "Invalid Restaurant Name")
        return None
    
    return {
        "Name": user_name,
        "Age": user_age,
        "Experience": user_experience,
        "Language": user_language,
        "Restaurant": user_restaurant
    }

def restaurant_user():
    user_data = get_data()
    if not user_data:
        return
    query = "INSERT INTO `restaurant` (`name`, `age`, `experience`, `language`, `restaurant`) VALUES (%s, %s, %s, %s, %s)"
    c.execute(query, (
        user_data["Name"],
        user_data["Age"],
        user_data["Experience"],
        user_data["Language"],
        user_data["Restaurant"],
    ))
    connection.commit()
    messagebox.showinfo(title = "New Entry Data", message = "User Added Successfully")

def deletedata():
    user_data = get_data()
    if not user_data:
        return 1
    
    check_query = "SELECT * FROM `restaurant` WHERE `name` = %s AND `age` = %s AND `experience` = %s AND `language` = %s AND `restaurant` = %s"

    #query delete
    c.execute(check_query, (
        user_data["Name"],
        user_data["Age"],
        user_data["Experience"],
        user_data["Language"],
        user_data["Restaurant"]
    ))
    result = c.fetchone()
    if result:
        delete_user = "DELETE FROM `restaurant` WHERE `name` = %s AND `age` = %s AND `experience` = %s AND `language` = %s AND `restaurant` = %s"
        c.execute(delete_user, (
            user_data["Name"],
            user_data["Age"],
            user_data["Experience"],
            user_data["Language"],
            user_data["Restaurant"]
        ))
        connection.commit()
        #messagebox.showinfo(title = "Data Deleted", message = "User Deleted Successfully")

submit_button = Button(page1, text = "Submit", command = restaurant_user)
submit_button.pack(pady = 10, padx = 10)
delete_button = Button(page1, text = "Delete", command = deletedata)
delete_button.pack(pady = 10, padx = 10)

#navigasi antar halaman
def page_regis():
    page3.pack_forget()
    page2.pack_forget()
    page1.pack()

def page_users():
    if not login:
        messagebox.showwarning("Kamu Harus Login Dulu Ya!!!")
        return
    for widget in page2.winfo_children(): #untuk inheritance page 2
        widget.destroy()
    title = Label(page2, text = "Register User")
    title.pack(pady = 10)
    query = "SELECT name, restaurants FROM restaurant"
    c.execute(query)
    users = c.fetchall()
    if not users:
        no_data = Label(page2, text = "Data Kosong!")
        no_data.pack()
    else:
        for name, restaurant in users:
            user_label = Label(page2, text = f"Name: {name} | Restaurant: {restaurant}")
            user_label.pack()
    page1.pack_forget()
    page2.pack()

page3 = Frame(main)
def page_review():
    if not login:
        messagebox.showwarning("Kamu Harus Login Dulu Ya!!!")
        return
    for widget in page3.winfo_children():
        widget.destroy()
    title = Label(page3, text = "Our Review")
    title.pack(pady = 10)
    review_label = Label(page3, text = "Our overall review: 5 stars")
    review_label.pack()
    page1.pack_forget()
    page2.pack_forget()
    page3.pack()

#menu navbar
menu_bar = Menu(main)

#menu login
login = Menu(menu_bar, tearoff = 0)
login.add_command(label = "Login", command = open_login)
menu_bar.add_cascade(label = "Login", menu = login)

#menu register
regis = Menu(menu_bar, tearoff = 0)
regis.add_command(label = "Register", command = page_regis)
menu_bar.add_cascade(label = "Register", menu = regis)

#menu restaurants
restaurant = Menu(menu_bar, tearoff = 0)
restaurant.add_command(label = "Restaurant", command = page_users)
menu_bar.add_cascade(label = "Restaurant", menu = restaurant)

#menu user
user = Menu(menu_bar, tearoff = 0)
user.add_command(label = "User", command = page_users)
menu_bar.add_cascade(label = "User", menu = user)

#menu review
review = Menu(menu_bar, tearoff = 0)
review.add_command(label = "Review", command = page_review)
menu_bar.add_cascade(label = "Review", menu = review)

main.config(menu = menu_bar)
page_regis()
main.mainloop()

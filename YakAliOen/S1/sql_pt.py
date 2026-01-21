import tkinter as tk
from tkinter import *
import tkinter.messagebox as mb
import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    port="3306",
    database="yakobus_12sa"
)
cursor = connection.cursor()  


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("PILOT")
        self.master.geometry("500x500")
        self.master.configure(bg="#23395d")

        self.container = Frame(self.master, bg="#23395d")
        self.container.pack(fill="both", expand=True)

        self.navbar()
        self.show_login()

    def navbar(self):
        navbar = Frame(self.master, bg="#1a2940", height=40)
        navbar.pack(fill="x")

        def style_btn(btn):
            btn.configure(
                bg="#00bfff", fg="white", activebackground="#1e90ff", activeforeground="white",
                font=("Arial", 11, "bold"), bd=0, relief="flat", cursor="hand2"
            )

        login_btn = Button(navbar, text="Login", command=self.show_login)
        style_btn(login_btn)
        login_btn.pack(side="left", padx=8, pady=6)

        register_btn = Button(navbar, text="Register", command=self.show_register)
        style_btn(register_btn)
        register_btn.pack(side="left", padx=8, pady=6)

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_login(self):
        self.clear_container()
        Form(self.container, "login")

    def show_register(self):
        self.clear_container()
        Form(self.container, "register")

    def show_homepage(self, username):
        self.clear_container()
        Form(self.container, "homepage", username)


class Form:
    """
    Handles the actual forms: login, register, homepage.
    Each form is initialized with 'form_type' so we know which UI to build.
    """
    def __init__(self, parent, form_type, username=None):
        self.parent = parent
        self.form_type = form_type
        self.username = username

        if form_type == "login":
            self.login()
        elif form_type == "register":
            self.register()
        elif form_type == "homepage":
            self.homepage()

    def register(self):
        Label(self.parent, text="Register", font=("Arial", 16, "bold"), bg="#23395d", fg="#00bfff").pack(pady=10)

        def style_entry(entry):
            entry.configure(bg="#1a2940", fg="#e0eaff", insertbackground="#00bfff", font=("Arial", 11), bd=2, relief="groove")

        form_frame = Frame(self.parent, bg="#23395d")
        form_frame.pack(pady=10)

        fields = [
            ("Username", False),
            ("Password", True),
            ("Maskapai", False),
            ("Age", False),
            ("TOEFL Score", False),
            ("Height", False),
            ("Weight", False)
        ]
        self.entries = {}
        for label_text, is_password in fields:
            frame = Frame(form_frame, bg="#23395d")
            frame.pack(pady=5)
            Label(frame, text=label_text+":", font=("Arial", 11), bg="#23395d", fg="#00bfff", width=12, anchor="e").pack(side="left")
            entry = Entry(frame, show="*" if is_password else None)
            style_entry(entry)
            entry.pack(side="left", padx=5)
            self.entries[label_text.lower().replace(" ", "_")] = entry

        submit_btn = Button(form_frame, text="Submit", command=self.register_user)
        submit_btn.configure(bg="#00bfff", fg="white", activebackground="#1e90ff", activeforeground="white", font=("Arial", 12, "bold"), bd=0, relief="flat", cursor="hand2")
        submit_btn.pack(pady=12)

    def register_user(self):
        username = self.entries["username"].get()
        password = self.entries["password"].get()
        maskapai = self.entries["maskapai"].get()
        age = self.entries["age"].get()
        toefl = self.entries["toefl_score"].get()
        height = self.entries["height"].get()
        weight = self.entries["weight"].get()

        try:
            cursor.execute(
                "INSERT INTO pilot (username, password, maskapai, age, toefl, height, weight) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (username, password, maskapai, age, toefl, height, weight)
            )
            connection.commit()
            mb.showinfo("Success", "User registered successfully!")
        except mysql.connector.Error as err:
            mb.showerror("Error", f"Database error: {err}")

    def login(self):
        Label(self.parent, text="Login", font=("Arial", 16, "bold"), bg="#23395d", fg="#00bfff").pack(pady=10)

        def style_entry(entry):
            entry.configure(bg="#1a2940", fg="#e0eaff", insertbackground="#00bfff", font=("Arial", 11), bd=2, relief="groove")

        form_frame = Frame(self.parent, bg="#23395d")
        form_frame.pack(pady=10)

        fields = [
            ("Username", False),
            ("Password", True)
        ]
        self.entries = {}
        for label_text, is_password in fields:
            frame = Frame(form_frame, bg="#23395d")
            frame.pack(pady=5)
            Label(frame, text=label_text+":", font=("Arial", 11), bg="#23395d", fg="#00bfff", width=12, anchor="e").pack(side="left")
            entry = Entry(frame, show="*" if is_password else None)
            style_entry(entry)
            entry.pack(side="left", padx=5)
            self.entries[label_text.lower()] = entry

        login_btn = Button(form_frame, text="Login", command=self.login_user)
        login_btn.configure(bg="#00bfff", fg="white", activebackground="#1e90ff", activeforeground="white", font=("Arial", 12, "bold"), bd=0, relief="flat", cursor="hand2")
        login_btn.pack(pady=12)

    def login_user(self):
        username = self.entries["username"].get()
        password = self.entries["password"].get()

        cursor.execute("SELECT * FROM pilot WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()

        if user:
            mb.showinfo("Success", f"Welcome {username}!")
            app.show_homepage(username)
        else:
            mb.showerror("Error", "Invalid credentials")

    def delete_account(self):
        if self.username:
            try:
                cursor.execute("DELETE FROM pilot WHERE username=%s", (self.username,))
                connection.commit()
                mb.showinfo("Success", "Account deleted successfully!")
                app.show_login()
            except mysql.connector.Error as err:
                mb.showerror("Error", f"Database error: {err}")
        else:
            mb.showerror("Error", "No user logged in")

    def homepage(self):
        home_frame = Frame(self.parent, bg="#23395d")
        home_frame.pack(expand=True)
        Label(home_frame, text=f"Welcome, {self.username}", font=("Arial", 16, "bold"), bg="#23395d", fg="#00bfff").pack(pady=20)

        cursor.execute("SELECT maskapai, age, toefl, height, weight FROM pilot WHERE username=%s", (self.username,))
        user_data = cursor.fetchone()
        if user_data:
            labels = ["Maskapai", "Age", "TOEFL Score", "Height", "Weight"]
            for label, value in zip(labels, user_data):
                Label(home_frame, text=f"{label}: {value}", font=("Arial", 12), bg="#23395d", fg="#e0eaff").pack(pady=3)

        del_btn = Button(home_frame, text="Delete Account", command=self.delete_account)
        del_btn.configure(bg="#00bfff", fg="white", activebackground="#1e90ff", activeforeground="white", font=("Arial", 12, "bold"), bd=0, relief="flat", cursor="hand2")
        del_btn.pack(pady=12)

root = tk.Tk()
app = App(root)
root.mainloop()
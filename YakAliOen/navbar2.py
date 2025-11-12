#libraries
import tkinter as tk
from tkinter import *
import tkinter.messagebox as mb
import mysql.connector
from PIL import Image, ImageTk


#colors
BG_COLOR = "#FFFFFF"
NAV_BG = "#004080"
BTN_BG = "#004080"
BTN_FG = "white"
TITLE_COLOR = "#004080"
TEXT_COLOR = "#333333"
ENTRY_BG = "white"


#main
main = Tk()
main.geometry("910x1000")
main.title("Aplikasi Avionics")
main.configure(bg=BG_COLOR)


#db
connection = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='yakobus_12sa')
c = connection.cursor()


#logo
logo_img = Image.open(r"C:\Users\Student\Documents\Yakobus Aliano Oenkiriwang\t2\avionics.png")
logo_img = ImageTk.PhotoImage(logo_img)
logo_l = Label(main, image=logo_img, bg=BG_COLOR)
logo_l.pack(pady=10)


#systems
SYSTEM = ("Universal Avionics", "Honeywell", "Rockwell Collins","Garmin", "Avidyne", "Aspen Avionics", "Dynon Avionics", "BendixKing")


#pages
page_register = Frame(main, bg=BG_COLOR)
page_login = Frame(main, bg=BG_COLOR)
page_profile = Frame(main, bg=BG_COLOR)
page_personnel = Frame(main, bg=BG_COLOR)
list_ids = []
current_user = {}

























#functions

#showpage function
def show_page(p):
    for w in main.winfo_children():
        if isinstance(w, Frame):
            w.pack_forget()
    p.pack(fill="both", expand=True)


#logout function
def logout():
    confirm = mb.askyesno("Logout", "Are you sure you want to logout?")
    if confirm:
        main.config(menu="")
        current_user.clear()
        show_page(page_register)


#center function
def centered_container(parent):
    outer = Frame(parent, bg=BG_COLOR)
    outer.place(relx=0.5, rely=0.5, anchor=CENTER)
    return outer






















#page area

#register page
container_reg = centered_container(page_register)

lbl_reg_title = Label(container_reg, text="Register Personnel", font=("Arial", 24, "bold"), fg=TITLE_COLOR, bg=BG_COLOR) #lebels
lbl_reg_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

labels = ["Name", "Age", "Gender (Male/Female)", "Height (cm)", "Weight (kg)", "Avionic System"]
entries = {}

for i, text in enumerate(labels):
    Label(container_reg, text=text, bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11)).grid(row=i+1, column=0, padx=(0, 15), pady=8, sticky=E)

entry_reg_name = Entry(container_reg, bg=ENTRY_BG, font=("Arial", 11), width=30) #widgets
entry_reg_age = Entry(container_reg, bg=ENTRY_BG, font=("Arial", 11), width=30)
entry_reg_gender = Entry(container_reg, bg=ENTRY_BG, font=("Arial", 11), width=30)
entry_reg_height = Entry(container_reg, bg=ENTRY_BG, font=("Arial", 11), width=30)
entry_reg_weight = Entry(container_reg, bg=ENTRY_BG, font=("Arial", 11), width=30)
entry_reg_system = StringVar(container_reg)
entry_reg_system.set(SYSTEM[0])
dropdown_reg_system = OptionMenu(container_reg, entry_reg_system, *SYSTEM)
dropdown_reg_system.config(bg=BTN_BG, fg=BTN_FG, font=("Arial", 11), width=25)

widgets = [entry_reg_name, entry_reg_age, entry_reg_gender, entry_reg_height, entry_reg_weight, dropdown_reg_system]

for i, w in enumerate(widgets):
    if isinstance(w, Entry):
        w.grid(row=i+1, column=1, pady=8, sticky=W)
    else:
        w.grid(row=i+1, column=1, pady=8, sticky=W)

def register_personnel(): #register function
    name = entry_reg_name.get().upper().strip()
    age = entry_reg_age.get().strip()
    gender = entry_reg_gender.get().strip()
    height = entry_reg_height.get().strip()
    weight = entry_reg_weight.get().strip()
    system = entry_reg_system.get().strip()

    if not all([name, age, gender, height, weight]):
        mb.showerror("Error", "Please fill in all fields")
        return

    try:
        c.execute("INSERT INTO personnel (name, age, gender, height, weight, system) VALUES (%s,%s,%s,%s,%s,%s)",(name, age, gender, height, weight, system))
        connection.commit()
        mb.showinfo("Success", "Personnel registered successfully")
        for e in [entry_reg_name, entry_reg_age, entry_reg_gender, entry_reg_height, entry_reg_weight]:
            e.delete(0, END)
    except Exception as e:
        mb.showerror("Database Error", str(e))

Button(container_reg, text="Register", command=register_personnel,bg=BTN_BG, fg=BTN_FG, font=("Arial", 10, "bold"), width=12).grid(row=8, column=0, columnspan=2, pady=20) #buttons
Button(container_reg, text="Go to Login", command=lambda: show_page(page_login),bg=BTN_BG, fg=BTN_FG, font=("Arial", 10, "bold"), width=12).grid(row=9, column=0, columnspan=2)


#login page
container_log = centered_container(page_login)

lbl_login_title = Label(container_log, text="Access Personnel System", font=("Arial", 24, "bold"), fg=TITLE_COLOR, bg=BG_COLOR) #labels
lbl_login_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

Label(container_log, text="Name", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11)).grid(row=1, column=0, padx=(0, 15), pady=8, sticky=E)
Label(container_log, text="Age", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11)).grid(row=2, column=0, padx=(0, 15), pady=8, sticky=E)
Label(container_log, text="Avionic System", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11)).grid(row=3, column=0, padx=(0, 15), pady=8, sticky=E)

entry_login_name = Entry(container_log, bg=ENTRY_BG, font=("Arial", 11), width=30)
entry_login_age = Entry(container_log, bg=ENTRY_BG, font=("Arial", 11), width=30)
entry_login_system = StringVar(container_log)
entry_login_system.set(SYSTEM[0])
dropdown_login_system = OptionMenu(container_log, entry_login_system, *SYSTEM)
dropdown_login_system.config(bg=BTN_BG, fg=BTN_FG, font=("Arial", 11), width=25)

entry_login_name.grid(row=1, column=1, pady=8, sticky=W)
entry_login_age.grid(row=2, column=1, pady=8, sticky=W)
dropdown_login_system.grid(row=3, column=1, pady=8, sticky=W)

def authenticate(): #login function
    name = entry_login_name.get().upper().strip()
    age = entry_login_age.get().strip()
    system = entry_login_system.get().strip()

    if not name or not age:
        mb.showerror("Error", "Please fill in all fields")
        return

    try:
        c.execute("SELECT * FROM personnel WHERE name=%s AND age=%s AND system=%s", (name, age, system))
        result = c.fetchone()
        if result:
            mb.showinfo("Access Granted", f"Welcome aboard, {name}")
            columns = ["id", "name", "age", "gender", "height", "weight", "system"]
            current_user.update(dict(zip(columns, result)))
            setup_pages()
        else:
            mb.showerror("Access Denied", "No matching personnel found in database")
    except Exception as e:
        mb.showerror("Database Error", str(e))

Button(container_log, text="Login", command=authenticate, bg=BTN_BG, fg=BTN_FG, font=("Arial", 10, "bold"), width=12).grid(row=4, column=0, columnspan=2, pady=20) #buttons
Button(container_log, text="Back to Register", command=lambda: show_page(page_register), bg=BTN_BG, fg=BTN_FG, font=("Arial", 10, "bold"), width=15).grid(row=5, column=0, columnspan=2)


#main pages
def setup_pages():
    menubar = Menu(main) #navbar

    home_menu = Menu(menubar, tearoff=0) #home dropdown
    home_menu.add_command(label="My Profile", command=lambda: show_page(page_profile))
    home_menu.add_command(label="Personnel", command=lambda: show_page(page_personnel))
    menubar.add_cascade(label="Home", menu=home_menu)

    inside_about = "Aplikasi Avionics is an account based database program to store data regarding personnel who are certified to be under all avionics system universally; they store data about top avionics personnel around the world and from all sorts of system.\n\n\nDEFINITIONS:\n\nAvionics (a portmanteau of aviation and electronics) are the electronic systems used on aircraft. Avionic systems include communications, navigation, the display and management of multiple systems, and the hundreds of systems that are fitted to aircraft to perform individual functions.\n\nPersonnel is a noun describing a group of people who follow orders, usually at a company."
    inside_usage = (
    "USAGE POLICY AND LICENSE INFORMATION\n\n"
    "Aplikasi Avionics © 2025 Yakobus Aliano Oenkiriwang. All rights reserved.\n\n"
    "This software is designed solely for educational and organizational use to record, "
    "manage, and view personnel data related to avionics systems.\n\n"
    "By using this application, you agree to the following terms:\n"
    "1. You shall not redistribute, modify, or resell this software without written permission from the author.\n"
    "2. All data entered into the application must be accurate and authorized. Users are responsible for "
    "ensuring the privacy and legality of any stored information.\n"
    "3. The developer is not liable for any misuse of stored data, data loss, or system malfunction "
    "arising from improper usage.\n"
    "4. The application and its associated graphics, name, and logo are protected under copyright law.\n\n"
    "DATA PRIVACY NOTICE:\n"
    "The personnel data stored in this program is used solely for identification and record-keeping. "
    "No data is transmitted externally unless done manually by the user.\n\n"
    "For inquiries, contact: yakobus.avionics@gmail.com\n"
    "Version 1.0.0 — Educational License"
)
    help_menu = Menu(menubar, tearoff=0) #help button
    help_menu.add_command(label="About", command=lambda: mb.showinfo("About", inside_about))
    help_menu.add_command(label="Usage", command=lambda: mb.showinfo("Usage", inside_usage))
    menubar.add_cascade(label="Help", menu=help_menu)

    menubar.add_command(label="Logout", command=logout) #logout button
    main.config(menu=menubar)
    show_page(page_profile)

    #user profile page
    for w in page_profile.winfo_children():
        w.destroy()
    frame = centered_container(page_profile)
    Label(frame, text="User Profile", font=("Arial", 24, "bold"), fg=TITLE_COLOR, bg=BG_COLOR).grid(row=0, column=0, columnspan=2, pady=(0, 20))

    details = {
        "Name": current_user["name"],
        "Age": current_user["age"],
        "Gender": current_user["gender"],
        "Height (cm)": current_user["height"],
        "Weight (kg)": current_user["weight"],
        "Avionic System": current_user["system"]
    }
    for i, (key, value) in enumerate(details.items()): #displaying data
        Label(frame, text=f"{key}:", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 12, "bold")).grid(row=i+1, column=0, sticky=E, padx=10, pady=5)
        Label(frame, text=value, bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 12)).grid(row=i+1, column=1, sticky=W, padx=10, pady=5)

    #personnel list page
    page_personnel.configure(bg=BG_COLOR)
    list_container = Frame(page_personnel, bg=BG_COLOR)
    list_container.pack(pady=30)
    lbl_list_title = Label(list_container, text="Registered Personnel", font=("Arial", 24, "bold"), fg=TITLE_COLOR, bg=BG_COLOR)
    lbl_list_title.pack(pady=(0, 20))
    listbox = Listbox(list_container, bg=ENTRY_BG, font=("Arial", 11), selectmode=SINGLE, selectbackground=BTN_BG, selectforeground=BTN_FG, width=40, height=12)
    listbox.pack(pady=10)

    def refresh_list(): #refresh list function
        try:
            listbox.delete(0, END)
            list_ids.clear()
            c.execute("SELECT id, name, system FROM personnel ORDER BY id ASC")
            rows = c.fetchall()
            for idx, r in enumerate(rows, start=1):
                list_ids.append(r[0])
                listbox.insert(END, f"{idx}. {r[1]} ({r[2]})")
        except Exception as e:
            mb.showerror("Database Error", str(e))

    def details(): #details function
        sel = listbox.curselection()
        if not sel:
            mb.showwarning("Select", "Please select a person")
            return
        pid = list_ids[sel[0]]
        c.execute("SELECT name, age, gender, height, weight, system FROM personnel WHERE id=%s", (pid,))
        r = c.fetchone()
        if r:
            mb.showinfo("Details", f"Name: {r[0]}\nAge: {r[1]}\nGender: {r[2]}\nHeight: {r[3]} cm\nWeight: {r[4]} kg\nSystem: {r[5]}")

    def delete_personnel(): #delete personnel function
        sel = listbox.curselection()
        if not sel:
            mb.showwarning("Select", "Please select someone to delete")
            return
        pid = list_ids[sel[0]]
        if not mb.askyesno("Confirm", "Delete this record?"):
            return
        c.execute("DELETE FROM personnel WHERE id=%s", (pid,))
        connection.commit()
        refresh_list()

    btn_frame = Frame(list_container, bg=BG_COLOR) #buttons
    btn_frame.pack(pady=20)
    Button(btn_frame, text="Refresh", command=refresh_list, bg=BTN_BG, fg=BTN_FG, font=("Arial", 10, "bold"), width=12).pack(side=LEFT, padx=10)
    Button(btn_frame, text="Details", command=details, bg=BTN_BG, fg=BTN_FG, font=("Arial", 10, "bold"), width=12).pack(side=LEFT, padx=10)
    Button(btn_frame, text="Delete", command=delete_personnel, bg=BTN_BG, fg=BTN_FG, font=("Arial", 10, "bold"), width=12).pack(side=LEFT, padx=10)
    refresh_list()

























#startup
show_page(page_register)
main.mainloop()

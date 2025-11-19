import tkinter as tk
from tkinter import *
import tkinter.messagebox as mb
import mysql.connector
from PIL import Image, ImageTk


#colours
BG_COLOR = "#FFFFFF"
NAV_BG = "#004080"
BTN_BG = "#004080"
BTN_FG = "white"
TITLE_COLOR = "#004080"
TEXT_COLOR = "#333333"
ENTRY_BG = "white"


#layout
main = Tk()
main.geometry("1000x1000")
main.title("Aplikasi mcdonald")
main.configure(bg=BG_COLOR)


#database
connection = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database ='oliver_12scia')
c = connection.cursor()


#system
SYSTEM = ("mcchicken", "cheeseburger", "mcspicy", "bigmac", "smolmac")


#register
login = False
page1 = Frame(main, bg=BG_COLOR, padx=50, pady=20)


# Create a container frame for better alignment
form_container = Frame(page1, bg=BG_COLOR)
form_container.pack()


#title
title_label = Label(form_container, text="Register", font=("Arial", 24, "bold"), fg=TITLE_COLOR, bg=BG_COLOR)
title_label.grid(row=0, column=0, columnspan=2, pady=(0,20))


#create labels
lbl_name = Label(form_container, text="Name", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11))
lbl_age = Label(form_container, text="Age", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11))
lbl_gender = Label(form_container, text="Gender", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11))
lbl_height = Label(form_container, text="Height (cm)", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11))
lbl_weight = Label(form_container, text="Weight (kg)", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11))
lbl_system = Label(form_container, text="mcdonalds system", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11))


#grid weights
form_container.grid_columnconfigure(1, weight=1)


#align labels
lbl_name.grid(row=1, column=0, padx=(0,15), pady=8, sticky=E)
lbl_age.grid(row=2, column=0, padx=(0,15), pady=8, sticky=E)
lbl_gender.grid(row=3, column=0, padx=(0,15), pady=8, sticky=E)
lbl_height.grid(row=4, column=0, padx=(0,15), pady=8, sticky=E)
lbl_weight.grid(row=5, column=0, padx=(0,15), pady=8, sticky=E)
lbl_system.grid(row=6, column=0, padx=(0,15), pady=8, sticky=E)


#entry
ENTRY_WIDTH = 30


#create entries
entry_name = Entry(form_container, bg=ENTRY_BG, font=("Arial", 11), width=ENTRY_WIDTH)
entry_age = Entry(form_container, bg=ENTRY_BG, font=("Arial", 11), width=ENTRY_WIDTH)
entry_gender = Entry(form_container, bg=ENTRY_BG, font=("Arial", 11), width=ENTRY_WIDTH)
entry_height = Entry(form_container, bg=ENTRY_BG, font=("Arial", 11), width=ENTRY_WIDTH)
entry_weight = Entry(form_container, bg=ENTRY_BG, font=("Arial", 11), width=ENTRY_WIDTH)
entry_system = Entry(form_container, bg=ENTRY_BG, font=("Arial", 11), width=ENTRY_WIDTH)



#align entries
entry_name.grid(row=1, column=1, pady=8, sticky=W)
entry_age.grid(row=2, column=1, pady=8, sticky=W)
entry_gender.grid(row=3, column=1, pady=8, sticky=W)
entry_height.grid(row=4, column=1, pady=8, sticky=W)
entry_weight.grid(row=5, column=1, pady=8, sticky=W)
entry_system.grid(row=6, column=1, pady=8, sticky=W)


#initializing chicken
page2 = Frame(main)


#navbar
menubar = Menu(main)


#home dropdown navbar
home_menu = Menu(menubar, tearoff=0)
home_menu.add_command(label="Register", command=lambda: show_page(page1))
home_menu.add_command(label="chicken", command=lambda: show_page(page2))
menubar.add_cascade(label="Home", menu=home_menu)


#help navbar
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=lambda: mb.showinfo("About", "mcdonald system"))
menubar.add_cascade(label="Help", menu=help_menu)


#configure navbar
main.config(menu=menubar)


#configure chicken
page2.configure(bg=BG_COLOR)


#alignment container
list_container = Frame(page2, bg=BG_COLOR)
list_container.pack()


#chicken title
lbl_list_title = Label(list_container, text="Registered chicken", font=("Arial", 24, "bold"), fg=TITLE_COLOR, bg=BG_COLOR)
lbl_list_title.pack(pady=(0,20))


#listbox
list_frame = Frame(list_container, bg=BG_COLOR)
list_frame.pack(fill=BOTH, expand=YES)


#scrollbar
listbox = Listbox(list_frame, bg=ENTRY_BG, font=("Arial", 11), selectmode=SINGLE,selectbackground=BTN_BG, selectforeground=BTN_FG, width=40, height=12)
listbox.pack(pady=10)

#index->chicken id
list_ids = []


#refresh and details buttons
btn_frame = Frame(list_container, bg=BG_COLOR)
btn_frame.pack(pady=20)
btn_refresh = Button(btn_frame, text="Refresh", command=lambda: refresh_list(),bg=BTN_BG, fg=BTN_FG, font=("Arial", 10, "bold"), width=12)
btn_refresh.pack(side=LEFT, padx=10)
btn_details = Button(btn_frame, text="Details", command=lambda: details(),bg=BTN_BG, fg=BTN_FG, font=("Arial", 10, "bold"), width=12)
btn_details.pack(side=LEFT, padx=10)
btn_delete = Button(btn_frame, text="Delete", command=lambda: delete_chicken(),bg=BTN_BG, fg=BTN_FG, font=("Arial", 10, "bold"), width=12)
btn_delete.pack(side=LEFT, padx=10)


#page switcher
def show_page(p):
    page1.pack_forget()
    page2.pack_forget()
    p.pack(fill="both", expand=1)


#save button
def save_data():
    data = get_data()
    if not isinstance(data, dict):
        return
    try:
        # Save using normalized key `system` provided by `get_data()` below.
        c.execute("INSERT INTO chicken (name, age, gender, height, weight, sys) VALUES (%s,%s,%s,%s,%s,%s)", (data["name"], data["age"], data["gender"], data["height"], data["weight"], data["system"]),)
        connection.commit()
        mb.showinfo("Success", "mcdonald registered successfully")
        clear_form()
        refresh_list()
    except Exception as e:
        connection.rollback()
        mb.showerror("Database error", f"Failed to save data: {e}")


#clear button
def clear_form():
    entry_name.delete(0, END)
    entry_age.delete(0, END)
    entry_gender.delete(0, END)
    entry_height.delete(0, END)
    entry_weight.delete(0, END)
    entry_system.delete(0,END)


#refresh button
def refresh_list():
    try:
        listbox.delete(0, END)
        #oldest->newest
        c.execute("SELECT id, name, sys FROM chicken ORDER BY id ASC")
        rows = c.fetchall()
        #rebuilding and reordering
        list_ids.clear()
        for idx, r in enumerate(rows, start=1):
            list_ids.append(r[0])
            listbox.insert(END, f"{idx}. {r[1]} ({r[2]})")
    except Exception as e:
        mb.showerror("Database error", f"Failed to fetch data: {e}")


#details button
def details():
    sel = listbox.curselection()
    if not sel:
        mb.showwarning("Select", "Please select a person from the list")
        return
    person_id = list_ids[sel[0]]
    try:
        c.execute("SELECT name, age, gender, height, weight, sys FROM chicken WHERE id=%s", (person_id,))
        r = c.fetchone()
        if r:
            mb.showinfo("Details", f"Name: {r[0]}\nAge: {r[1]}\nGender: {r[2]}\nHeight: {r[3]} cm\nWeight: {r[4]} kg\nSystem: {r[5]}")
        else:
            mb.showwarning("Not found", "Person not found in database")
    except Exception as e:
        mb.showerror("Database error", f"Failed to fetch details: {e}")


#save and clear buttons
action_frame = Frame(form_container, bg=BG_COLOR)
btn_save = Button(action_frame, text="Save", command=save_data,bg=BTN_BG, fg=BTN_FG, font=("Arial", 10, "bold"), width=12)
btn_clear = Button(action_frame, text="Clear", command=clear_form,bg=BTN_BG, fg=BTN_FG, font=("Arial", 10, "bold"), width=12)
btn_save.pack(side=LEFT, padx=10)
btn_clear.pack(side=LEFT, padx=10)
action_frame.grid(row=7, column=0, columnspan=2, pady=20)


#input
def get_data():
    chicken_name = entry_name.get().upper().strip()
    if not chicken_name:
        mb.showerror("Error", "Name cannot be empty")
        return

    try:
        chicken_age = int(entry_age.get().strip())
        if chicken_age <= 0:
            raise ValueError
    except ValueError:
        mb.showerror("Error", "Age must be a positive integer")
        return
    
    try:
        chicken_gender = entry_gender.get().upper().strip()
        if chicken_gender not in ["MALE", "FEMALE"]:
            raise ValueError
    except ValueError:
        mb.showerror("Error", "Gender must be 'MALE' or 'FEMALE'")
        return
    
    try:
        chicken_height = float(entry_height.get().strip())
        if chicken_height <= 0:
            raise ValueError
    except ValueError:
        mb.showerror("Error", "Height must be a positive number")
        return
    
    try:
        chicken_weight = float(entry_weight.get().strip())
        if chicken_weight <= 0:
            raise ValueError
        elif chicken_weight > 100:
            mb.showwarning("Warning", "Weight seems unusually high")
    except ValueError:
        mb.showerror("Error", "Weight must be a positive number")
        return
    
    # normalize to lowercase so it can be compared to `SYSTEM` reliably
    chicken_system = entry_system.get().strip().lower()
    if chicken_system not in SYSTEM:
        mb.showerror("Error", f"Invalid system. Valid options: {', '.join(SYSTEM)}")
        return
    
    return {
        "name": chicken_name,
        "age": chicken_age,
        "gender": chicken_gender,
        "height": chicken_height,
        "weight": chicken_weight,
        # return normalized key matching save_data() usage
        "system": chicken_system
    }


#delete
def delete_chicken():
    sel = listbox.curselection()
    if not sel:
        mb.showwarning("Select", "Please select a person to delete")
        return
    person_id = list_ids[sel[0]]
    confirm = mb.askyesno("Confirm Delete", "Are you sure you want to delete the selected person?")
    if not confirm:
        return
    try:
        c.execute("DELETE FROM chicken WHERE id=%s", (person_id,))
        connection.commit()
        mb.showinfo("Deleted", "Person deleted successfully")
        refresh_list()
    except Exception as e:
        connection.rollback()
        mb.showerror("Database error", f"Failed to delete person: {e}")


#start up register page 1
show_page(page1)
try:
    refresh_list()
except Exception:
    pass


#run
main.mainloop()

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector

# SETUP
root = Tk()
root.geometry("500x500")
root.title("Watcher's Archive")
Connection = mysql.connector.connect(host="localhost", user="root", password="", port="3306", database="watcherarchive")
c = Connection.cursor()

# Global references
logo_img = None
ArchiveHome = None
ArchivalEntry = None

valid_archivists = {
    "Rowan": "Artwood",
    "Elizabeth": "Bloodflame",
    "Miraen": "Sanna",
    "Gigi": "Murin",
    "Jonathan": "Sims"
}

# --------------------- FUNCTIONS ---------------------

def show_frame(frame):
    # Hide all frames and show the selected one
    for widget in root.winfo_children():
        if isinstance(widget, Frame):
            widget.pack_forget()
    frame.pack()

def EntryGranted():
    global logo_img, ArchiveHome

    LoginFrame.pack_forget()
    top_frame.pack_forget()

    # Create ArchiveHome only once
    if not hasattr(EntryGranted, "created"):
        ArchiveHome = Frame(root)

        # ✅ Reuse the already loaded logo image
        logo_label = Label(ArchiveHome, image=logo_img)
        logo_label.image = logo_img   # Keep a reference
        logo_label.pack()

        Label(ArchiveHome, text="Welcome to the Archive!", font=("Times New Roman", 20)).pack(pady=10)
        Label(ArchiveHome, text="Take a look around our many entries, or add your own", font=("Times New Roman", 15)).pack(pady=10)

        EntryGranted.created = True

    ArchiveHome.pack()

    # Set up the menu bar
    main_bar = Menu(root)
    root.config(menu=main_bar)

    main_bar.add_command(label="Home", command=lambda: show_frame(ArchiveHome))
    main_bar.add_command(label="New Entry", command=NewEntry)
    main_bar.add_command(label="Delete Entry", command=EntryDelete)
    main_bar.add_command(label="Watch Archives", command=ShowArchiveTable)
    main_bar.add_command(label="Logout", command=logout)

def NewEntry():
    global ArchivalEntry

    if ArchivalEntry is None:
        ArchivalEntry = Frame(root)

        # Centered heading label spanning 2 columns
        Label(ArchivalEntry, text="Enter Entry Below", font=("Times New Roman", 20)).grid(row=0, column=0, columnspan=2, pady=15)

        EntryLabel = Label(ArchivalEntry, text="New Archive Entry:", font=("Times New Roman", 10,"bold"))
        DetailLabel = Label(ArchivalEntry, text="Entry Detail:", font=("Times New Roman", 10, "bold"))
        CategoryLabel = Label(ArchivalEntry, text="Entry Category:", font=("Times New Roman", 10, "bold"))
        YearLabel = Label(ArchivalEntry, text="Entry Year:", font=("Times New Roman", 10, "bold"))

        EntryLabel.grid(row=1, column=0, sticky='W', pady=5, padx=10)
        DetailLabel.grid(row=2, column=0, sticky='NW', pady=5, padx=10)
        CategoryLabel.grid(row=3, column=0, sticky='W', pady=5, padx=10)
        YearLabel.grid(row=4, column=0, sticky='W', pady=5, padx=10)

        EntryLabelEntry = Entry(ArchivalEntry)
        DetailEntry = Text(ArchivalEntry, width=40, height=5)

        CategoryEntry = StringVar()
        CategoryEntry.set("Undefined")
        # Category Label
        CategoryLabel.grid(row=3, column=0, sticky='W', pady=5, padx=10)

        # Frame to hold radiobuttons
        category_frame = Frame(ArchivalEntry)
        category_frame.grid(row=3, column=1, columnspan=2, pady=5, padx=10, sticky='w')

        # Now add radiobuttons inside the frame
        CategoryEntry1 = Radiobutton(category_frame, text="Fauna", variable=CategoryEntry, value="Fauna")
        CategoryEntry2 = Radiobutton(category_frame, text="Flora", variable=CategoryEntry, value="Flora")
        CategoryEntry3 = Radiobutton(category_frame, text="Kingdom", variable=CategoryEntry, value="Kingdom")
        CategoryEntry4 = Radiobutton(category_frame, text="Event", variable=CategoryEntry, value="Event")
        CategoryEntry5 = Radiobutton(category_frame, text="People", variable=CategoryEntry, value="People")
        CategoryEntry6 = Radiobutton(category_frame, text="Undefined", variable=CategoryEntry, value="Undefined")

        
        YearEntry = Entry(ArchivalEntry)

        EntryLabelEntry.grid(row=1, column=1, pady=5, padx=10, sticky='ew')
        DetailEntry.grid(row=2, column=1, pady=5, padx=10)

        CategoryEntry1.grid(row=0, column=0, padx=5, pady=2, sticky='w')
        CategoryEntry2.grid(row=0, column=1, padx=5, pady=2, sticky='w')
        CategoryEntry3.grid(row=0, column=2, padx=5, pady=2, sticky='w')

        CategoryEntry4.grid(row=1, column=0, padx=5, pady=2, sticky='w')
        CategoryEntry5.grid(row=1, column=1, padx=5, pady=2, sticky='w')
        CategoryEntry6.grid(row=1, column=2, padx=5, pady=2, sticky='w')
        

        YearEntry.grid(row=4, column=1, pady=5, padx=10, sticky='ew')

        def SubmitEntry():
            EntryName = EntryLabelEntry.get().upper().strip()
            Detail = DetailEntry.get("1.0", END).strip()   # ✅ correct way to get Text content
            Category = CategoryEntry.get()
            Year = YearEntry.get().strip()

            # Basic validation
            if not EntryName or not Detail or not Year:
                messagebox.showwarning("Missing Data", "Please fill all fields before submitting.")
                return

            try:
                insert_query = "INSERT INTO `archive contents` (`Entry Name`, `Archive Detail`, `Category`, `Year`) VALUES (%s, %s, %s, %s)"
                data = (EntryName, Detail, Category, Year)
                c.execute(insert_query, data)
                Connection.commit()

                # ✅ Clear inputs properly
                EntryLabelEntry.delete(0, END)
                DetailEntry.delete("1.0", END)
                YearEntry.delete(0, END)

                # ✅ Show popup confirmation
                messagebox.showinfo("Archive Notice", f"Your entry '{EntryName}' has been saved successfully!")

            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"An error occurred:\n{err}")


        ArchivalEntry.grid_columnconfigure(1, weight=1)
        
        SubmitButton = Button(ArchivalEntry, text="Submit Data", command= SubmitEntry)
        SubmitButton.grid(row=6, column=0, columnspan= 2, pady=10, padx=10, sticky="nsew")

    show_frame(ArchivalEntry)

def EntryDelete():
    global DeleteFrame

    if 'DeleteFrame' not in globals() or DeleteFrame is None:
        DeleteFrame = Frame(root)

        Label(DeleteFrame, text="Remove an Entry", font=("Times New Roman", 20)).grid(row=0, column=0, columnspan=2, pady=15)
        Label(DeleteFrame, text="Warning: among archivists, the removal of an entry is looked down upon, for it goes against everything we stand for. Proceed with caution.", font=("Times New Roman", 12), anchor = "center", wraplength=450, justify="left").grid(row=1, column=0, columnspan=2, pady=10)

        DelEntryLabel = Label(DeleteFrame, text="Delete Archive Entry:", font=("Times New Roman", 10, "bold"))
        DelEntryLabel.grid(row=3, column=0, sticky='W', pady=5, padx=10)

        DelEntryEntry = Entry(DeleteFrame)
        DelEntryEntry.grid(row=3, column=1, pady=5, padx=10, sticky='ew')

        def DeleteEntry():
            DelName = DelEntryEntry.get().upper().strip()
            if not DelName:
                messagebox.showwarning("Missing Name", "Please enter the name of the entry to delete.")
                return

            confirm = messagebox.askyesno(
                "Confirm Deletion",
                f"Are you sure you want to delete '{DelName}'?\nIf deleted inappropriately, you will be held accountable."
            )

            if confirm:
                try:
                    c.execute("DELETE FROM `archive contents` WHERE `Entry Name` = %s", (DelName,))
                    Connection.commit()
                    if c.rowcount > 0:
                        messagebox.showinfo("Entry Removed", f"The entry '{DelName}' has been deleted.\nThe archive mourns its loss.")
                    else:
                        messagebox.showwarning("Not Found", f"No entry found named '{DelName}'.")
                    DelEntryEntry.delete(0, END)
                except mysql.connector.Error as err:
                    messagebox.showerror("Database Error", f"An error occurred:\n{err}")
            else:
                messagebox.showinfo("Cancelled", "No changes have been made. The archive breathes a sigh of relief.")

        DeleteButton = Button(DeleteFrame, text="Delete Entry", command=DeleteEntry)
        DeleteButton.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

    show_frame(DeleteFrame)

def fetch_data(category=None, sort_by=None, descending=False):
    base_query = "SELECT `Entry Name`, `Category`, `Year`, `Archive Detail` FROM `archive contents`"
    params = []

    if category and category != "All":
        base_query += " WHERE `Category` = %s"
        params.append(category)

    if sort_by:
        order = "DESC" if descending else "ASC"
        base_query += f" ORDER BY `{sort_by}` {order}"

    c.execute(base_query, params)
    return c.fetchall()


def ShowArchiveTable():
    ArchiveTable = Frame(root)
    columns = ("Name", "Category", "Year", "Detail")
    tree = ttk.Treeview(ArchiveTable, columns=columns, show="headings", height=15)

    #-----------------------------
    # Search
    #-----------------------------

    ttk.Label(ArchiveTable, text="Search by Name:").pack(pady=5)
    SearchEntry = Entry(ArchiveTable)
    SearchEntry.pack(pady=5)

    
    def OnSearchChange(event):
        UpdateTable(CategoryFilter.get(), sort_column, sort_descending, SearchEntry.get())

    SearchEntry.bind("<KeyRelease>", OnSearchChange)

    # ----------------------------
    # Sorting state
    # ----------------------------
    sort_column = None
    sort_descending = False

    column_map = {
    "Name": "`Entry Name`",
    "Category": "`Category`",
    "Year": "`Year`",
    "Detail": "`Archive Detail`" 
}

    # Search Funct




    # ----------------------------
    # Update table content
    # ----------------------------
    def UpdateTable(category=None, sort_by=None, descending=False, search_text=""):
        query = "SELECT `Entry Name`, `Category`, `Year`, `Archive Detail` FROM `archive contents`"
        params = []

        conditions = []
        if category and category != "All":
            query += " WHERE `Category`=%s"
            params.append(category)

        if search_text:
            conditions.append("`Entry Name` LIKE %s")
            params.append(f"%{search_text}%")

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        if sort_by:
            db_col = column_map.get(sort_by)
            if db_col:
                query += f" ORDER BY {db_col}"
                if descending:
                    query += " DESC"

        c.execute(query, params)
        rows = c.fetchall()
        # populate treeview
        for row in tree.get_children():
            tree.delete(row)
        for row in rows:
            tree.insert("", END, values=row)


    # ----------------------------
    # Filter change
    # ----------------------------
    def OnFilterChange(event):
        selected_category = CategoryFilter.get()
        UpdateTable(selected_category)

    # ----------------------------
    # Column header click -> sort
    # ----------------------------
    def OnHeadingClick(col):
        nonlocal sort_column, sort_descending
        ValidCols = ["Name", "Category", "Year"]
        if col not in ValidCols:
            messagebox.showinfo("Not sortable", f"The '{col}' column cannot be sorted.")
            return
        if sort_column == col:
            sort_descending = not sort_descending
        else:
            sort_column = col
            sort_descending = False
        UpdateTable(CategoryFilter.get(), sort_column, sort_descending)

    # ----------------------------
    # Setup category filter
    # ----------------------------
    ttk.Label(ArchiveTable, text="Filter by category:").pack(pady=5)
    CategoryFilter = ttk.Combobox(
        ArchiveTable, state="readonly",
        values=['All','Fauna','Flora','Kingdom','Event','People','Undefined']
    )
    CategoryFilter.current(0)
    CategoryFilter.bind("<<ComboboxSelected>>", OnFilterChange)
    CategoryFilter.pack(pady=5)

    # ----------------------------
    # Setup Treeview headings
    # ----------------------------
    for col in columns:
        tree.heading(col, text=col, command=lambda _col=col: OnHeadingClick(_col))
        tree.column(col, width=120)
    tree.pack(padx=10, pady=10)

    # ----------------------------
    # Double-click to view full detail
    # ----------------------------
    def on_item_double_click(event):
        if not tree.selection():
            return
        selected_item = tree.selection()[0]
        item_values = tree.item(selected_item, "values")
        full_name = item_values[0]

        c.execute("SELECT `Archive Detail` FROM `archive contents` WHERE `Entry Name`=%s", (full_name,))
        full_detail = c.fetchone()[0]

        detail_window = Toplevel(root)
        detail_window.title(f"Detail: {full_name}")
        detail_window.geometry("400x300")

        text = Text(detail_window, wrap='word')
        text.tag_configure("title", font=("Times New Roman", 16, "bold"))
        text.tag_configure("body", font=("Times New Roman", 12))

        # Insert title (first line) and body (rest)
        full_text = full_name + "\n" + "\n" + full_detail
        text.insert("1.0", full_text)

        # Apply tags
        text.tag_add("title", "1.0", "1.end")         
        text.tag_add("body", "2.0", END)              

        text.config(state=DISABLED)
        text.pack(padx=10, pady=10, fill='both', expand=True)

    tree.bind("<Double-1>", on_item_double_click)

    # ----------------------------
    # Initial population
    # ----------------------------
    UpdateTable()
    show_frame(ArchiveTable)


def logout():
    ArchiverLoginEntry.delete(0, END)
    ArchiverIDCode.delete(0, END)

    # Reset menu bar
    root.config(menu=Menu(root))

    # Show login screen
    show_frame(top_frame)
    LoginFrame.pack(pady=10)

def Login():
    username = ArchiverLoginEntry.get()
    password = ArchiverIDCode.get()

    if username in valid_archivists and valid_archivists[username] == password:
        EntryGranted()
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")

# --------------------- GUI LAYOUT ---------------------

# TOP FRAME (Logo)
top_frame = Frame(root)
top_frame.pack(pady=10)

ori_image = Image.open(r"C:\Users\loren\Desktop\Certificates\Documents\Giovano J Lorence G12 IPA\T2\T2Nav\Fantasy.png")
resized = ori_image.resize((250, 250), Image.LANCZOS)
logo_img = ImageTk.PhotoImage(resized)
logo_label = Label(top_frame, image=logo_img)
logo_label.image = logo_img
logo_label.pack()


# LOGIN FRAME
LoginFrame = Frame(root)
LoginFrame.pack(pady=10)

Label(LoginFrame, text="Archivist's Name", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky='w', pady=2)
Label(LoginFrame, text="Identification Code:", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky='w', pady=2)

ArchiverLoginEntry = Entry(LoginFrame)
ArchiverIDCode = Entry(LoginFrame)
ArchiverLoginEntry.grid(row=0, column=1, pady=2)
ArchiverIDCode.grid(row=1, column=1, pady=2)

ArchiverButton = Button(LoginFrame, text="Confirm Entry", command=Login)
ArchiverButton.grid(row=2, column=0, columnspan=2, pady=10)

# Run
root.mainloop()

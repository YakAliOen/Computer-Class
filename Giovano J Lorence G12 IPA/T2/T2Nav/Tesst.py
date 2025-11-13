import tkinter as tk

root = tk.Tk()
root.title("Tear-off Menu Example")

menubar = tk.Menu(root)
root.config(menu=menubar)

# Menu with tear-off enabled (default)
file_menu_tearoff = tk.Menu(menubar, tearoff=1) 
file_menu_tearoff.add_command(label="New")
file_menu_tearoff.add_command(label="Open")
menubar.add_cascade(label="File (Tear-off)", menu=file_menu_tearoff)

# Menu with tear-off disabled
edit_menu_no_tearoff = tk.Menu(menubar, tearoff=0)
edit_menu_no_tearoff.add_command(label="Cut")
edit_menu_no_tearoff.add_command(label="Copy")
menubar.add_cascade(label="Edit (No Tear-off)", menu=edit_menu_no_tearoff)

root.mainloop()
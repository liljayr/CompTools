import tkinter as tk
from tkinter import ttk
from tkinter import *

# Initializing the root and frame
root = tk.Tk()
frame = Frame(root)
frame.pack()

# Styling and sizing
root.title("02807 Computational Tools for Data Science")
root.geometry("1500x2000")


# Function for searching for recommended books
def searchBooks():
    # Refresh and clear table column
    # Make a check if table is NOT EMPTY, then delete existing table
    #table.delete(0, END)

    # Inserting a row with data
    table.insert(parent='', index='end',
                 values=('Test book title', 'Test book genre', 'Test review score', 'Test '
                                                                                    'summary'))


header = Label(frame, text="Top 5 book recommendations", pady=15, font=('Times', 22, 'bold'))

search = tk.Button(frame, text="Search 🔎", fg="black", bg="#263D42", padx=8, pady=3, borderwidth=4,
                   command=searchBooks, font=('Times', 15,))

entry = tk.Entry(frame, width=100, borderwidth=5)


# Creating the table
table = ttk.Treeview(root, style="style.Treeview", height=30)

table['columns'] = ('book_title', 'author', 'genre', 'review_score', 'summary')
table.column("#0", width=0, stretch=NO)
table.column("book_title", anchor=CENTER, width=400)
table.column("author", anchor=CENTER, width=150)
table.column("genre", anchor=CENTER, width=200)
table.column("review_score", anchor=CENTER, width=200)
table.column("summary", anchor=CENTER, width=400)

table.heading("book_title", text="Book title", anchor=CENTER)
table.heading("author", text="Author", anchor=CENTER)
table.heading("genre", text="Genre", anchor=CENTER)
table.heading("review_score", text="Review/Score", anchor=CENTER)
table.heading("summary", text="Summary", anchor=CENTER)

table.pack(pady=20)

# Styling - table/treeview
style = ttk.Style()
style.configure("style.Treeview", rowheight=35)  # Modify height on the row
style.configure("style.Treeview", highlightthickness=0, bd=0, font=('Times', 17))  # Modify the font of the body
style.configure("style.Treeview.Heading", font=('Times', 22), foreground='black', background='white',
                rowheight=35)  # Modify the font of the headings

# Positions
header.grid(row=0, column=0)
entry.grid(row=1, column=0)
search.grid(row=1, column=1, padx=10, pady=5)
root.mainloop()

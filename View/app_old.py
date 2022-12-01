import tkinter as tk
from tkinter import ttk
from tkinter import *
from SearchBooks import SearchBooks
import pandas as pd

# Initializing the root and frame
root = tk.Tk()
# frame = Frame(root)
# frame.pack()



# Styling and sizing
root.title("02807 Computational Tools for Data Science")
root.geometry("1500x2000")


# Function for searching for recommended books
sb = SearchBooks()
sb.read_books_file()
sb.root = root

# def display_data():
#     sb.title = entry.get()
#     sb.final_five()
#     for book in sb.final_five_df:
#         table.insert('', tk.END, values=book)
#     print("AAAAAAAAAAA")
#     print(sb.title)
#     print(sb.recommendations)
#     print(sb.final_five_df)
#     print("BBBBBBBB")
#     print(sb.books_df.head(5))

header = Label(frame, text="Top 5 book recommendations", pady=15, font=('Times', 22, 'bold'))


# sb.search_books("Functions and Graphs")

data = dict(Title='sd',authors='sd',publishedDate='sd',clean_summary='sd',clean_categories='sd',averageRating='sd')
# sb.final_five_df = pd.DataFrame(columns=['Title','authors','publishedDate','clean_summary','clean_categories','averageRating'])
sb.final_five = pd.DataFrame(data, index=[0])

entry = tk.Entry(frame, width=100, borderwidth=5)


search = tk.Button(frame, text="Search 🔎", fg="black", bg="#263D42", padx=8, pady=3, borderwidth=4,
                   command=sb.show_table, font=('Times', 15,))

# final_rec = sb.final_five()

# print(sb.final_five_df)


# Creating the table
sb.table = ttk.Treeview(root, style="style.Treeview", height=30)

sb.table['columns'] = ('Title', 'Authors', 'Genres', 'Review Score', 'Summary')
sb.table.column("#0", width=0, stretch=NO)
sb.table.column("Title", anchor=CENTER, width=400)
sb.table.column("Authors", anchor=CENTER, width=150)
sb.table.column("Genres", anchor=CENTER, width=200)
sb.table.column("Review Score", anchor=CENTER, width=200)
sb.table.column("Summary", anchor=CENTER, width=400)

sb.table.heading("Title", text="Book title", anchor=CENTER)
sb.table.heading("Authors", text="Author", anchor=CENTER)
sb.table.heading("Genres", text="Genre", anchor=CENTER)
sb.table.heading("Review Score", text="Review/Score", anchor=CENTER)
sb.table.heading("Summary", text="Summary", anchor=CENTER)

# print(sb.final_five)

sb.table.pack(pady=20)

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

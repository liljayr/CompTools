import tkinter as tk
from SearchBooks import SearchBooks

root = tk.Tk()
root.title("02807 Computational Tools for Data Science")
root.geometry("1500x2000")

sb = SearchBooks(root)

root.mainloop()
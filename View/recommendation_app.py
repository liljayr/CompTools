import tkinter as tk
from tkinter import ttk
from tkinter import *
from SearchBooks import SearchBooks
import pandas as pd

root = tk.Tk()
root.title("02807 Computational Tools for Data Science")
root.geometry("1500x2000")

sb = SearchBooks(root)

root.mainloop()
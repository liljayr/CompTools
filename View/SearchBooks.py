import pandas as pd
from functions import *
from gensim.models.doc2vec import Doc2Vec
from nltk.corpus import stopwords
from tkinter import CENTER, NO, Button, Frame, ttk, messagebox, Entry
import webbrowser as wb

class SearchBooks:
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()

        self.entry = Entry(root, width=100, borderwidth=5)
        self.entry.pack(pady=20)

        self.button = Button(root, text="Search 🔎", fg="black", bg="#263D42", padx=8, pady=3, borderwidth=4,
                   command=self.show_table, font=('Times', 15,))
        self.button.pack(pady=20)

        self.table = ttk.Treeview(root, style="style.Treeview", height=30)
        self.initialize_table()

        self.books_df = pd.DataFrame()
        self.read_books_file()
        self.hash = ''
        self.recommendations = pd.DataFrame()
        self.final_five_df = pd.DataFrame()
        self.title = ''
        self.root = ''

        self.table.pack(pady=20)

    def initialize_table(self):
        self.table['columns'] = ('Title','authors','clean_summary','clean_categories','averageRating')
        self.table.column("#0", width=0, stretch=NO)
        self.table.column("Title", anchor=CENTER, width=400)
        self.table.column("authors", anchor=CENTER, width=150)
        self.table.column("clean_categories", anchor=CENTER, width=200)
        self.table.column("averageRating", anchor=CENTER, width=200)
        self.table.column("clean_summary", anchor=CENTER, width=400)

        self.table.heading("Title", text="Book title", anchor=CENTER)
        self.table.heading("authors", text="Author", anchor=CENTER)
        self.table.heading("clean_categories", text="Genre", anchor=CENTER)
        self.table.heading("averageRating", text="Review/Score", anchor=CENTER)
        self.table.heading("clean_summary", text="Summary", anchor=CENTER)
        self.table.bind('<<TreeviewSelect>>', self.open_link) 

    def open_link(self, event):
        # table = event.widget  # get the treeview widget
        item = self.table.item(self.table.focus())  # get the treeview selection
        title = item['values'][0]  # get the link from the selected row
        new_row = self.books_df.loc[self.books_df['Title'] == title]
        link = new_row['previewLink'].values[0]
        wb.open_new_tab(link)  # open the link in a browser tab

    def read_books_file(self, path = 'final.csv'):
        try:
            self.books_df = pd.read_csv(path)
        except Exception as error:
            print('Caught this error: ' + repr(error))

    def get_hash(self):
        refined = self.books_df[[ 'clean_summary' , 'Title']]
        self.hash = tuple(refined['Title'])

    def search_books(self):
        self.get_hash()
        # Load in trained model for searching
        try:
            model= Doc2Vec.load("../Data/d2v.model")
        except Exception as error:
            print('Caught this error: ' + repr(error))

        # Get the index to search by in the model
        try:
            index = self.books_df.index[self.books_df['Title'] == self.title].to_list()[0]
        except Exception as error:
            messagebox.showerror("Invalid input","Book not found, try another title")
            print('Caught this error: ' + repr(error))
            return
        
        # Search for the most similar through the model
        most_similar_docs = []
        for d in model.dv.most_similar([index]):
            most_similar_docs.append(self.hash[d[0]])

        for title in most_similar_docs:
            new_row = self.books_df.loc[self.books_df['Title'] == title]
            self.recommendations = pd.concat([self.recommendations, new_row])

        # Return top 5 of the recommended books
        self.recommendations = self.recommendations.head(5)

    def final_five(self):
        titles = self.recommendations['Title']
        for title in titles:
            curr = self.books_df.loc[self.books_df['Title'] == title]
            self.final_five_df = pd.concat([self.final_five_df, curr])
        self.final_five_df = self.final_five_df[['Title','authors','clean_summary','clean_categories','averageRating', 'previewLink']]

    def show_table(self):
        self.title = self.entry.get()
        self.search_books()
        self.final_five()

        for _ in range(len(self.final_five_df.index.values)):
            self.table.insert('','end',value=tuple(self.final_five_df.iloc[_,[0,1,2,3,4]].values))
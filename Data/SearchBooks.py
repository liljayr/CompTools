import pandas as pd
from functions import *
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.corpus import stopwords
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

class SearchBooks:
    def __init__(self):
        self.books_df = pd.DataFrame()
        self.hash = ''
        self.recommendations = pd.DataFrame()

    def read_books_file(self, path = 'final.csv'):
        self.books_df = pd.read_csv(path)

    def get_hash(self):
        refined = self.books_df[[ 'clean_summary' , 'Title']]
        words = tuple(refined['clean_summary'])
        self.hash = tuple(refined['Title'])

    def search_books(self, title_str):
        self.get_hash()
        # Load in trained model for searching
        model= Doc2Vec.load("d2v.model")

        # Get the index to search by in the model
        index = self.books_df.index[self.books_df['Title'] == title_str].to_list()[0]
        
        # Search for the most similar through the model
        most_similar_docs = []
        for d in model.dv.most_similar([index]):
            most_similar_docs.append(self.hash[d[0]])

        for title in most_similar_docs:
            new_row = self.books_df.loc[self.books_df['Title'] == title]
            self.recommendations = pd.concat([self.recommendations, new_row])

        # Return top 5 of the recommended books
        return self.recommendations.head(5)

    def final_five(self):
        titles = self.recommendations['Title']
        final_five_df = pd.DataFrame()
        for title in titles:
            curr = self.books_df.loc[self.books_df['Title'] == title]
            final_five_df = pd.concat([final_five_df, curr])
        return final_five_df

# if __name__=="__main__":
#     sb = SearchBooks()
#     sb.read_books_file()
#     sb.search_books("Functions and Graphs")
#     # print(final_rec)
#     final_rec = sb.final_five()
#     print(final_rec.columns)
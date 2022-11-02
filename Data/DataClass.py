import pandas as pd
import numpy as np
import json
import nltk
import re
import csv
import matplotlib.pyplot as plt
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import MultiLabelBinarizer

from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

from sklearn.metrics import f1_score, accuracy_score

import pickle


class DataClass:
    def __init__(self) -> None:
        pass

    def read_csv(self, file_name):
        return pd.read_csv(file_name)

    def clean_up_data(self):
        book_data_pd = pd.read_csv('books_data.csv')
        book_data_pd = book_data_pd[book_data_pd['categories'].notna()]
        book_data_pd = book_data_pd[book_data_pd['ratingsCount'].notna()]
        book_data_pd = book_data_pd[book_data_pd['description'].notna()]
        book_data_pd.to_csv('clean_books_data.csv')

    def data_heatmap(self, df):
        print("visualizing data heatmap")
        # make heatmap of dataframe
        fig, ax = plt.subplots()
        ax.pcolor(df)
        plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
        plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
        fig.set_size_inches(10, 10)
        plt.savefig("heatmap.png")

    def genre_count(self):
        book_reviews_pd = pd.read_csv('books_and_ratings.csv')
        genre_pd = pd.DataFrame(columns=['genre', 'count'])

        for index, row in book_reviews_pd.head(15).iterrows():
            print(row['categories'])
            genre_list = [row['categories'].strip("'[]")]
            # genre_list = row['categories'].split(',')
            print(genre_list[0])
            for item in genre_list:
                # print("Item")
                # print(item)
                if (genre_pd['genre'] == item).any():
                    print("adding to existing")
                    # index = genre_pd[genre_pd['genre']==item].index()
                    index = genre_pd.index[genre_pd['genre'] == item].to_list()
                    print(index[0])
                    genre_pd.at[index[0], 'count'] += 1
                    # genre_pd.loc['genre'==item, 'count'] += 1
                else:
                    new_row = pd.DataFrame([[item, 1]], columns=['genre', 'count'])
                    # new_row = {'genre': item, 'count': 1}
                    print("adding new")
                    genre_pd = pd.concat([genre_pd, new_row], ignore_index=True)
                    # genre_pd.concat(new_row)
                    # genre_list['genre'] = item
                    # genre_pd['count'] = 1

        print(genre_pd)


# book_data_pd = pd.read_csv('books_data.csv')
# # rating_data_pd = pd.read_csv('Books_rating.csv')

# # print(book_data_pd['ratingsCount'].mean())
# print(book_data_pd['ratingsCount'][7])

# # print(book_data_pd['ratingsCount', 'description', 'categories'].isnull().sum())
# # print(book_data_pd.isnull().sum())
# # print(type(book_data_pd['categories']))
# print(type(book_data_pd['categories'][0]))
# print('Before')
# print(len(book_data_pd.index))

# test = book_data_pd[book_data_pd['categories'].notna()]
# print('After')
# print(len(test.index))
# print(test.columns)

# test = test[test['ratingsCount'].notna()]
# print('After2')
# print(len(test.index))
# print(test.columns)

# test = test[test['description'].notna()]
# print('After3')
# print(len(test.index))
# print(test.columns)


# rating_data_pd = pd.read_csv('/Users/liljayrgudmundsdottir/Documents/DTU/CompTools4DS/Books_rating.csv')
# book_data_pd = pd.read_csv('clean_books_data.csv')

# print(len(rating_data_pd.index))
# print(rating_data_pd.columns)

# rating_data_pd = rating_data_pd[rating_data_pd['Title'].isin(book_data_pd['Title'])]

# print(len(rating_data_pd.index))
# print(rating_data_pd.columns)

# rating_data_pd.to_csv('clean_book_ratings.csv')

# print(len(book_data_pd.index))
# book_data_pd = book_data_pd[book_data_pd['description'].notna()]
# print(len(book_data_pd.index))

#Combing the two csv files into one where the book.csv contains the average rating
# rate_pd = pd.read_csv('clean_book_ratings.csv')
# print(len(rate_pd.index))
# print(rate_pd.columns)

# dum_pd = rate_pd[rate_pd['Title'] == 'Voices from the Farm: Adventures in Community Living']
# print(dum_pd['review/score'])
# print(sum(dum_pd['review/score'])/len(dum_pd.index))

print("Got the data")
# print(book_data_pd.tail(3))

#writing to clean data with ratings combined
# for index, row in book_data_pd.iterrows():
#     dum_pd = rate_pd[rate_pd['Title'] == row['Title']]
#     aveRating = round(sum(dum_pd['review/score'])/len(dum_pd.index), 2)
#     book_data_pd.at[index, 'averageRating'] = aveRating
#     print(row['Title'])
#     print(aveRating)
#     # 44285
#     print(index/10000)

# print("DONE!!!")
# book_data_pd.to_csv('books_and_ratings.csv')

book_reviews_pd = pd.read_csv('books_and_ratings.csv')
genre_pd = pd.DataFrame(columns=['genre', 'count'])

for index, row in book_reviews_pd.head(15).iterrows():
    print(row['categories'])
    genre_list = [row['categories'].strip("'[]")]
    # genre_list = row['categories'].split(',')
    print(genre_list[0])
    for item in genre_list:
        # print("Item")
        # print(item)
        if (genre_pd['genre'] == item).any():
            print("adding to existing")
            # index = genre_pd[genre_pd['genre']==item].index()
            index = genre_pd.index[genre_pd['genre'] == item].to_list()
            print(index[0])
            genre_pd.at[index[0], 'count'] += 1
            # genre_pd.loc['genre'==item, 'count'] += 1
        else:
            new_row = pd.DataFrame([[item, 1]], columns=['genre', 'count'])
            # new_row = {'genre': item, 'count': 1}
            print("adding new")
            genre_pd = pd.concat([genre_pd, new_row], ignore_index=True)
            # genre_pd.concat(new_row)
            # genre_list['genre'] = item
            # genre_pd['count'] = 1

print(genre_pd)

# dc = DataClass()
# dc.data_heatmap(book_reviews_pd)
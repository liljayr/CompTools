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


rating_data_pd = pd.read_csv('/Users/liljayrgudmundsdottir/Documents/DTU/CompTools4DS/Books_rating.csv')
book_data_pd = pd.read_csv('clean_books_data.csv')

print(len(rating_data_pd.index))
print(rating_data_pd.columns)

rating_data_pd = rating_data_pd[rating_data_pd['Title'].isin(book_data_pd['Title'])]

print(len(rating_data_pd.index))
print(rating_data_pd.columns)

rating_data_pd.to_csv('clean_book_ratings.csv')

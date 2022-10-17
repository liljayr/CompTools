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



def data():
    data = []

    with open("booksummaries.txt", 'r') as f:
        reader = csv.reader(f, dialect='excel-tab')
        for row in tqdm(reader):
            data.append(row)

    book_id = []
    book_name = []
    summary = []
    genre = []

    for i in tqdm(data):
        book_id.append(i[0])
        book_name.append(i[2])
        genre.append(i[5])
        summary.append(i[6])

    books = pd.DataFrame({'book_id': book_id, 'book_name': book_name,
                    'genre': genre, 'summary': summary})
    return books

# final_data = data()
# final_data.to_csv("book_info.csv")
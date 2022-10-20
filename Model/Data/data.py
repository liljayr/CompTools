import pandas as pd
import csv
from tqdm import tqdm
import json










def data():
    data = []

    with open("booksummaries.txt", 'r') as f:
        reader = csv.reader(f, dialect='excel-tab')
        for row in tqdm(reader):
            data.append(row)

    book_id = []
    book_name = []
    book_date = []
    summary = []
    genre = []

    for i in tqdm(data):
        book_id.append(i[0])
        book_name.append(i[2])
        genre.append(i[5])
        summary.append(i[6])
        try:
            year = i[4].split('-')[0]
            print(year)
            book_date.append(int(year))
        except:
            book_date.append(int(i[4]))

    books = pd.DataFrame({'book_id': book_id, 'book_name': book_name,
<<<<<<< Updated upstream
                    'date': book_date,'genre': genre, 'summary': summary})
    return books

# final_data = data()
# final_data.to_csv("book_info3.csv")

pd_data = pd.read_csv("book_info2.csv")
missing = pd_data.isnull().sum()
print(missing)
print(pd_data.dtypes)
# total_cells = np.product(pd_data.shape)
# print(total_cells)

# other_pd = pd_data.dropna()
# other_pd.to_csv("book_wo_missing.csv")

# pd_data['date'].fillna(0)
# pd_data['genre'].fillna('None')
# pd_data.to_csv("books.csv")
=======
                    'genre': genre, 'summary': summary})
    books.drop(books[books['genre']==''].index, inplace=True)
    books[books['genre']=='']
    json.loads(books['genre'][0]).values()
    genres = []
    for i in books['genre']:
     genres.append(list(json.loads(i).values()))
    books['genre_new'] = genres
    return books
>>>>>>> Stashed changes

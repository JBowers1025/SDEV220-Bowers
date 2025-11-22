# books.py
# Jennifer Bowers
# This program calls on a book.csv file

import csv

with open('books.csv', 'rt') as books:
    cin = csv.DictReader(books)
    books = [row for row in cin]
    print(books)
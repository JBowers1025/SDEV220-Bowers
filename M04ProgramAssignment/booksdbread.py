# booksdbread.py
# Jennifer Bowers
# This program reads and writes the data from books2.csv to the books.db

import sqlite3
import csv

with open('books2.csv', 'r') as bookFin:
    dr = csv.DictReader(bookFin)
    bookData = [(i['title'], i['author'], i['year']) for i in dr]
    print(bookData)

sqliteConn = sqlite3.connect('books.db')
cursor = sqliteConn.cursor()

cursor.executemany( "INSERT INTO books (title, author, year) VALUES (?,?,?);", bookData)

cursor.execute('SELECT * FROM books')
show = cursor.fetchall()
print(show)

sqliteConn.commit()
cursor.close()
# 16.5 Read books2.csv and insert its data into the book table.

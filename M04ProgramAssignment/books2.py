# books2.py
# Jennifer Bowers
# This program creates a sql database called books.db

import sqlite3
import csv

conn = sqlite3.connect('books.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS books(
               title VARCHAR(255) PRIMARY KEY, author VARCHAR(255), year INT)''')
conn.commit()
conn.close()

# 16.4 Use the sqlite3 module to create a SQLite database called books.db and a table called books with these fields: title (text), author (text), and year (integer).

# 16.5 Read books2.csv and insert its data into the book table.

# 16.6 Select and print the title column from the book table in alphabetical order.

# 16.7 Select and print all columns from the book table in order of publication.
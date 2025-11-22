# selectYear.py
# Jennifer Bowers
# This program selects all data and lists numerically by year with SQLite3

import sqlite3

DB = 'books.db'
sqliteConn = sqlite3.connect(DB)
cursor = sqliteConn.cursor()


with open(DB):
    cursor.execute('SELECT * FROM books ORDER BY year ASC')
    show = cursor.fetchall()
    print(show)
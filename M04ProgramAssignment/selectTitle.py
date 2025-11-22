# selectTitle.py
# Jennifer Bowers
# This program selects all title and lists alphabetically with SQLite3

import sqlite3

DB = 'books.db'
sqliteConn = sqlite3.connect(DB)
cursor = sqliteConn.cursor()


with open(DB):
    cursor.execute('SELECT title FROM books ORDER BY title ASC')
    show = cursor.fetchall()
    print(show)
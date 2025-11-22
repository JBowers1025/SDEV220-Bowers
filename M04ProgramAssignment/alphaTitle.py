# alphaTitle.py
# Jenn Bowers
# This program uses sqlalchemy to access books.db and sort via title alphabetically

from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///books.db")
conn = engine.connect()

with conn:
    show = conn.execute(text("SELECT title FROM books ORDER BY title ASC"))
    for row in show:
        print(row)
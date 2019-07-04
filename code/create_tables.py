import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"

cursor.execute(create_table)

create_items_table = "CREATE TABLE IF NOT EXISTS items (name text , price real)"

cursor.execute(create_items_table)

items = [
("chair", 100),
("book", 50)
]

put_items_in_db =" INSERT INTO items VALUES (?,?) "

cursor.executemany(put_items_in_db , items)


connection.commit()

connection.close()

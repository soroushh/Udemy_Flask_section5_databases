import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

query = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(query)

inserting_query = "INSERT INTO users VALUES (?,?,?)"

cursor.execute(inserting_query, (1,"soroush", "khosravi"))

connection.commit()

connection.close()

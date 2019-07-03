import sqlite3
connection = sqlite3.connect("data.db")
cursor = connection.cursor()
create_table = "CREATE TABLE people (name text, family text)"
cursor.execute(create_table)

insert_into = "INSERT INTO people VALUES (?, ?)"

name =("soroush", "khosravi")

cursor.execute(insert_into, name)

insert_into_directly = "INSERT INTO people VALUES ('farnaz', 'ostovari')"

cursor.execute(insert_into_directly)

names ={('kati', 'yazdani'),('rostam', 'khosravi')}

cursor.executemany(insert_into, names)

find_query = "SELECT * FROM people WHERE family='khosravi'"

soroush = cursor.execute(find_query)

for name in soroush:
    print(name)

connection.commit()

connection.close()

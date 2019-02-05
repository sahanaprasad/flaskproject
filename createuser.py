import sqlite3
conn=sqlite3.connect('database.db')
print ("opened database successfully")
conn.execute('CREATE TABLE users1(username TEXT NOT NULL,email VARCHAR NOT NULL, firstname TEXT NOT NULL, lastname TEXT NOT NULL, dob DATE NOT NULL, password TEXT NOT NULL, activity BOOLEAN NOT NULL)')
print("table created successfully")
conn.close()

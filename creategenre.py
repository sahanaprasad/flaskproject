import sqlite3
conn=sqlite3.connect('database2.db')
print ("opened database successfully")
conn.execute('CREATE TABLE genrestable4(ID TEXT NOT NULL,genre TEXT NOT NULL )')
print("table created successfully")
conn.close()

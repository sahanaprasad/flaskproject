import sqlite3
conn=sqlite3.connect('database2.db')
print ("opened database successfully")
conn.execute('CREATE TABLE usercomment3(sid TEXT NOT NULL,sname TEXT NOT NULL,uname TEXT NOT NULL,rating TEXT NOT NULL,comments TEXT NOT NULL)')
print("table created successfully")
conn.close()

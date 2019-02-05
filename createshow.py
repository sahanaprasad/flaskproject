import sqlite3
conn=sqlite3.connect('database2.db')
print ("opened database successfully")
conn.execute('CREATE TABLE showlist2(g_id TEXT NOT NULL ,s_id TEXT NOT NULL,sname TEXT NOT NULL,rating TEXT NOT NULL , suggestions TEXT NOT NULL,FOREIGN KEY(g_id) REFERENCES genrestable(ID))')
print("table created successfully")
conn.close()

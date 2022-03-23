import sqlite3
con = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute(""" create table student(id int, name varchar(20), department varchar(30))""")
con.commit()
con.close()
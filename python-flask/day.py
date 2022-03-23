import sqlite3
con = sqlite3.connect('data.db', check_same_thread=False)

def getall():
    cur = con.cursor()
    cur.execute("select * from student")
    data= cur.fetchall()
    con.commit()
    return(data)

def Insert(data):
    cur = con.cursor()
    #cur.execute(f'insert into student values("{data["id"]}","{data["name"]}", "{data["department"]}")')
    if type(data)==list:
        cur.executemany(f'insert into student values(:id,:name,:department)',data)
    else:
        cur.execute(f'insert into student values("{data["id"]}","{data["name"]}", "{data["department"]}")')
    con.commit()

def update(data):
    cur=con.cursor()
    cur.execute(f'update student set name= "{data["name"]}", department = "{data["department"]}" where id = {data["id"]}')
    con.commit()

def delete(id):
    cur=con.cursor()
    cur.execute(f'delete from student where id={id}')
    con.commit()


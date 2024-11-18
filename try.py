import sqlite3
con=sqlite3.connect('new_db')
cur=con.cursor()

cur.execute("select * from booking_history")
res=cur.fetchall()
for i in res:
    print(i)
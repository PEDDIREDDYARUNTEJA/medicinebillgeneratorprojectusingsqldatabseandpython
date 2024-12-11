import os
import sqlite3 as sql
con=sql.connect('amazon')
curs=con.cursor()
q="select * from emp where eid=101"
curs.execute(q)
data=curs.fetchall()
for i in data:
    for j in i:
        print(j,end="\n")
    print()
con.commit()
con.close()        
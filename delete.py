import os
import sqlite3 as sql
con=sql.connect('amazon')
curs=con.cursor()
q="drop table medicines"
curs.execute(q)
con.close()
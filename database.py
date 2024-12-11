import os
import sqlite3 as sql
con=sql.connect('amazon')
curs=con.cursor()
q="create table emp(eid int,ename varchar(20),sal float)"
curs.execute(q)
con.close()

import os
import sqlite3 as sql
con=sql.connect('amazon')
print("database established")
curs=con.cursor()
q="create table medicine(medid int primary key,medname varchar(15),cost float,availaability int,expdate date)"
curs.execute(q)
print("medicine table created")
con.close()
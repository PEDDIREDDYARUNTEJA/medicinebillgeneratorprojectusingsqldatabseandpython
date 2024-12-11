import os
import sqlite3 as sql
con=sql.connect('amazon')
print("database established")
curs=con.cursor()
q="update medicine set availaability=availaability+100"
curs.execute(q)
con.commit()
con.close()

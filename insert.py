import os
import sqlite3 as sql
con=sql.connect('amazon')
curs=con.cursor()
q="insert into medicine values (101,'dolo',20,100,'2025-06-08'),(111,'acetadote',100,105,'2026-07-08'),(131,'michol',35,20,'2024-12-02'),(121,'trianal',65,500,'2028-11-03'),(301,'gantrisin',200,20,'2028-10-10')"
print("data inserted")
curs.execute(q)
con.commit()
con.close()
import os
import sqlite3 as sql
lists=[]
total=0
print("The madicine list :")
print("1.dolo\n2.acetadote\n3.michol\n4.trianal\n5.gantrisin")
con=sql.connect('amazon')
curs=con.cursor()
ch="y"
while ch=="y":
    medname=input("enter medicine name:")
    q="select  medname,cost,availaability from medicine where medname=?"
    data=(medname,)
    curs.execute(q,data)
    j=curs.fetchall()
    if len(j)>0:
        medname=j[0][0]
        cost=j[0][1]
        available=j[0][2]
        #lists.append(medname)
        #lists.append(cost)
        print("medname :",medname)
        print("cost    :",cost)
        quantity=int(input('enter quantity :'))
        if quantity>available:
            print("sorry we have",available ,"qunatity")
            ch=input("if you wnat to add avilable quantity(y/n):") 
        else:
           # lists.append(quantity)
            billamount=quantity*cost
            print("current bill is:",billamount)
            #lists.append(billamount)
            total=total+billamount 
            s="update medicine set availaability=availaability-? where medname=medname"
            t=(quantity,)
            curs.execute(s,t)
            con.commit()
            lists.append([medname,cost,quantity,billamount])
            ch=input("if you wnat to add more(y/n):")   
    else:
        print("medicine not available")
print('name          cost        quantity          amount')
for i in lists:
    for j in i:
        print(j,end='\t\t')
    print()     
print("--------------------------------------")          
print("total amount is:",total)   
print()
print()
print("avilable medicines are ")
r="select *from medicine"
curs.execute(r)
data=curs.fetchall()
for i in data:
    for j in i:
        print(j,end="\t\t")
    print()                 
con.close()
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='password@123',database='buscompany')
cur=mydb.cursor()
up="update bus_company set cname='mno' where cid=4"
s="Select * from passenger"
cur.execute(s)
result=cur.fetchall()
for rec in result:
    print(rec)
#mydb.commit()

#upd="update passenger set p_age=20 where pname='priyanka'"
#cur.execute(upd)
#mydb.commit()

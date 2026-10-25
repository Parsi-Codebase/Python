import mysql.connector
conncetion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='mydb'
)
cursor=conncetion.cursor()
qry="select * from customers order by name"
cursor.execute(qry)
records=cursor.fetchall()
for record in records:
    print(record)
# selecting coluns
qry="select name,address from customers order by address desc"
cursor.execute(qry)
records=cursor.fetchall()
for record in records:
    print(record)
conncetion.close()
cursor.close()
#record=cursor.fetchone() fetch only 1st record/row
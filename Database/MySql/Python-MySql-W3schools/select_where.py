import mysql.connector
conncetion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='mydb'
)
cursor=conncetion.cursor()
qry="select * from customers where address=%s"
data=("Yellow Garden 2",)
cursor.execute(qry,data)
records=cursor.fetchall()
for record in records:
    print(record)
# selecting coluns
qry="select * from customers where name like '%a%'"
cursor.execute(qry)
records=cursor.fetchall()
for record in records:
    print(record)
conncetion.close()
cursor.close()

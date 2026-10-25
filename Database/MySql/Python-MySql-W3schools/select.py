import mysql.connector
conncetion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='mydb'
)
cursor=conncetion.cursor()
qry="select * from customers"
cursor.execute(qry)
records=cursor.fetchall()
for record in records:
    print(record)
# selecting coluns
qry="select name,address from customers"
cursor.execute(qry)
records=cursor.fetchall()
for record in records:
    print(record)
conncetion.close()
cursor.close()
#record=cursor.fetchone() fetch only 1st record/row
#cursor.execute("SELECT * FROM customers LIMIT 5") return only 5 records
#cursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2") return only 5 records starting from 3rd record

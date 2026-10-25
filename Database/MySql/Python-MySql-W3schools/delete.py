import mysql.connector
conncetion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='mydb'
)
cursor=conncetion.cursor()
qry="Delete from customers where id=%s"
data=(2,)
cursor.execute(qry,data)
conncetion.commit()
print('Customer Deleted')
conncetion.close()
cursor.close()
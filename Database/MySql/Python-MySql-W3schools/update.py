import mysql.connector
conncetion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='mydb'
)
cursor=conncetion.cursor()
qry="Update customers set name=%s,address=%s where id=%s"
data=('Akhil','Delhi',3)
cursor.execute(qry,data)
conncetion.commit()
print('Customer Update')
conncetion.close()
cursor.close()
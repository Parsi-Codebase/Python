import mysql.connector
conncetion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='mydb'
)
cursor=conncetion.cursor()
qry="insert into customers(name,address) values(%s,%s)"
data=('Virat','Delhi')
cursor.execute(qry,data)
conncetion.commit()
print('Customer Added')
print("1 record inserted, ID:", cursor.lastrowid) # to get Id
conncetion.close()
cursor.close()
import mysql.connector
# Establish Conncetion
connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='ecommdb'
)
# create a cursor to execute queries
cursor=connection.cursor()
# execute a simple query
cursor.execute("Select Database()")
# fetch result
db_name=cursor.fetchone()
print('you connected to ',db_name)
# close the connection
connection.close()

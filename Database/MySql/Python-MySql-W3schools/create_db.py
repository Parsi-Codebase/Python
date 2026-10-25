import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin"
)
print(connection)
cursor=connection.cursor()
cursor.execute('Create database mydb')
print('mydb created successfully!!')
cursor.close()
connection.close()
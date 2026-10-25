import mysql.connector #import mysql connector
# create to mysql connection
connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='productdb'
)
cursor=connection.cursor(); #create cursor
sql='insert into product(name,price) values(%s,%s)' #sql query
data=('pen',20) #data to be inserted
cursor.execute(sql,data) #execute the sql query
connection.commit() #to save the changes
cursor.close() #close the cursor
connection.close(); #close the connection
import mysql.connector #import mysql connector
# create to mysql connection
connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='productdb'
)
cursor=connection.cursor(); #create cursor
sql="delete from product where id=%s" #sql query
data=(3,) #data to be used in the query
cursor.execute(sql,data) #execute the sql query
connection.commit() #to save the changes
cursor.close() #close the cursor
connection.close(); #close the connection
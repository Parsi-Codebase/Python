import mysql.connector #import mysql connector
# create to mysql connection
connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='productdb'
)
cursor=connection.cursor(); #create cursor
sql="select * from product" #sql query
cursor.execute(sql) #execute the sql query
results=cursor.fetchall() #fetch all the records
for row in results:
    print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}") #print each record
cursor.close() #close the cursor
connection.close(); #close the connection
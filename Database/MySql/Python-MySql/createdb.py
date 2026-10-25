import mysql.connector
# create to mysql
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin'
)
#crate cursor
cur=conn.cursor()
# create a new database
cur.execute('Create database If not exists ProductDB')

#select database
cur.execute('use ProductDB')
#create table
cur.execute("""
            create table if not exists Product(
                id int auto_increment primary key,
                name varchar(50),
                price int
            )
            """)
print('database and table Created Successfully!!')
cur.close()
conn.close()
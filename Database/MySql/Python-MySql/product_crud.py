import mysql.connector #import mysql connector
# create to mysql connection
connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='productdb'
)
cursor=connection.cursor(); #create cursor
def add_product(name, price):
    sql='insert into product(name,price) values(%s,%s)' #sql query
    data=(name, price) #data to be inserted
    cursor.execute(sql,data) #execute the sql query
    connection.commit() #to save the changes        
def update_product(id, name, price):
    sql="update product set name=%s, price=%s where id=%s" #sql query
    data=(name, price, id) #data to be used in the query
    cursor.execute(sql,data) #execute the sql query
    connection.commit() #to save the changes    
def delete_product(id):
    sql="delete from product where id=%s" #sql query
    data=(id,) #data to be used in the query
    cursor.execute(sql,data) #execute the sql query
    connection.commit() #to save the changes    
def select_product_by_id(id):
    sql="select * from product where id=%s" #sql query
    data=(id,) #data to be used in the query
    cursor.execute(sql,data) #execute the sql query
    results=cursor.fetchall() #fetch all the records
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}") #print each record  
def select_all_products():
    sql="select * from product" #sql query
    cursor.execute(sql) #execute the sql query
    results=cursor.fetchall() #fetch all the records
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}") #print each record  
# Close cursor and connection when done
def close_connection():
    cursor.close() #close the cursor
    connection.close(); #close the connection
# Example usage:
# using menu
while True:
    print("\nProduct Management Menu:")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Select Product by ID")
    print("5. Select All Products")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        add_product(name, price)
        print("Product added successfully.")
    elif choice == '2':
        id = int(input("Enter product ID to update: "))
        name = input("Enter new product name: ")
        price = float(input("Enter new product price: "))
        update_product(id, name, price)
        print("Product updated successfully.")
    elif choice == '3':
        id = int(input("Enter product ID to delete: "))
        delete_product(id)
        print("Product deleted successfully.")
    elif choice == '4':
        id = int(input("Enter product ID to select: "))
        select_product_by_id(id)
    elif choice == '5':
        select_all_products()
    elif choice == '6':
        close_connection()
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")


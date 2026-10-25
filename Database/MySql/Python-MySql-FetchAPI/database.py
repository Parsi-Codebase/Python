import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="ecommdb"
        )
        if conn.is_connected():
            return conn
        else:
            raise Exception("MySQL Connection not available.")
    except Error as e:
        print("Error while connecting to MySQL:", e)
        raise Exception("MySQL Connection not available.")


#eventdata.py -- Add code to retrieve all rows of all EVENT table and display  using fetchone() command.. 

import mysql.connector
import getpass

# Read username and password from the user
username = input("Enter MySQL username: ")
password = getpass.getpass("Enter MySQL password: ")

try:
    # Create a connection to the database
    conn = mysql.connector.connect(
        host='localhost',
        user=username,
        password=password,
        database='Olympic_Game_2024_22663281'
    )
    if conn.is_connected():
        db_info = conn.get_server_info()
        print(f"Connected to MySQL Server version {db_info}")
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print(f"You're connected to database: {record[0]}")

        # Add the code to retrieve and display rows from the Emp table
        select_query1 = "SELECT * FROM EVENT"
        cursor.execute(select_query1)
        
        # Get all rows
        rows = cursor.fetchall()
        
        # Print the first four columns of all rows
        for row in rows:
            print(row[0], row[1], ", ", row[2], ", ", row[3])  # Adjusted to match the first four columns of the EVENT table
            
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed.")


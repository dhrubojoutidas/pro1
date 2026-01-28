

# schdeule.py this pyhton file retrive the data of SCEHEDULE table suhc as end_date, start_date, vanue_code  using where conditon status = CANCELLED
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
        record = cursor.fetchall()
        print(f"You're connected to database: {record[0]}")

      
        
        # Retrieve and display the employee's details using the hardcoded employee number
        select_query = """SELECT start_date, end_date, venue_code  
                          FROM SCHEDULE WHERE
                           status = 'CANCELLED' """
        
        
        cursor.execute(select_query )
        
        # Fetch and display the result
        rows = cursor.fetchall()
        if rows:
             for row in rows:
                print(f" start date: {row[0]}, end date: {row[1]}, venue code: {row[2]}")
        else:
            print("No  schedule events with starus found.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed.")
        
        
        


        

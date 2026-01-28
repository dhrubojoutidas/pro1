# insert.py ---- is the file that do insertation in python into the EVENT table.. 
import mysql.connector
import getpass

 #  asking user  for useranme and password to be connected 
username = input("Enter your MySQL username: ")
password = getpass.getpass("Enter MySQL password: ")



# here, trying to connected with MYSQL server
try:
    conn = mysql.connector.connect(
        host='localhost', 
        user=username,
        password=password,
        database='Olympic_Game_2024_22663281' 
    )


    # here, creating a cursor object  suin cursor () method
    cursor = conn.cursor()

    # here, inserting the new data inTO EVENT TABLE OF MYSQL SERVER
    insert_query = """
    INSERT INTO EVENT (event, sport, sport_code)
    VALUES (%s, %s, %s)
    """

    # we can ask user to give event_name, sport_name, sport_code according to their choice
    event_name = input("Hi!!... plz Enter the event name: ")
    sport_name = input("Hi!!!....plz Enter the sport name: ")
    sport_code = input("HI there!! plz...Enter the sport code: ")


    # to store the value from user input
    NewRow = (event_name, sport_name, sport_code)

    # command to exceute SQL 
    cursor.execute(insert_query, NewRow)


    # by typing this commit the changes in the DATABASES
    conn.commit()
    print("WOW!!!!!   Row inserted successfully.")

except mysql.conn.Error as er:
    print(f"Failed to insert record into MySQL table: {er}")
   
    # rollback of any error
    if conn:
        conn.rollback()

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
        
        
        #Weightlifting  WEIGHTLIFTING

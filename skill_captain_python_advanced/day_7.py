import mysql.connector

# Error handling for database connection
try:
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="testdatabase")
    connected = True
except Exception as e:
    print(f"Error: {e}")
    db.rollback()
    connected = False
if connected:
    cursor = db.cursor()
    # Example code for creating table with specified data and adding data into the table
    # cursor.execute("CREATE TABLE students(name VARCHAR(30), program VARCHAR(10), studentID int)")
    # cursor.execute("INSERT INTO students (name, program, studentID) VALUES (%s,%s,%s)", ("Berna", "BSCS", 12341 ))
    #db.commit()

    # Handle error exception for select query
    try:
        cursor.execute("SELECT name FROM students") #Select query to return all values of name
        result = cursor.fetchall() # Print the result from the select query
        for i in result:
            print(i)
    except Exception as e:
        print(f"Error during select query {e}")
    db.close()




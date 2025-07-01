import mysql.connector

def connect_user_db():
    
    mysql_password = "Moon9977" # Change to your mysql server password

    mydb = mysql.connector.connect(
        host="localhost", 
        user="root", 
        passwd=mysql_password
    )
    mycursor = mydb.cursor()

    databases = []
    mycursor.execute("SHOW DATABASES")
    for db in mycursor:
        databases.append(db[0])

    # Check if the database already exist
    if "user_info" not in databases:
        mycursor.execute("CREATE DATABASE user_info")

        # Create table 
        mydb.database = "user_info"

        # User credentials
        mycursor.execute("""
        CREATE TABLE users (
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(100) UNIQUE,
            password_hash VARCHAR(64)
        )
        """)
        
        # Saved tickers
        mycursor.execute("""
        CREATE TABLE saved_ticker (
            id INT PRIMARY KEY AUTO_INCREMENT,
            user_id INT,
            ticker VARCHAR(32),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """)
        mydb.commit()
        
    mydb.close()

    

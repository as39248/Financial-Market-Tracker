import mysql.connector
from utils.hash_password import hash_password
from utils.connect_db import connect_db

def signup():

    userdb = connect_db()
    cursor = userdb.cursor()

    print("\nSign up\n")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    # Hash password
    hashed_pw = hash_password(password)

    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, hashed_pw))
        userdb.commit()
        print("\nUser added successfully!")
    except mysql.connector.IntegrityError:
        print("\nUsername already exists.")
        userdb.close()
        signup()
    
    userdb.close()
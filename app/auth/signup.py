import mysql.connector
import getpass
from utils.hash_password import hash_password
from utils.connect_db import connect_db

def signup():

    userdb = connect_db()
    cursor = userdb.cursor()

    print("\nSign up\n")
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ").strip()
    re_password = getpass.getpass("Re-enter Password: ").strip()
    
    if password != re_password:
        print("\nPasswords do not match.")
        return signup()
        

    # Hash password
    hashed_pw = hash_password(password)

    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, hashed_pw))
        userdb.commit()
        userdb.close()
        print("\nUser added successfully!")
        
    except mysql.connector.IntegrityError:
        print("\nUsername already exists.")
        userdb.close()
        return signup()
       
    
    
    
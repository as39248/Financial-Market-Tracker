import mysql.connector
import getpass
from utils.hash_password import hash_password
from utils.connect_db import connect_db

def signup(username, password, re_password):

    userdb = connect_db()
    cursor = userdb.cursor()

   
    
    if password != re_password:
        return 1
        

    # Hash password
    hashed_pw = hash_password(password)

    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, hashed_pw))
        userdb.commit()
        userdb.close()
        return 0
        
    except mysql.connector.IntegrityError:
        userdb.close()
        return 2
        #return signup()
       
    
    
    
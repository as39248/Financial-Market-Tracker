from utils.connect_db import connect_db
from utils.hash_password import hash_password

def login(username, password):

    userdb = connect_db()
    cursor = userdb.cursor()

    
    hashed_pw = hash_password(password)

    cursor.execute("SELECT * FROM users WHERE username=%s AND password_hash=%s", (username, hashed_pw))
    user = cursor.fetchone()
    if user:
        userdb.close()
        return True
    else:
        
        userdb.close()
        return False


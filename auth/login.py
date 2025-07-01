from utils.connect_db import connect_db
from utils.hash_password import hash_password

def login():

    userdb = connect_db()
    cursor = userdb.cursor()

    print("\nLog in\n")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    hashed_pw = hash_password(password)

    cursor.execute("SELECT * FROM users WHERE username=%s AND password_hash=%s", (username, hashed_pw))
    user = cursor.fetchone()
    if user:
        print("\nLogin successful!")
        userdb.close()
        return user[1]
    else:
        print("\nIncorrect username or password.")
        userdb.close()
        login()


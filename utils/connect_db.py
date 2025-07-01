import mysql.connector

def connect_db():

    mysql_password = "Moon9977" # Change to your mysql server password

    userdb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=mysql_password,
        database="user_info"
    )
    return userdb
from utils.connect_db import connect_db

def save_ticker(current_user):

    userdb = connect_db()
    cursor = userdb.cursor()

    print("\nSave Ticker\n")
    ticker = input("Enter ticker: ").strip().upper()

    cursor.execute("SELECT id FROM users WHERE username=%s", (current_user,))
    user = cursor.fetchone()
    user_id = user[0]
    
    cursor.execute("SELECT user_id, ticker FROM saved_ticker WHERE user_id=%s AND ticker=%s", (user_id, ticker))
    ticker_exist = cursor.fetchone()
    
    if ticker_exist:
        print("\nTicker already saved.")
        userdb.close()
        save_ticker(current_user)
    else:
        cursor.execute("INSERT INTO saved_ticker (user_id, ticker) VALUES (%s, %s)", (user_id, ticker))
        userdb.commit()
        print("\nTicker Saved.")
    userdb.close()


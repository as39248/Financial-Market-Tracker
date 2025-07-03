from utils.connect_db import connect_db
from utils.validate_ticker import check_ticker

def save_ticker(current_user):
    
    print("\nRETURN - Return")
    ticker = input("\nAdd ticker: ").strip().upper()

    if ticker == "RETURN":
        return True

    if not check_ticker(ticker):
        return False

    userdb = connect_db()
    cursor = userdb.cursor()

    cursor.execute("SELECT id FROM users WHERE username=%s", (current_user,))
    user = cursor.fetchone()
    user_id = user[0]
    
    cursor.execute("SELECT user_id, ticker FROM saved_ticker WHERE user_id=%s AND ticker=%s", (user_id, ticker))
    ticker_exist = cursor.fetchone()
    
    if ticker_exist:
        print("\nTicker already saved.")
        userdb.close()
        return save_ticker(current_user)
    else:
        cursor.execute("INSERT INTO saved_ticker (user_id, ticker) VALUES (%s, %s)", (user_id, ticker))
        userdb.commit()
        print("\nTicker Saved.")

    userdb.close()
    return True



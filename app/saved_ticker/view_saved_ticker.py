from utils.connect_db import connect_db

def view_saved_ticker(current_user):

    userdb = connect_db()
    cursor = userdb.cursor()

    # Find the user_id
    cursor.execute("SELECT id FROM users WHERE username=%s", (current_user,))
    user = cursor.fetchone()
    user_id = user[0]

    # Find the saved tickers
    cursor.execute("SELECT ticker FROM saved_ticker WHERE user_id=%s", (user_id,))
    tickers = cursor.fetchall()

    saved_tickers = []
    if tickers:  
        for t in tickers:
            saved_tickers.append(t[0])
    else:
        return None
    return saved_tickers






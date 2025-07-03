from utils.connect_db import connect_db
from utils.display_saved_tickers import display_saved_tickers

def delete_ticker(tickers):

    userdb = connect_db()
    cursor = userdb.cursor()

    index = display_saved_tickers(tickers)
    if index == -2:
        return
    elif index == -1:
        print("\nInvalid Option.")
        return delete_ticker(tickers)
    else:
        target_ticker = tickers[index][0]
        cursor.execute("DELETE FROM saved_ticker WHERE ticker=%s", (target_ticker,))
        userdb.commit()
        userdb.close()
        print("\nTicker Deleted.")

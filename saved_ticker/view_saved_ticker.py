from utils.connect_db import connect_db
from market.time_series import make_time_series
from market.prev_close_price import get_prev_close
from market.search_ticker import get_ticker_info
from utils.display_saved_tickers import display_saved_tickers


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
    if tickers:
        print("\nSaved tickers:\n")
        for t in tickers:
            print(t[0])
    else:
        print("\nNo tickers saved.")

    return tickers


def search_saved_ticker(tickers):
    index = display_saved_tickers(tickers)
    if index == -1:
        print("\nInvalid Option.")
        search_saved_ticker(tickers)

    make_time_series(tickers[index][0])
    get_ticker_info(tickers[index][0])
    get_prev_close(tickers[index][0])
    



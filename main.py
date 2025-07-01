from utils.api import get_polygon_client
from market.time_series import make_time_series
from market.prev_close_price import get_prev_close
from market.search_ticker import get_ticker_info
from init_db.user_db import connect_user_db
from auth.login import login
from auth.signup import signup
from saved_ticker.save_ticker import save_ticker
import sys



def check_ticker(ticker):

    client = get_polygon_client()

    try:
        client.get_ticker_details(ticker)
        return True
    except Exception:
        return False

def ticker_search():
    print(f"""TICKER SEARCH

RETURN - Return to main menu
""")
    ticker = input("Enter ticker: ").strip().upper()
    if ticker == "RETURN":
        return
    elif check_ticker(ticker):
        make_time_series(ticker)
        get_ticker_info(ticker)
        get_prev_close(ticker)
    else:
        print("Invalid Ticker")
        ticker_search()

def handle_command(command, current_user):
    if command == "E":
        return False
    elif command == "T":
        ticker_search()
    elif command == "S":
        save_ticker(current_user)
        pass
    else:
        print("Invalid Command")
    return True

def handle_signin():
    print("""\nWelcome!
1 - Sign up          
2 - Log in          
E - Exit          
          """)
    command = input("Enter command: ").strip().upper()
    if command == "1":
        signup()
        return login()
    elif command == "2":
        return login()
    elif command == "E":
        sys.exit(0)
    else:
        print("\nInvalid Command")
        handle_signin()


def main():
    connect_user_db()
    current_user = handle_signin()

    while True:
        print(f"""
Available Commands:
              
T - Ticker Search
S - Saved Tickers
E - Exit
        """)
        command = input("Enter command: ").strip().upper()
        if not handle_command(command, current_user):
            break


if __name__ == "__main__":
    main()
from utils.api import get_polygon_client
from utils.validate_ticker import check_ticker
from market.time_series import make_time_series
from market.prev_close_price import get_prev_close
from market.search_ticker import get_ticker_info
from init_db.user_db import connect_user_db
from auth.login import login
from auth.signup import signup
from saved_ticker.save_ticker import save_ticker
from saved_ticker.view_saved_ticker import view_saved_ticker, search_saved_ticker
from saved_ticker.delete_ticker import delete_ticker
import sys


def ticker_search():
    print(f"""\nTicker search

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

def saved_ticker_handler(current_user):

    tickers = view_saved_ticker(current_user)
    print("""
A - Add ticker           
V - View ticker details          
D - Delete ticker
R - Return          
          """)
    command = input("Enter command: ").strip().upper()

    if command == "A":
        validate_ticker = save_ticker(current_user)
        if not validate_ticker:
            print("\nInvalid Ticker")
        saved_ticker_handler(current_user)
    elif command == "V":
        print("n\SEARCH TICKER")
        search_saved_ticker(tickers)
        saved_ticker_handler(current_user)
    elif command == "D":
        print("n\DELETE TICKER")
        delete_ticker(tickers)
        saved_ticker_handler(current_user)
    elif command == "R":
        return
    else:
        print("\nInvalid Command")
        saved_ticker_handler(current_user)


def handle_command(command, current_user):
    if command == "E":
        return False
    elif command == "T":
        ticker_search()
    elif command == "S":
        saved_ticker_handler(current_user)
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
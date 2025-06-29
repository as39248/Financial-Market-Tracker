from utils.api import get_polygon_client
from time_series import make_time_series
from prev_close_price import get_prev_close
from search_ticker import get_ticker_info
client = get_polygon_client()

def check_ticker(ticker):
    try:
        client.get_ticker_details(ticker)
        return True
    except Exception:
        return False

def run_ticker_task(title, handler_func):
    print(f"""{title}

RETURN - Return to main menu
""")
    ticker = input("Enter ticker: ").strip().upper()
    if ticker == "RETURN":
        return
    elif check_ticker(ticker):
        handler_func(ticker)
    else:
        print("Invalid Ticker")
        run_ticker_task(title, handler_func)



def run_forecast():
    run_ticker_task("\nHISTORICAL DATA AND FORECAST SEARCH", make_time_series)

def prev_close():
    run_ticker_task("\nPREVIOUS CLOSE PRICE SEARCH", get_prev_close)

def search_ticker_info():
    run_ticker_task("\nTICKER INFO SEARCH", get_ticker_info)


def handle_command(command):
    if command == "E":
        return False
    elif command == "F":
        run_forecast()
    elif command == "P":
        prev_close()
    elif command == "S":
        search_ticker_info()
    else:
        print("Invalid Ticker")
    return True


def main():
    while True:
        print(f"""
Available Commands:
              
S - Search ticker info
P - Show previous close price
F - Show historical data and forecast
E - Exit
        """)
        command = input("Enter command: ").strip().upper()
        if not handle_command(command):
            break


if __name__ == "__main__":
    main()
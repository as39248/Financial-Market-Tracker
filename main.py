from utils.api import get_polygon_client
from time_series import make_time_series
from prev_close_price import get_prev_close

client = get_polygon_client()

def check_ticker(ticker):
    try:
        client.get_ticker_details(ticker)
        return True
    except Exception:
        return False
    
def run_forecast():
    print("""PREVIOUS CLOSE PRICE SEARCH
    
RETURN - Return to main menu
          """)
    ticker = input("Enter ticker: ").strip().upper()
    if check_ticker(ticker):
        make_time_series(ticker)
    elif ticker == "RETURN":
        return
    else:
        print("Invalid Ticker")
        run_forecast()

def prev_close():
    print("""PREVIOUS CLOSE PRICE SEARCH
    
    RETURN - Return to main menu
          """)
    ticker = input("Enter ticker: ").strip().upper()
    if check_ticker(ticker):
        get_prev_close(ticker)
    elif ticker == "RETURN":   
        return
    else:
        print("Invalid Ticker")
        prev_close()

def handle_command(command):
    if command == "E":
        return False
    elif command == "F":
        run_forecast()
    elif command == "P":
        prev_close()
    else:
        print("Invalid Ticker")
    return True


def main():
    while True:
        print(f"""
Available Commands:
              
P - Show previous close price
F - Show historical data and forecast
E - Exit
        """)
        command = input("Enter command: ").strip().upper()
        if not handle_command(command):
            break


if __name__ == "__main__":
    main()
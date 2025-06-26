from time_series import make_time_series
from polygon import RESTClient

client = RESTClient(api_key="lRZg8R5AflQqo34bbvXjjkwpRyu5sI6x")

def check_ticker(ticker):
    try:
        client.get_ticker_details(ticker)
        return True
    except Exception:
        return False

def handle_command(command):
    if command == "HELP":
        print("") #TBA
    elif command == "EXIT":
        return False
    else:
        if check_ticker(command):
            make_time_series(command)
        else:
            print("Invalid Ticker")
    return True


def main():
    while True:
        command = input("Enter command: ").strip().upper()
        
        if not handle_command(command):
            break


if __name__ == "__main__":
    main()
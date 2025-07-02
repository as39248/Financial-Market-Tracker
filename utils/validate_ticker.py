from utils.api import get_polygon_client

def check_ticker(ticker):

    client = get_polygon_client()

    if ticker == '':
        return False

    try:
        client.get_ticker_details(ticker)
        return True
    except Exception:
        return False
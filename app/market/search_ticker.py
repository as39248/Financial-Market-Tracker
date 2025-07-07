from utils.api import get_polygon_client


client = get_polygon_client()

def get_ticker_info(ticker):
    details = client.get_ticker_details(
	ticker,
	)
    return details.name, details.description

   
from utils.api import get_polygon_client
from datetime import datetime

client = get_polygon_client()

def get_prev_close(ticker):
    agg = client.get_previous_close_agg(
        ticker,
        adjusted="true",
    )
    close_date = datetime.fromtimestamp(agg[0].timestamp / 1000).date()
    return f"""Date: {close_date} | ${agg[0].close}"""
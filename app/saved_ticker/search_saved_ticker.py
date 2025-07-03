from market.time_series import make_time_series
from market.prev_close_price import get_prev_close
from market.search_ticker import get_ticker_info
from utils.display_saved_tickers import display_saved_tickers

def search_saved_ticker(tickers):
    index = display_saved_tickers(tickers)
    if index == -2:
        return
    elif index == -1:
        print("\nInvalid Option.")
        return search_saved_ticker(tickers)
    else:
        make_time_series(tickers[index][0])
        get_ticker_info(tickers[index][0])
        get_prev_close(tickers[index][0])
    
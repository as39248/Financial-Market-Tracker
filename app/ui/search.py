import streamlit as st
from utils.validate_ticker import check_ticker
from market.time_series import make_time_series
from market.prev_close_price import get_prev_close
from market.search_ticker import get_ticker_info
from saved_ticker.save_ticker import save_ticker
from utils.search_result import search_result

def search_page():
    st.title("Search Ticker")
    ticker = st.text_input("", placeholder="Search").strip().upper()

    if ticker:
        if check_ticker(ticker):
            
            if st.button("Save"):
                current_user = st.session_state.username
                saved = save_ticker(current_user, ticker)
                if saved:
                    st.success("Ticker Saved")
                else:
                    st.error("Ticker already saved")

            search_result(ticker)
        else:
            st.error("Invalid Ticker")
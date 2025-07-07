import streamlit as st
from market.time_series import make_time_series
from market.prev_close_price import get_prev_close
from market.search_ticker import get_ticker_info

def search_result(ticker):
    ticker_name, ticker_description = get_ticker_info(ticker)
    price_info = get_prev_close(ticker)
    st.header(ticker_name)
    st.write(ticker_description)
    make_time_series(ticker)
    st.subheader("Previous Close Price: ",)
    st.write(price_info)
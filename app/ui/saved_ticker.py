import streamlit as st
from saved_ticker.view_saved_ticker import view_saved_ticker
from utils.search_result import search_result
from saved_ticker.delete_ticker import delete_ticker


def saved_ticker_page():

    st.title("Saved Tickers")

    current_user = st.session_state.username

    saved_tickers = view_saved_ticker(current_user)
    if not saved_ticker_page:
        for i in range(len(saved_tickers)):
            st.subheader(saved_tickers[i])
            if st.button("Search", key=f"search_{i}"):
                search_result(saved_tickers[i])
            if st.button("Delete", key=f"delete_{i}"):
                delete_ticker(saved_tickers[i])
                st.success(f"{saved_tickers[i]} deleted")
                st.rerun() 
    else:
        st.subheader("No Saved Tickers")
        
    
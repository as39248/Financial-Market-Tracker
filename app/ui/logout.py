import streamlit as st
import time 

def logout_page(): 
    st.session_state.logged_in = False
    st.session_state.username = None 
    st.success("You have been logged out.")
    time.sleep(1)
    st.rerun()
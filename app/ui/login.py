import streamlit as st
from auth.login import login


def login_page():
    st.title("Welcome to the Financial Market!")
    st.header("Log in")
    username = st.text_input("Username", placeholder="Username")
    password = st.text_input("Password", type="password", placeholder="Password")

    if st.button("Log in"):
        if login(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Invalid credentials.")

    if st.button("Sign up"):
        st.session_state.go_signup = True  
        st.rerun()
        
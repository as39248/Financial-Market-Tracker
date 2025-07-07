import streamlit as st
import time
from auth.signup import signup

def signup_page():

    st.title("Sign up")
    
    username = st.text_input("Username", placeholder="Username")
    password = st.text_input("Password", type="password", placeholder="Password")
    re_password = st.text_input("Re-enter Password", type="password", placeholder="Re-enter Password")

    if st.button("Sign up"):
        result = signup(username, password, re_password)
        
        # Check username availablilty
        if result == 2:
            st.error("Username already exists.")

        if result == 0:
            st.success("Signup successful.")
            time.sleep(1)
            st.session_state.go_signup = False
            st.rerun()
        elif result == 1:
            st.error("Passwords do not match.")
    
    if st.button("Log in"):
        st.session_state.go_signup = False
        st.rerun()
        

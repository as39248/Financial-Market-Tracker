import streamlit as st
from ui.login import login_page
from ui.logout import logout_page
from ui.signup import signup_page
from ui.search import search_page
from ui.saved_ticker import saved_ticker_page


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "go_signup" not in st.session_state:
    st.session_state.go_signup = False

# Sign up 
if st.session_state.go_signup:
    signup_page()
    st.stop()

# Page display logged in 
if st.session_state.logged_in:

    if st.sidebar.button("Log out", use_container_width=True):
        logout_page()
        
    search = st.Page(search_page, title="Search", icon=":material/search:")
    saved_ticker = st.Page(saved_ticker_page, title="Saved Ticker", icon=":material/bookmark:")

    pg = st.navigation({
        "Search": [search],
        "Saved": [saved_ticker],
        
    })
    pg.run()
    
# Page display not logged in 
else:

    login_page()
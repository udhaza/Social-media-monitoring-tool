import streamlit as st
from streamlit_option_menu import option_menu
from get_tweets import tweets

# 1. Sidebar menu
#with st.sidebar:
    # selected = option_menu(
    #     menu_title="Main Menu",
    #     options=["Home", "Projects", "Contact"],
    #     icons=["house", "book", "envelope"],
    #     menu_icon="cast",
    #     default_index=0,
    # )
# 2.Horizontal Menu
selected = option_menu(
    menu_title="Main Menu",
    options=["Home", "Projects", "Contact"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)
if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")

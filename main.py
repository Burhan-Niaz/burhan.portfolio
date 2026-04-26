import streamlit as st
import streamlit.components.v1 as components

# 1. Hide the standard Streamlit menu and padding for a cleaner look
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {padding-top: 0rem; padding-bottom: 0rem;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 2. Open and read your HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# 3. Render the HTML using Streamlit Components
# Adjust height to fit your specific web page
components.html(html_data, height=1000, scrolling=True)

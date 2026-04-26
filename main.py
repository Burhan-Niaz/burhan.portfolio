import streamlit as st
import streamlit.components.v1 as components

# 1. Page Setup
st.set_page_config(page_title="Burhan Portfolio", layout="wide", initial_sidebar_state="collapsed")

# Hide standard Streamlit UI elements
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 0rem; padding-bottom: 0rem; padding-left: 0rem; padding-right: 0rem;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# 2. Read the static files
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

with open("style.css", "r", encoding="utf-8") as f:
    css_data = f.read()

with open("script.js", "r", encoding="utf-8") as f:
    js_data = f.read()

# 3. Inject CSS and JS directly into the HTML string
# This forces the iframe to load your styles and interactive scripts
full_portfolio_code = f"""
    {html_data}
    <style>{css_data}</style>
    <script>{js_data}</script>
"""

# 4. Render the stitched-together site
components.html(full_portfolio_code, height=1200, scrolling=True)

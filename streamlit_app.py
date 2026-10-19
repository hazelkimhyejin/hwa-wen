from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="小一小二华文测验", page_icon="✏️", layout="centered")

# Hide Streamlit's default menu/footer and trim padding so the test fills the page.
st.markdown(
    """
    <style>
      #MainMenu, footer, header {visibility: hidden;}
      .block-container {padding-top: 0.5rem; padding-bottom: 0; max-width: 820px;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "huawen_test.html").read_text(encoding="utf-8")
components.html(html, height=1500, scrolling=True)

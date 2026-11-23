from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Film Green Book", page_icon="🌿", layout="wide", initial_sidebar_state="collapsed")

# Remove Streamlit's own header, footer and padding so the page fills the screen
st.markdown(
    """<style>
    header[data-testid="stHeader"], footer, #MainMenu {display:none !important}
    .block-container {padding:0 !important; max-width:100% !important}
    </style>""",
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")

# Make the embedded page grow to its own height so there is no inner scrollbar
AUTO_HEIGHT = """<script>(function(){try{var f=window.frameElement;if(!f)return;
var set=function(){f.style.height=Math.ceil(document.documentElement.scrollHeight)+'px'};
new ResizeObserver(set).observe(document.documentElement);window.addEventListener('load',set);set()}catch(e){}})()</script>"""
head, sep, tail = html.rpartition("</body>")
html = head + AUTO_HEIGHT + sep + tail

components.html(html, height=1700, scrolling=True)

from streamlit_option_menu import option_menu
import streamlit as st
import importlib.util
import sys
from pathlib import Path

# ――― page config ―――
st.set_page_config(
    page_title="Chat with Ramin",
    layout="wide",
    initial_sidebar_state="auto",
)

# ――― single menu item ―――
choose = option_menu(
    "Ramin Rahimi Fard",
    ["Lucy"],          # only one visible page
    icons=["robot"],
    menu_icon="chat",  # top icon
    default_index=0,
)

# ――― route to the correct file ―――
pages = {"Lucy": "_pages/home.py"}

# import and run the selected page
page_path = Path(pages[choose])
spec = importlib.util.spec_from_file_location(choose, page_path)
module = importlib.util.module_from_spec(spec)
sys.modules[choose] = module
spec.loader.exec_module(module)

# ――― (optional) LinkedIn icon in sidebar ―――
st.markdown(
    """
    <div style='text-align: center; padding-top: 2rem;'>
        <a href='https://linkedin.com/in/raminrahimifard' target='_blank'>
            <img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg' width='40'>
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

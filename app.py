import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Rishi's Portfolio",
    page_icon="desktop_computer",
    layout="wide",
    initial_sidebar_state="auto",
)
with st.sidebar:
    choose = option_menu(
        "Rishi Raj Sharma",
        [
            "Lucy",
            "About Me",
            "Experience",
            "Technical Skills",
            "Education",
            "Projects",
            "Achivements",
            "Volunteering",
            "Blog",
            "Contact",
        ],
        icons=[
            "robot",
            "person fill",
            "clock history",
            "tools",
            "book half",
            "clipboard",
            "trophy fill",
            "heart",
            "pencil square",
            "envelope",
        ],
        menu_icon="mortarboard",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#0D1117"},
            "icon": {"color": "darkorange", "font-size": "20px"},
            "nav-link": {
                "font-size": "17px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#1F2937",
            },
            "nav-link-selected": {"background-color": "#A41117"},
        },
    )
    st.markdown(
    "<div style='text-align: center;'>"
    "<a href='https://linkedin.com/in/rishirajsharma231'><img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='40'></a>"
    "&nbsp;&nbsp;&nbsp;&nbsp;"
    "<a href='https://github.com/Rishiraj01'><img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'></a>"
    "&nbsp;&nbsp;&nbsp;&nbsp;"
    "<a href='mailto:rishirajsharma231@gmail.com'><img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='40'></a>"
    "</div>",
    unsafe_allow_html=True,
)

pages = {
    "Lucy": "_pages/home.py",
    "About Me": "_pages/About_Me.py",
    "Experience": "_pages/Experience.py",
    "Technical Skills": "_pages/technical_skills.py",
    "Education": "_pages/Education.py",
    "Projects": "_pages/Projects.py",
    "Achivements": "_pages/Achivements.py",
    "Volunteering": "_pages/Volunteering.py",
    "Blog": "_pages/Blog.py",
    "Contact": "_pages/Contact.py",
}

# Dynamically load the selected page
page_file = pages.get(choose)
if page_file:
    with open(page_file, encoding="utf-8") as file:
        exec(file.read())

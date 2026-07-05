from pathlib import Path
import streamlit as st


def load_css():
    css_path = Path("assets/styles.css")
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="FactoryAssist AI",
    page_icon="🏭",
    layout="wide",
)

load_css()

st.title("🏭 FactoryAssist AI")

st.markdown(
    """
    Welcome to FactoryAssist AI!

    Use the navigation menu on the left to explore the application.

    All modules are currently under development.
    """
)

st.success("Project initialized successfully.")
from pathlib import Path
import streamlit as st

from pages.dashboard import render_dashboard


def load_css():
    css_path = Path("assets/styles.css")
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def main():
    st.set_page_config(
        page_title="FactoryAssist AI",
        page_icon="🏭",
        layout="wide",
    )

    load_css()

    render_dashboard()


if __name__ == "__main__":
    main()
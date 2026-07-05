import streamlit as st


def page_header(
    title: str,
    subtitle: str,
    icon: str = "🏭"
) -> None:
    """
    Render a reusable page header.

    Parameters
    ----------
    title : str
        Main page title.

    subtitle : str
        Short description displayed below the title.

    icon : str, optional
        Emoji or icon displayed before the title.
    """

    st.markdown(
        f"""
        <div class="page-header">

            <div class="page-title">
                <span class="page-icon">{icon}</span>
                <span>{title}</span>
            </div>

            <div class="page-subtitle">
                {subtitle}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()
import streamlit as st
import pandas as pd


def table_card(
    title: str,
    dataframe: pd.DataFrame,
    subtitle: str | None = None,
    use_container_width: bool = True,
    hide_index: bool = True
) -> None:
    """
    Render a reusable table inside a styled card.

    Parameters
    ----------
    title : str
        Card title.

    dataframe : pandas.DataFrame
        DataFrame to display.

    subtitle : str | None, optional
        Optional description displayed below the title.

    use_container_width : bool, optional
        Stretch the table to the available width.

    hide_index : bool, optional
        Hide DataFrame index.
    """

    with st.container():

        st.markdown(
            f"""
            <div class="card table-card">

                <div class="table-header">

                    <div class="table-title">
                        {title}
                    </div>

                    {"<div class='table-subtitle'>" + subtitle + "</div>" if subtitle else ""}

                </div>
            """,
            unsafe_allow_html=True,
        )

        st.dataframe(
            dataframe,
            use_container_width=use_container_width,
            hide_index=hide_index,
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
        )
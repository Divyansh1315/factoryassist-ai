import streamlit as st
import plotly.graph_objects as go


def chart_card(
    title: str,
    figure: go.Figure,
    subtitle: str | None = None,
    use_container_width: bool = True
) -> None:
    """
    Render a reusable Plotly chart inside a styled card.

    Parameters
    ----------
    title : str
        Card title.

    figure : plotly.graph_objects.Figure
        Plotly figure to render.

    subtitle : str | None, optional
        Optional description shown below the title.

    use_container_width : bool, optional
        Stretch chart to container width.
    """

    with st.container():

        st.markdown(
            """
            <div class="card chart-card">
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="chart-title">
                {title}
            </div>
            """,
            unsafe_allow_html=True,
        )

        if subtitle:
            st.markdown(
                f"""
                <div class="chart-subtitle">
                    {subtitle}
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.plotly_chart(
            figure,
            use_container_width=use_container_width,
            config={
                "displayModeBar": False
            },
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
        )
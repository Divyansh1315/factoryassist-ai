import streamlit as st
from typing import Union


def metric_card(
    title: str,
    value: Union[int, float, str],
    icon: str = "📊",
    delta: str | None = None,
    color: str = "var(--color-primary)"
) -> None:
    """
    Render a reusable KPI metric card.

    Parameters
    ----------
    title : str
        Title of the metric.

    value : int | float | str
        Value displayed on the card.

    icon : str, optional
        Emoji or icon displayed in the top-right corner.

    delta : str | None, optional
        Optional secondary information displayed below the value.
        Examples:
            "+5% from last month"
            "Updated today"
            "3 machines offline"

    color : str, optional
        Left border accent color.
        Defaults to the application's primary color.
    """

    delta_html = ""

    if delta:
        delta_html = f"""
            <div class="metric-delta">
                {delta}
            </div>
        """

    card_html = f"""
    <div class="card metric-card" style="border-left:6px solid {color};">

        <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
            margin-bottom:10px;
        ">

            <div class="metric-title">
                {title}
            </div>

            <div style="font-size:30px;">
                {icon}
            </div>

        </div>

        <div class="metric-value">
            {value}
        </div>

        {delta_html}

    </div>
    """

    st.markdown(card_html, unsafe_allow_html=True)
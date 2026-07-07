import streamlit as st


_STATUS_MAP = {
    "Running": ("var(--status-success-bg)", "var(--status-success-text)"),
    "Completed": ("var(--status-success-bg)", "var(--status-success-text)"),
    "Normal": ("var(--status-success-bg)", "var(--status-success-text)"),

    "Idle": ("var(--status-warning-bg)", "var(--status-warning-text)"),
    "Scheduled": ("var(--status-warning-bg)", "var(--status-warning-text)"),
    "Warning": ("var(--status-warning-bg)", "var(--status-warning-text)"),

    "Stopped": ("var(--status-danger-bg)", "var(--status-danger-text)"),
    "Critical": ("var(--status-danger-bg)", "var(--status-danger-text)"),
    "Overdue": ("var(--status-danger-bg)", "var(--status-danger-text)"),

    "Maintenance": ("var(--status-info-bg)", "var(--status-info-text)"),
    "In Progress": ("var(--status-info-bg)", "var(--status-info-text)")
}


def status_badge(status: str) -> None:
    """
    Render a reusable status badge.

    Parameters
    ----------
    status : str
        Status text to display.
    """

    background, text = _STATUS_MAP.get(
        status,
        (
            "var(--status-neutral-bg)",
            "var(--status-neutral-text)"
        )
    )

    st.markdown(
        f"""
        <span
            class="status-badge"
            style="
                background:{background};
                color:{text};
            "
        >
            {status}
        </span>
        """,
        unsafe_allow_html=True,
    )
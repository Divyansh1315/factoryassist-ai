from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")

MACHINES_FILE = DATA_DIR / "machines.xlsx"
MAINTENANCE_FILE = DATA_DIR / "maintenance_logs.xlsx"


def _load_machines():
    return pd.read_excel(MACHINES_FILE)

if not MACHINES_FILE.exists():
    raise FileNotFoundError(
        f"Missing data file: {MACHINES_FILE}"
    )


def _load_maintenance_logs():
    return pd.read_excel(MAINTENANCE_FILE)

if not MAINTENANCE_FILE.exists():
    raise FileNotFoundError(
        f"Missing data file: {MAINTENANCE_FILE}"
    )


def get_dashboard_data():
    machines_df = _load_machines()
    maintenance_df = _load_maintenance_logs()

    total_machines = len(machines_df)

    running_machines = (
        machines_df["Status"]
        .eq("Running")
        .sum()
    )

    total_downtime = (
        maintenance_df["Downtime_Hours"]
        .sum()
    )

    resolved = (
        maintenance_df["Resolved"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    open_issues = (
        ~resolved.isin(["true", "yes", "y", "1"])
    ).sum()

    kpis = [
        {
            "title": "Machines",
            "value": total_machines,
            "delta": "",
            "delta_type": "neutral",
        },
        {
            "title": "Running",
            "value": running_machines,
            "delta": "",
            "delta_type": "positive",
        },
        {
            "title": "Downtime",
            "value": f"{total_downtime:.1f} hrs",
            "delta": "",
            "delta_type": "negative",
        },
        {
            "title": "Open Issues",
            "value": open_issues,
            "delta": "",
            "delta_type": "neutral",
        },
    ]

    return {
        "kpis": kpis,
    }
import pandas as pd

machine_status = pd.DataFrame(
    {
        "Machine": [
            "CNC-01",
            "Press-02",
            "Lathe-04",
            "Robot-01",
        ],
        "Status": [
            "Running",
            "Stopped",
            "Running",
            "Maintenance",
        ],
    }
)
import json
from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

for name in ["base_cafe_spiral_mean_both", "base_cafe_spiral_mean_both_small"]:
    path = rf"simulation\{name}\personas\Bernard Lowe\bootstrap_memory\associative_memory\nodes.json"

    with open(path, "r", encoding="utf-8") as f:
        nodes = json.load(f)

    data = []

    for node in nodes.values():
        if node.get("created") is not None and node.get("valence") is not None:
            data.append(
                (
                    datetime.strptime(node["created"], "%Y-%m-%d %H:%M:%S"),
                    node["valence"],
                )
            )

    data.sort(key=lambda x: x[0])

    datetimes = [item[0] for item in data]
    valences = [item[1] for item in data]

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(datetimes, valences, marker=".", linewidth=1.2)

    ax.set_xlabel("Node count")
    ax.set_ylabel("Valence")
    ax.set_title("Valence by Node Count")
    ax.grid(True, alpha=0.25)

    # format datetime
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    fig.autofmt_xdate()

    fig.tight_layout()
    fig.savefig(f"{name}_valence.png", dpi=180)
    plt.close(fig)

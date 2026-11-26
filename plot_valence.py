import json
from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt


def add_plot(ax: plt.Axes, name: str, label: str):
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

    ax.plot(datetimes, valences, marker=".", linewidth=1.2, label=label)
    return


# what to plot
plot_attrs = [
    {"name": "base_cafe_spiral_mean_both", "label": "Qwen3.8-27B-FP8"},
    {"name": "base_cafe_spiral_mean_both_small", "label": "Qwen3.5-9B"},
]
# set color palette
colors = plt.cm.Set1(range(len(plot_attrs)))
plt.rcParams["axes.prop_cycle"] = plt.cycler(color=colors)

# plot
fig, ax = plt.subplots(figsize=(12, 5))
for attr in plot_attrs:
    add_plot(ax, **attr)

ax.set_xlabel("Time (H:M)")
ax.set_ylabel("Valence")
ax.set_title("Valence over Time")
ax.grid(True, alpha=0.25)
ax.legend()

# format datetime
ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
fig.autofmt_xdate()

fig.tight_layout()
fig.savefig("valence_plot.png")
plt.close(fig)

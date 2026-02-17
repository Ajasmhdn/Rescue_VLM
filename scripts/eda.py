import json
from collections import Counter
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Paths
# -----------------------------
PROJECT_ROOT = Path("/home/cai_tkmce/Desktop/DisasterVLM")
JSON_PATH = PROJECT_ROOT / "raw_data/DisasterM3_Instruct/train_release.json"

# ✅ Save figures here
FIG_DIR = PROJECT_ROOT / "figures" / "eda_graphs_highlight"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Highlight tasks (your chosen tasks)
# -----------------------------
HIGHLIGHT_TASKS = {"disaster caption", "disaster restoration advice"}

# -----------------------------
# Load JSON
# -----------------------------
with open(JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

print("✅ Loaded total samples:", len(data))

# -----------------------------
# Task counts
# -----------------------------
task_counts = Counter([x["task"] for x in data])

df = pd.DataFrame(task_counts.items(), columns=["Task", "Count"])
df = df.sort_values(by="Count", ascending=False).reset_index(drop=True)
df["Percent"] = (df["Count"] / df["Count"].sum()) * 100

# -----------------------------
# Color mapping
# -----------------------------
colors = ["orange" if t in HIGHLIGHT_TASKS else "gray" for t in df["Task"]]

# -----------------------------
# 1) Highlighted Bar Chart
# -----------------------------
plt.figure(figsize=(14, 6))
plt.bar(df["Task"], df["Count"], color=colors)

plt.xticks(rotation=45, ha="right")
plt.ylabel("Count")
plt.title("Task Counts Distribution in DisasterM3 (Highlighted Tasks)")

# ✅ Correct annotation placement
for idx, row in enumerate(df.itertuples(index=False)):
    if row.Task in HIGHLIGHT_TASKS:
        plt.text(
            idx,
            row.Count + 500,
            str(row.Count),
            ha="center",
            fontsize=10,
            fontweight="bold"
        )

# legend
plt.bar([], [], color="orange", label="Selected tasks")
plt.bar([], [], color="gray", label="Other tasks")
plt.legend()

plt.tight_layout()
plt.savefig(FIG_DIR / "task_counts_highlighted.png", dpi=300)
plt.show()
print("✅ Saved:", FIG_DIR / "task_counts_highlighted.png")

# -----------------------------
# 2) Highlighted Pie Chart
# -----------------------------
plt.figure(figsize=(10, 10))
plt.pie(
    df["Count"],
    labels=df["Task"],
    autopct="%1.1f%%",
    startangle=140,
    colors=colors
)
plt.title("Task Percentage Distribution (Highlighted Tasks)")

plt.tight_layout()
plt.savefig(FIG_DIR / "task_percentage_highlighted.png", dpi=300)
plt.show()
print("✅ Saved:", FIG_DIR / "task_percentage_highlighted.png")

print("\n✅ All figures saved successfully in:", FIG_DIR)

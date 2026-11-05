import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("breast_cancer_clean.csv")
colors = {"benign": "#2a9d8f", "malignant": "#e63946"}

# Chart 1: number of tumours by diagnosis
counts = df["diagnosis"].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(counts.index, counts.values, color=[colors[d] for d in counts.index])
plt.title("Number of tumours by diagnosis")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("chart1_counts.png", dpi=150)
plt.close()

# Chart 2: tumour radius by diagnosis
plt.figure(figsize=(6, 4))
data = [df[df["diagnosis"] == d]["mean_radius"] for d in ["benign", "malignant"]]
plt.boxplot(data)
plt.xticks([1, 2], ["benign", "malignant"])
plt.title("Mean radius by diagnosis")
plt.ylabel("Mean radius")
plt.tight_layout()
plt.savefig("chart2_radius.png", dpi=150)
plt.close()

# Chart 3: radius vs area
plt.figure(figsize=(6, 4))
for d, c in colors.items():
    sub = df[df["diagnosis"] == d]
    plt.scatter(sub["mean_radius"], sub["mean_area"], s=12, alpha=0.6, color=c, label=d)
plt.title("Mean radius vs mean area")
plt.xlabel("Mean radius")
plt.ylabel("Mean area")
plt.legend()
plt.tight_layout()
plt.savefig("chart3_radius_vs_area.png", dpi=150)
plt.close()

print("Saved chart1_counts.png, chart2_radius.png, chart3_radius_vs_area.png")

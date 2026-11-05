import pandas as pd

df = pd.read_csv("breast_cancer.csv")

print("Shape:", df.shape)
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())
print(df["diagnosis"].value_counts())

# clean column names: spaces -> underscores (needed later for SQL)
df.columns = [c.replace(" ", "_") for c in df.columns]

summary = df.groupby("diagnosis")[["mean_radius", "mean_area", "mean_texture"]].mean().round(2)
print(summary)

df.to_csv("breast_cancer_clean.csv", index=False)
summary.to_csv("summary_by_diagnosis.csv")
print("Saved breast_cancer_clean.csv and summary_by_diagnosis.csv")

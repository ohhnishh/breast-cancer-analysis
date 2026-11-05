from sklearn.datasets import load_breast_cancer

data = load_breast_cancer(as_frame=True)
df = data.frame.copy()
df["diagnosis"] = df["target"].map({0: "malignant", 1: "benign"})
df = df.drop(columns="target")
df.to_csv("breast_cancer.csv", index=False)
print(df.shape)
print(df["diagnosis"].value_counts())

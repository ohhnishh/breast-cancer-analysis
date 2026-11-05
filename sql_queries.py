import sqlite3
import pandas as pd

# Load the cleaned CSV into a SQLite database (built into Python, no install needed)
df = pd.read_csv("breast_cancer_clean.csv")
conn = sqlite3.connect("cancer.db")
df.to_sql("tumours", conn, if_exists="replace", index=False)

queries = {
    "1. Number of tumours by diagnosis":
        "SELECT diagnosis, COUNT(*) AS total FROM tumours GROUP BY diagnosis;",
    "2. Average radius and area by diagnosis":
        "SELECT diagnosis, ROUND(AVG(mean_radius), 2) AS avg_radius, "
        "ROUND(AVG(mean_area), 2) AS avg_area FROM tumours GROUP BY diagnosis;",
    "3. Five largest tumours by area":
        "SELECT diagnosis, mean_radius, mean_area FROM tumours "
        "ORDER BY mean_area DESC LIMIT 5;",
    "4. Percentage of malignant tumours":
        "SELECT ROUND(100.0 * SUM(diagnosis = 'malignant') / COUNT(*), 1) "
        "AS percent_malignant FROM tumours;",
    "5. Tumours with area above 1000, by diagnosis":
        "SELECT diagnosis, COUNT(*) AS total FROM tumours "
        "WHERE mean_area > 1000 GROUP BY diagnosis;",
    "6. Average concave points by diagnosis":
        "SELECT diagnosis, ROUND(AVG(mean_concave_points), 3) AS avg_concave_points "
        "FROM tumours GROUP BY diagnosis;",
}

for title, sql in queries.items():
    print(title)
    print(pd.read_sql_query(sql, conn).to_string(index=False))
    print()

conn.close()

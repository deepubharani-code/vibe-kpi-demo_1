import sqlite3
import pandas as pd
import os

# Paths
CSV_PATH = "data/raw/customers_raw.csv"
DB_PATH = "data/db/analytics.db"

# Ensure db directory exists
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Load CSV
df = pd.read_csv(CSV_PATH)

# Create SQLite connection and load data
conn = sqlite3.connect(DB_PATH)
df.to_sql("customers_raw", conn, if_exists="replace", index=False)
conn.close()

print(f"ETL complete: Loaded {len(df)} rows into {DB_PATH}")

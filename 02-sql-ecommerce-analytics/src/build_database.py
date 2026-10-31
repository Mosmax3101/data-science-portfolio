import sqlite3
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
DB = ROOT / "data" / "ecommerce.db"

FILES = {
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "customers": "olist_customers_dataset.csv",
    "products": "olist_products_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
}

DB.parent.mkdir(parents=True, exist_ok=True)
conn = sqlite3.connect(DB)

for table, filename in FILES.items():
    df = pd.read_csv(RAW / filename)
    df.to_sql(table, conn, if_exists="replace", index=False)
    print(f"Loaded {table}: {len(df):,} rows")

conn.close()
print(f"Database saved to {DB}")
import sqlite3
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "ecommerce.db"
SQL_DIR = ROOT / "sql"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

conn = sqlite3.connect(DB)

for sql_file in sorted(SQL_DIR.glob("*.sql")):
    result = pd.read_sql_query(sql_file.read_text(), conn)
    result.to_csv(OUT / f"{sql_file.stem}.csv", index=False)
    print(f"\n=== {sql_file.stem} ===")
    print(result.head(10).to_string(index=False))

conn.close()
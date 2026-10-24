import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "naira_usd.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

# 1. Load and clean
df = pd.read_csv(RAW)
df = df.rename(columns={"ratedate": "date", "closingrate": "rate"})
df["date"] = pd.to_datetime(df["date"], format="%B-%d-%Y", errors="coerce")
df["rate"] = pd.to_numeric(df["rate"], errors="coerce")
df = df.dropna(subset=["date", "rate"]).sort_values("date")

# 2. Monthly averages, month-on-month change, and 3-month volatility
monthly = df.set_index("date")["rate"].resample("MS").mean().to_frame("avg_rate")
monthly["mom_change_pct"] = monthly["avg_rate"].pct_change() * 100
monthly["volatility_3m"] = monthly["mom_change_pct"].rolling(3).std()

# 3. Flag unusually large monthly moves (more than 2 standard deviations)
threshold = 2 * monthly["mom_change_pct"].std()
monthly["unusual_move"] = monthly["mom_change_pct"].abs() > threshold

# 4. Save results
monthly.to_csv(OUT / "monthly_fx_summary.csv")
print(monthly.tail(12).round(2))
print(f"\nUnusual months flagged: {monthly['unusual_move'].sum()}")

# 5. Chart the trend and highlight unusual months
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(monthly.index, monthly["avg_rate"], label="Monthly average rate", color="#1f4e79")
flagged = monthly[monthly["unusual_move"]]
ax.scatter(flagged.index, flagged["avg_rate"], color="red", label="Unusual move", zorder=5)
ax.set_title("NGN/USD monthly average exchange rate")
ax.set_ylabel("Naira per US dollar")
ax.legend()
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(OUT / "fx_trend.png", dpi=150)
print("Chart saved to outputs/fx_trend.png")
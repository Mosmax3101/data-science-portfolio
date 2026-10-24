# Naira FX Analysis

## Problem
Import-dependent businesses need to understand how volatile the naira is and when rate moves are unusual.

## Data
NGN/USD historical exchange rates (source: Central Bank of Nigeria). Stored in data/raw.

## Method
- Cleaned and aggregated daily rates to monthly averages
- Calculated month-on-month change and 3-month rolling volatility
- Flagged months where the move exceeded 2 standard deviations

## Key findings and Limitations

## Findings

- April 2025 was the weakest point for the naira in the period, at 1,602.79 per USD. The month-on-month move was +4.55%, and the script flagged it as unusual.
- February 2026 was the largest monthly move, at -4.25%. The average fell from 1,416.53 in January to 1,356.30. It is the second flagged month, and the only other one.
- The naira strengthened by about 16% over the period. The average rate fell from 1,553.73 per USD in December 2024 to 1,337.76 in October 2026. That is a 13.9% drop in the rate, which equals about a 16% gain for the naira against the dollar.
- The decline accelerated from August 2025 to January 2026. The rate fell from 1,535.18 to 1,416.53, a drop of 7.7% over five months, with the largest step-downs in September and October 2025.
- Volatility fell sharply by late 2026. The 3-month rolling volatility peaked at 3.35 in April 2025 and was 3.13 in March 2026. It fell to 1.38 in October 2026, though that month is partial.

## Limitations

- The first month (December 2024) and the last month (October 2026) may be partial. Check the first and last dates in your raw CBN file. The October 2026 average covers only part of the month and may change once the full month is included.
- Monthly averages are based on the daily closing rate. The CBN file also includes weighted and simple average rates, which could give slightly different results.
- The unusual-move flag uses a threshold of two standard deviations across the whole period. This includes the flagged months themselves in the calculation, and it doesn’t account for changes in volatility over time. With only 23 monthly observations, two flagged months is a small sample.
- Monthly averages smooth out movements within each month, so short-term spikes may not appear.

## How to run
pip install -r requirements.txt
python src/analysis.py

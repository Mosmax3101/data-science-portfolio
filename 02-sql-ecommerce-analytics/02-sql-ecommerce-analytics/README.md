# E-Commerce Sales Analytics with SQL

## Problem
Management needs to know which product categories drive revenue, how revenue changes over time, and how many customers come back to buy again.

## Data
Brazilian E-Commerce Public Dataset by Olist (Kaggle). Five CSV files loaded into a SQLite database. Raw files are not included in this repository. Download them from Kaggle and place them in data/raw/.

## Method
- Loaded CSVs into SQLite with pandas
- Monthly revenue and order counts using joins and aggregation
- Top product categories by revenue
- Repeat vs one-time customer split using a CTE and window function

## Key findings

# Findings

- Orders grew about ninefold in one year. Delivered orders rose from 750 in January 2017 to 7,069 in January 2018, and monthly revenue rose from 127,482 to 1,077,887.

- November 2017 was the peak month, most likely driven by Black Friday. Orders jumped 63% from 4,478 in October to 7,289, the highest monthly total in the data. Revenue rose 54% to 1,153,364, also the highest in the data.

- Revenue plateaued in 2018. Monthly revenue stayed between about 0.97M and 1.13M from January to May 2018, then dropped 10% in June to 1,011,978. It has stayed near 1.0M since, so growth slowed after early 2018.

- Health & beauty generated the most revenue, but bed/bath/table sold the most units. Health & beauty brought in 1,233,132 from 9,465 items, while bed/bath/table sold 10,953 items for 1,023,435. Watches & gifts had the highest revenue per item, at about 199, compared with about 130 for health & beauty and 93 for bed/bath/table.

- Repeat customers are rare. Of 93,358 customers, 2,801 (3.0%) ordered more than once, and 97.0% bought only once. Improving retention is likely a bigger opportunity than acquiring new customers.

# Limitations

- Only delivered orders are counted. Cancelled, unavailable, or in-transit orders are excluded, so totals reflect completed sales only.

- Revenue is defined differently in the two queries. Monthly revenue includes freight (price + freight value), while category revenue uses only the product price. Compare the two with this in mind.

- Early months are not representative. The 2016 rows contain only a few orders, reflecting the platform’s launch period. The trend analysis is more meaningful from January 2017.

- The data stops at August 2018 in this output. Check whether the source data contains later delivered orders. If it does, extend the analysis or note the cutoff.

- Category names are in Portuguese. In the README, translate them (for example, beleza_saude to health & beauty) and state that the translations are approximate.

- No cost or margin data. The analysis measures revenue, not profit, so the category rankings do not show which categories are most profitable.

- The repeat-customer rate is affected by timing. Customers who bought recently have had less time to reorder, so the 3% figure likely understates repeat behaviour for the full period.


## How to run
pip install pandas
python src/build_database.py
python src/run_queries.py
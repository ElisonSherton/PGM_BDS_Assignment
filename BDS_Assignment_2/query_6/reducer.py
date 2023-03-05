#!/home/vinayak/anaconda3/bin/python
"""/home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_6/reducer.py"""

import sys
from collections import defaultdict
stock_revenue_map = defaultdict(lambda: 0)

# Read the input from standard input
for line in sys.stdin:
    # Remove the leading and trailing whitespaces
    line = line.strip()

    # Parse the mapper input
    stock_code, revenue = line.split(',')
    
    # Sum the revenue into the respective country's account
    stock_revenue_map[stock_code] += float(revenue)

# Figure out the country with highest quantity of items sold
highest_revenue_item = sorted(stock_revenue_map, key = lambda x: stock_revenue_map[x], reverse = True)[0]

print(f"For 12/2010; Stock Code giving highest revenue: {highest_revenue_item} | Revenue Accrued: {stock_revenue_map[highest_revenue_item]:.2f}")
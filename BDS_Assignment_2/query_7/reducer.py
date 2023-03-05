#!/home/vinayak/anaconda3/bin/python
"""/home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_7/reducer.py"""

import sys
from collections import defaultdict
country_sales_map = defaultdict(lambda: 0)

# Read the input from standard input
for line in sys.stdin:
    # Remove the leading and trailing whitespaces
    line = line.strip()

    # Parse the mapper input
    country, quantity = line.split(',')
    
    # Sum the revenue into the respective country's account
    country_sales_map[country] += int(quantity)

# Figure out the country with highest quantity of items sold
lowest_sales_item = sorted(country_sales_map, key = lambda x: country_sales_map[x], reverse = False)[0]

print(f"For the year 2010; Country with lowest quantity of sales: {lowest_sales_item} | Total items sold: {country_sales_map[lowest_sales_item]:.2f}")
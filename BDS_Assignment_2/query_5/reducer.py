#!/home/vinayak/anaconda3/bin/python
"""/home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_5/reducer.py"""

import sys
from collections import defaultdict
stock_code_sales = defaultdict(lambda: 0)

# Read the input from standard input
for line in sys.stdin:
    # Remove the leading and trailing whitespaces
    line = line.strip()

    # Parse the mapper input
    stock_code, quantity = line.split(',')
    
    # Sum the revenue into the respective country's account
    stock_code_sales[stock_code] += int(quantity)

# Figure out the country with highest quantity of items sold
highest_sale_item = sorted(stock_code_sales, key = lambda x: stock_code_sales[x], reverse = True)[0]

print(f"For Germany; Stock Code giving highest sale: {highest_sale_item} | Volume Sold: {stock_code_sales[highest_sale_item]:.2f}")
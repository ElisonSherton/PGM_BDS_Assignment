#!/home/vinayak/anaconda3/bin/python
"""/home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_3/reducer.py"""

import sys
from collections import defaultdict
month_quantity_map = defaultdict(lambda: 0)

# Read the input from standard input
for line in sys.stdin:
    # Remove the leading and trailing whitespaces
    line = line.strip()

    # Parse the mapper input
    month, quantity = line.split(',')
    
    # Sum the quantity into the respective month's account
    month_quantity_map[month] += int(quantity)

# Figure out the month with highest items sold
highest_selling_month = sorted(month_quantity_map, key = lambda x: month_quantity_map[x], reverse = True)[0]

# Print the highest revenue country and the highest revenue to console
print(f"For 2010; Highest Selling Month: {highest_selling_month:0<2} | Items Sold: {month_quantity_map[highest_selling_month]}")
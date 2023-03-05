#!/home/vinayak/anaconda3/bin/python
"""/home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_4/reducer.py"""

import sys
from collections import defaultdict
country_quantity_map = defaultdict(lambda: 0)

# Read the input from standard input
for line in sys.stdin:
    # Remove the leading and trailing whitespaces
    line = line.strip()

    # Parse the mapper input
    country, quantity = line.split(',')
    
    # Sum the revenue into the respective country's account
    country_quantity_map[country] += int(quantity)

# Figure out the country with highest quantity of items sold
highest_selling_country = sorted(country_quantity_map, key = lambda x: country_quantity_map[x], reverse = True)[0]

print(f"For 01/2010; Country selling max items: {highest_selling_country} | Volume Sold: {country_quantity_map[highest_selling_country]}")
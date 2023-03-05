#!/home/vinayak/anaconda3/bin/python
"""/home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_2/reducer.py"""

import sys
from collections import defaultdict
country_revenue_map = defaultdict(lambda: 0)

# Read the input from standard input
for line in sys.stdin:
    # Remove the leading and trailing whitespaces
    line = line.strip()

    # Parse the mapper input
    country, revenue = line.split(',')
    
    # Sum the revenue into the respective country's account
    country_revenue_map[country] += float(revenue)

# Figure out the country with highest revenue
highest_revenue_country = sorted(country_revenue_map, key = lambda x: country_revenue_map[x], reverse = True)[0]

# Print the highest revenue country and the highest revenue to console
print(f"For 03/2010; Highest Revenue Country: {highest_revenue_country} | Highest Revenue: {country_revenue_map[highest_revenue_country]:.3f}")
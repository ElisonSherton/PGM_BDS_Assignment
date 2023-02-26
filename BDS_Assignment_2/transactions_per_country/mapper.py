#!/home/vinayak/anaconda3/bin/python
"""/home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/transactions_per_country/mapper.py"""

import sys

# Read the input from standard input
for line in sys.stdin:
    # Remove all the whitespaces
    line = line.strip()
    
    # Split any given record into corresponding fields
    *irrelevant_fields, customer_id, country = line.split(",")

    # We don't want to print the first line to the standard input
    # since it's only headers; Hence skip it
    if not country == "Country":
        print(f"{country},1")
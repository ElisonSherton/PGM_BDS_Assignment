#!/home/vinayak/anaconda3/bin/python
"""/home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/report_generation/mapper.py"""
# Assumptions 
# 1. Price is total price of the line item, not item per unit of the stockcode
# 2. Each line item is a transaction, i.e. multiple items bought by same person at same time is not one transaction but as many transactions as the number of line items

import sys
count = 0

# Read the input from standard input
for line in sys.stdin:
    # Remove all the whitespaces
    line = str(line)
    line = line.strip()
    
    # Split any given record into corresponding fields
    *irrelevant_fields, transaction_date, transaction_amount, customer_id, country = line.split(",")

    # We don't want to print the first line to the standard input
    # since it's only headers; Hence skip it
    if not country == "Country":
        # Only get the date part from the invoice date and drop the time part of it
        transaction_date, _ = transaction_date.split(" ")
        
        # Print the invoice date and the price associated with that line item
        print(f"{transaction_date.strip()},{transaction_amount.strip()}")
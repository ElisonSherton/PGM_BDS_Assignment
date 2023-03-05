#!/home/vinayak/anaconda3/bin/python
"""/home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_6/mapper.py"""

import sys
from datetime import datetime

banned_stock_codes = ["ADJUST","ADJUST2","AMAZONFEE","B",
                      "BANK CHARGES","C2","C3","D",
                      "DOT","GIFT","M",
                      "POST","S","TEST001","TEST002","m"]
banned_stock_codes = set(banned_stock_codes)

# Read the input from standard input
for line in sys.stdin:
    # Remove all the whitespaces
    line = line.strip()

    # Split any given record into corresponding fields
    rec_no, invoice, stock_code, *desc, quantity, invoice_date, price, cust_id, country = line.split(",")

    # We don't want to do any computation for the header of the file, hence skip the first line
    if not country == "Country":
        
        price = float(price); quantity = int(quantity)
        revenue = price * quantity
        
        # Parse the date appropriately
        # Some dates are delimited by / and some others are delimited by -
        # Some dates have hour-min-sec in time and some others have hour-min
        if len(invoice_date.split(":")) == 2:
            if "/" in invoice_date:
                dt = datetime.strptime(invoice_date, "%m/%d/%Y %H:%M")
            else:
                dt = datetime.strptime(invoice_date, "%m-%d-%Y %H:%M")
        else:
            if "/" in invoice_date:
                dt = datetime.strptime(invoice_date, "%m/%d/%Y %H:%M:%S")
            else:
                dt = datetime.strptime(invoice_date, "%m-%d-%Y %H:%M:%S")
        
        # Only select the dates which belong to the month of December 2010
        if (dt.month == 12) and (dt.year == 2010):
            # Check if the quantity and prices are positive
            if (price > 0) and (quantity > 0) and (revenue > 0):
                # Check if the stock code is not in the banned stock codes
                if stock_code not in banned_stock_codes:
                    print(f"{stock_code},{revenue}")
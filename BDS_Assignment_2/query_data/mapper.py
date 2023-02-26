#!/home/vinayak/anaconda3/bin/python
"""/home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/query_data/mapper.py"""

import sys
from datetime import datetime

query_params = {"invoice": ["489434"], 
                "stock_code": [],
                "quantity": [],
                "invoice_date": [],
                "price": [],
                "customer_id": [],
                "country": []}

# Read the input from standard input
for line in sys.stdin:
    # Remove all the whitespaces
    line = line.strip()
    
    # Split any given record into corresponding fields
    invoice, stock_code, *description, quantity, invoice_date, price, customer_id, country = line.split(",")

    # We don't want to print the first line to the standard input
    # since it's only headers; Hence skip it
    if not country == "Country":
        to_print = False
        if invoice in query_params["invoice"]: to_print = True
        elif stock_code in query_params["stock_code"]: to_print = True
        elif quantity in query_params["quantity"]: to_print = True
        elif price in query_params["price"]: to_print = True
        elif customer_id in query_params["customer_id"]: to_print = True
        elif country in query_params["country"]: to_print = True
        else:
            dt = datetime.strptime(invoice_date, '%m/%d/%Y %H:%M:%S')
            dt = dt.strftime(f"%d/%m/%Y")
            if dt in query_params["invoice_date"]: to_print = True
        
        if to_print: print(line)
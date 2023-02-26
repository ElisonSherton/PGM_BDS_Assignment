#!/home/vinayak/anaconda3/bin/python
"""/home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/transactions_per_country/reducer.py"""

import sys

current_customer = None
current_count = 0
customer = None

# Read the input from standard input
for line in sys.stdin:
    # Remove the leading and trailing whitespaces
    line = line.strip()

    # Parse the mapper input
    customer, count = line.split(',')

    # Convert the count into an integer value and 
    # continue if the provided count is not an integer
    try:
        count = int(count)
    except Exception as e:
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: country) before it is passed to the reducer
    if current_customer == customer:
        current_count += count
    else:
        if current_customer:
            print(f"{current_customer:<20}{current_count}")
        current_count = count
        current_customer = customer

# do not forget to output the last country!
if current_customer == customer:
    print(f"{current_customer:<20}{current_count}")
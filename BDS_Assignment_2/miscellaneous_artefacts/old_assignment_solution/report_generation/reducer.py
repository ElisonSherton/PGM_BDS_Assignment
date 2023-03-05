#!/home/vinayak/anaconda3/bin/python
"""/home/vinayak/Desktop/PGM_BDS_Assignment/BDS_Assignment_2/report_generation/reducer.py"""

import sys
from datetime import datetime
from collections import defaultdict

# Create dictionaries to keep running sum and running count of the transactions
datewise_transaction_dict = defaultdict(lambda: {"running_sum": 0, "running_count": 0})
weekwise_transaction_dict = defaultdict(lambda: {"running_sum": 0, "running_count": 0})
monthwise_transaction_dict = defaultdict(lambda: {"running_sum": 0, "running_count": 0})

# Read the input from standard input
for line in sys.stdin:
    # Remove the leading and trailing whitespaces
    line = line.strip()

    # Parse the mapper input
    transaction_date, transaction_amount = line.split(',')

    # Convert the amount into an integer value and 
    # continue if the provided count is not an integer
    try:
        transaction_amount = float(transaction_amount)
    except Exception as e:
        continue

    transaction_date = datetime.strptime(transaction_date, '%m/%d/%Y')

    day_key = transaction_date.strftime("%d-%m-%Y")
    week_key = f"Year: {transaction_date.year}; Week: {str(transaction_date.isocalendar()[1]):0<2}"
    month_key = transaction_date.strftime("%m-%Y")

    # Update the information in each of the dictionaries
    datewise_transaction_dict[day_key]["running_sum"] += transaction_amount
    datewise_transaction_dict[day_key]["running_count"] += 1

    weekwise_transaction_dict[week_key]["running_sum"] += transaction_amount
    weekwise_transaction_dict[week_key]["running_count"] += 1

    monthwise_transaction_dict[month_key]["running_sum"] += transaction_amount
    monthwise_transaction_dict[month_key]["running_count"] += 1


print(f"#############################  Monthwise Reporting  #############################")
for k, v in monthwise_transaction_dict.items():
    total_amount = v["running_sum"]
    volume = v["running_count"]
    avg_amount = total_amount /volume
    print(f"{k}  |  Volume: {str(volume):<5}  | Average Amount: {avg_amount:.3f} | Total Amount: {total_amount:.3f}")
    

print("#############################  Weekwise Reporting  #############################")
for k, v in weekwise_transaction_dict.items():
    total_amount = v["running_sum"]
    volume = v["running_count"]
    avg_amount = total_amount /volume
    print(f"{k}  |  Volume: {str(volume):<5}  | Average Amount: {avg_amount:.3f} | Total Amount: {total_amount:.3f}")
    
print("#############################  Datewise Reporting  #############################")
for k, v in datewise_transaction_dict.items():
    total_amount = v["running_sum"]
    volume = v["running_count"]
    avg_amount = total_amount /volume
    print(f"{k}  |  Volume: {str(volume):<5}  | Average Amount: {avg_amount:.3f} | Total Amount: {total_amount:.3f}")
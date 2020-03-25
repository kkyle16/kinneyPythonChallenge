import os
import csv

file = os.path.join("Resources", "budget_data.csv")

# Establishing thr variables to be used
total_months = 0
total_profit = 0
monthly_average_profit = 0
greatest_inc = 0
greatest_inc_month = ""
greatest_dec = 0
greatest_dec_month = ""
changes = []

# Additional variables to use inside the for loop
prev_pl = 0
first_loop = True

# Opens the csv file to begin searching through data
with open(file) as data:
    csvreader = csv.reader(data, delimiter = ",")
    header = next(csvreader)

    for row in csvreader:
        date = row[0]
        pl = int(row[1])
        total_profit += pl
        total_months += 1

        # Tracks the month to month change, starting between the first and second month. 
        change = pl - prev_pl
        if first_loop == False:
            changes.append(change)
        if change > greatest_inc:
            greatest_inc = change
            greatest_inc_month = date
        if change < greatest_dec:
            greatest_dec = change
            greatest_dec_month = date
        
        prev_pl = pl
        first_loop = False

avg_change = sum(changes) / len(changes)

#Outputs the information gathered from the csv
analysis = f"""
Total Profit: ${total_profit}
Total Months: {total_months}
Average Monthly Change: ${avg_change}
Greatest Increase: {greatest_inc_month}, ${greatest_inc}
Greatest Decrease: {greatest_dec_month}, ${greatest_dec}
"""
print(analysis)

# Outputs the results in a text file
output_file = "output.txt"
with open(output_file, "w") as doc:
    doc.write(analysis)
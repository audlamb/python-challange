import os
import csv

csvpath = os.path.join("..", "Data", "budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    
    totPL= 0
    netPL = 0
    totchange = 0
    maxchange = 0
    minchange = 0
    for i, row in enumerate(csvreader):
        PL = int(row[1])
        totPL = totPL + PL
        if i > 0:
            change = PL - prePL
            totchange = totchange + change
            if change > maxchange:
                maxchange = change
                maxmonth = row[0]
            if change < minchange:
                minchange = change
                minmonth = row[0]
        prePL = PL

count = i + 1
avechange = totchange/i

print("Financial Analysis\n---------------------------------")
print(f"Total Months: {count}")
print(f"Total: ${totPL}")
avechange = '${:,.2f}'.format(avechange)
print(f"Average Change: {avechange}")
print(f"Greatest Increase in Profits: {maxmonth} ${maxchange}")
print(f"Greatest Decrease in Profits: {minmonth} ${minchange}")
print("-----------------------------------")

#Create .txt file
outputfile = os.path.join('..', 'Data', 'BudgetSummary.txt')
with open(outputfile, "w") as txt_file:
    txt_file.write("Financial Analysis\n---------------------------------\n")
    txt_file.write(f"Total Months: {count}\n")
    txt_file.write(f"Total: ${totPL}\n")
    txt_file.write(f"Average Change: {avechange}\n")
    txt_file.write(f"Greatest Increase in Profits: {maxmonth} ${maxchange}\n")
    txt_file.write(f"Greatest Decrease in Profits: {minmonth} ${minchange}\n")
    txt_file.write("-----------------------------------")

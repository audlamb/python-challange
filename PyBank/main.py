import os
import csv

bank_csv = os.path.join('Data', 'budget_data.csv')

with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")





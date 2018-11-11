import os
import csv

csvpath = os.path.join("..", "Data", "election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    
    
    totvotes = 0
    mydict = {}
    
    for i, row in enumerate(csvreader):
        cand = row[2]
        totvotes += 1
       
        if cand in mydict:
            mydict[cand] += 1
       
        else:
            mydict[cand] = 1

maxvotes =  0
winner = " "

print(f'Election Results\n--------------------------------')
print(f'Total Votes: {totvotes}\n---------------------------')
for key, value in mydict.items():
    print(f'{key}: {value/totvotes*100:.3f}% ({value})')
    if value > maxvotes:
        maxvotes = value
        winner = key
print("--------------------------------------")
print(f'Winner: {winner}')
print("--------------------------------------")

#Create .txt file

outputfile = os.path.join('..', 'Data', 'ElectionResults.txt')
with open(outputfile, "w") as txt_file:
    txt_file.write(f'Election Results\n--------------------------------\n')
    txt_file.write(f'Total Votes: {totvotes}\n---------------------------\n')
    for key, value in mydict.items():
        txt_file.write(f'{key}: {value/totvotes*100:.3f}% ({value})\n')
        if value > maxvotes:
            maxvotes = value
            winner = key
    txt_file.write('--------------------------------------\n')
    txt_file.write(f'Winner: {winner}\n')
    txt_file.write('--------------------------------------\n')
import csv

infile=open("EmployeePay.csv","r")

csvfile=csv.reader(infile, delimiter=',')

for record in csvfile:
    print(record[1]+' '+record[2]+', '+record[4])

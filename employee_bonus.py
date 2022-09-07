import csv

infile=open("EmployeePay.csv","r")

csvfile=csv.reader(infile, delimiter=',')
infile.readline()
for record in csvfile:
    full_name=record[1]+ ' '+record[2]
    salary=int(record[3])
    bonus=float(record[4])
    total_bonus=int(salary*bonus)
    total_pay=int(total_bonus+salary)
    print("Full Name: ",full_name)
    print("Total_Salary: $",salary)
    print("Total Bonus: $",total_bonus)
    print("Total Pay: $",total_pay)
    print('\n')


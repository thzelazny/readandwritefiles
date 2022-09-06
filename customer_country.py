import csv

infile=open("customers.csv","r")
outfile=open("customer_country.csv","w")

csvfile=csv.reader(infile, delimiter=',')

outfile.write("FullName, Country")

for customer in csvfile:
    outfile.write(customer[1]+" "+customer[2]+","+" "+customer[4])
    outfile.write("\n")

outfile.close()



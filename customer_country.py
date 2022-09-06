import csv

infile=open("customers.csv","r")
outfile=open("customer_country.csv","w")

csvfile=csv.reader(infile, delimiter=',')

next(csvfile)
outfile.write("Full Name, Country\n")

for customer in csvfile:
    full_name=customer[1] + " " + customer[2]
    country=customer[4]
    outfile.write(full_name+ ', ' + country+ '\n')
    #outfile.write(customer[1]+" "+customer[2]+","+" "+customer[4])
    #outfile.write("\n")

outfile.close()



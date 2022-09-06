import csv

infile=open("steps.csv","r")
outfile=open("avg_steps.csv","w")

csvfile_old=csv.reader(infile, delimiter=',')
csvfile_new=csv.reader(outfile, delimiter=',')

for n in 
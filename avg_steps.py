import csv

infile=open("steps.csv","r")
outfile=open("avg_steps.csv","w")

csvfile_old=csv.reader(infile, delimiter=',')
#csvfile_new=csv.reader(outfile, delimiter=',')

csvinput=csv.writer(outfile)

infile.readline()
num_days1=0
num_days2=0
num_days3=0
num_days4=0
num_days5=0
num_days6=0
num_days7=0
num_days8=0
num_days9=0
num_days10=0
num_days11=0
num_days12=0

total_steps1=0
total_steps2=0
total_steps3=0
total_steps4=0
total_steps5=0
total_steps6=0
total_steps7=0
total_steps8=0
total_steps9=0
total_steps10=0
total_steps11=0
total_steps12=0
for record in csvfile_old:
    steps=int(record[1])

    if record[0]=="1":
        num_days1+=record.count(record[0])
        total_steps1+=steps
        avg_steps1=total_steps1/num_days1

        

    if record[0]=="2":
        num_days2+=record.count(record[0])
        total_steps2+=steps
        avg_steps2=total_steps2/num_days2
    
    if record[0]=="3":
        num_days3+=record.count(record[0])
        total_steps3+=steps
        avg_steps3=total_steps3/num_days3
    
    if record[0]=="4":
        num_days4+=record.count(record[0])
        total_steps4+=steps
        avg_steps4=total_steps4/num_days4

    if record[0]=="5":
        num_days5+=record.count(record[0])
        total_steps5+=steps
        avg_steps5=total_steps5/num_days5
    
    if record[0]=="6":
        num_days6+=record.count(record[0])
        total_steps6+=steps
        avg_steps6=total_steps6/num_days6
    
    if record[0]=="7":
        num_days7+=record.count(record[0])
        total_steps7+=steps
        avg_steps7=total_steps7/num_days7

    if record[0]=="8":
        num_days8+=record.count(record[0])
        total_steps8+=steps
        avg_steps8=total_steps8/num_days8

    if record[0]=="9":
        num_days9+=record.count(record[0])
        total_steps9+=steps
        avg_steps9=total_steps9/num_days9

    if record[0]=="10":
        num_days10+=record.count(record[0])
        total_steps10+=steps
        avg_steps10=total_steps10/num_days10
    
    if record[0]=="11":
        num_days11+=record.count(record[0])
        total_steps11+=steps
        avg_steps11=total_steps11/num_days11
    
    if record[0]=="12":
        num_days12+=record.count(record[0])
        total_steps12+=steps
        avg_steps12=total_steps12/num_days12

csvinput.writerow(["January",format(avg_steps1,",.2f")])
csvinput.writerow(["February",format(avg_steps2,",.2f")])
csvinput.writerow(["March",format(avg_steps3,",.2f")])
csvinput.writerow(["April",format(avg_steps4,",.2f")])
csvinput.writerow(["May",format(avg_steps5,",.2f")])
csvinput.writerow(["June",format(avg_steps6,",.2f")])
csvinput.writerow(["July",format(avg_steps7,",.2f")])
csvinput.writerow(["August",format(avg_steps8,",.2f")])
csvinput.writerow(["September",format(avg_steps9,",.2f")])
csvinput.writerow(["October",format(avg_steps10,",.2f")])
csvinput.writerow(["November",format(avg_steps11,",.2f")])
csvinput.writerow(["December",format(avg_steps12,",.2f")])


outfile.close()

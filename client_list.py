def main():
    infile=open("clients.txt","r")
    
    client_number=1
    for n in infile:
        print(client_number,". ",n.rstrip("\n"),sep='')
        client_number+=1
    

main()
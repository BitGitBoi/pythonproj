d=input("Enter department name ")
did=int(input("Enter department id "))
ba=input("Enter all batches ")
bano=int(input("Enter the no. of batches that gave exam"))
s=1
print("Enter the marks of all the above batches")
while bano==1:
    mar=int(input("Enter Marks "))
    s=s*mar
    bano=bano-1
    break

avg=s/bano
print("All the batches ",ba)
print("Average marks of all the batches ",avg)

import csv    

fields = ['dep id', 'dep name', 'batches'] 
    

rows = [ [did,d,ba]] 
    
 
filename = "depdet.csv"
    
 
with open(filename, 'w') as csvfile: 
   
    csvwriter = csv.writer(csvfile) 
        
     
    csvwriter.writerow(fields) 
        
   
    csvwriter.writerows(rows)




    

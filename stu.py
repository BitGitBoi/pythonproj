name=input("Enter name ")
id=int(input("Enter ID "))
roll=int(input("Enter roll "))
ba=input("Enter batch ")

print("Name - ",name)
print("ID - ",id)
print("Roll - ",roll)
print("batch - ",ba)

n=int(input("1. Update student, 2. Remove student"))
if n==1:
    name=input("Enter name ")
    id=int(input("Enter ID "))
    roll=int(input("Enter roll "))
    ba=input("Enter batch ")
    print("Updated Details")
    print("Name - ",name)
    print("ID - ",id)
    print("Roll - ",roll)
    print("batch - ",ba)
elif n==2:
    id=0
    roll=0
else:
    print("Wrong input")

ma=int(input("Enter marks in maths "))
sc=int(input("Enter marks in science"))
eng=int(input("Enter marks in english"))
avg=(ma+sc+eng)/3
if avg>=90:
    print("grade A")
elif avg>=80:
    print("grade B")
elif avg>=70:
    print("grade C")
elif avg>=60:
    print("grade D")
elif avg>=50:
    print("grade E")
elif avg<50:
    print("Fail")
else:
    print("wrong")

f= open("detail.txt","w+")
f.write("Grades. A=90,B=80,C=70,D=60,E=50,F=Fail")
f.close()

import csv    

fields = ['Name', 'Branch', 'Year', 'CGPA'] 
    

rows = [ [name,'CSE','2022',avg]] 
    
 
filename = "studentdet.csv"
    
 
with open(filename, 'w') as csvfile: 
   
    csvwriter = csv.writer(csvfile) 
        
     
    csvwriter.writerow(fields) 
        
   
    csvwriter.writerows(rows)
    

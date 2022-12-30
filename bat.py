b=input("Enter Batch ")
bid=int(input("Enter batch id "))
dep=input("Enter department name ")
co=input("List of courses in the batch ")
print("Enter students in the batch and their marks ")

class Student(object):
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    
    def getmarks(self):
        return self.marks
    
    def getroll(self):
        return self.roll
    
    def __str__(self):
        return self.name + ' : ' + str(self.getroll()) +'  ::'+  str(self.getmarks())
  
  
def Markss(rec, name, roll, marks):
    rec.append(Student(name, roll, marks))
    return rec


Record = []
x = 'y'
while x == 'y':
    name = input('Enter the name of the student: ')
    height = input('Enter the roll number: ')
    roll = input('Marks: ')
    Record = Markss(Record, name, roll, height)
    x = input('another student? y/n: ')
    

n = 1
for el in Record:
    print(n,'. ', el)
    n = n + 1

print("List of all courses taught ",co)

import csv    

fields = ['Batch id','Batch name', 'department', ' courses', 'student'] 
    

rows = [ [bid,b,dep,co,name]] 
    
 
filename = "batchdet.csv"
    
 
with open(filename, 'w') as csvfile: 
   
    csvwriter = csv.writer(csvfile) 
        
     
    csvwriter.writerow(fields) 
        
   
    csvwriter.writerows(rows)

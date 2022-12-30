e=input("Enter the name of the examination/course ")
print("Details of the examination")

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

class Student:
    def __init__(self):
        self.rollno = None
        self.name = None
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name
    def display(self):
        print ("rollno:",self.rollno,"name:",self.name)

student1 = Student(1000,'Ganesh')
student2 = Student(1001,'Ramesh')
student3 = Student(1002,'Vinesh')
student4 = Student()
print (student1.display())
print (student2.display())
print (student3.display())
print (student4.display())

class Student:

    def __init__(self):
        self.name = ""

    def get_name(self):
        print ("get_name is called")
        return self.name

    def set_name(self,name):
        print ("set_name is called")
        self.name = name

    def del_name(self):
        print ("del_name is called")

    def doc_name(self):
        return self.name.__doc__
        print ("doc_name is called")

    student_name = property(get_name,set_name,del_name,doc_name)

s = Student()
print ("setting student name")
s.student_name = "Govind"
print (s.student_name)
print (s.student_name.__doc__)
del s.student_name

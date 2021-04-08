class Student:

    def __init__(self):
        self.__name = ""

    # here sname is taken as a reference and all setter and getter property will be based on this name
    @property
    def sname(self):
        print ("getter is called")
        return self.__name

    @sname.setter
    def sname(self,name):
        print ("setter is called")
        self.__name = name

    @sname.deleter
    def sname(self):
        print ("deleter is called")
        del self.__name

s = Student()
print ("setting name of the student")
s.sname = "Govind"
print ("getting name of the student")
print (s.sname)
print ("deleting name of the student")
del s.sname

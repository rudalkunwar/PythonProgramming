class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printme(self):
        print(self.fname +" and " + self.lname)
class Student(Person):
    pass
obj = Person("rudal","kunwar")
obj.printme()
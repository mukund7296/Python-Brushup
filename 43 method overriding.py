class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname1(self):
    print(self.lastname,self.firstname)


class Student(Person):
    pass
class Emp(Person):
    pass
a1=Student("Mukund","Biradar")
a1.printname1()

a1=Emp("Mukund","Biradar")
a1.printname1()
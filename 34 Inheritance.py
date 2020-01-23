"""Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class."""


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname1(self):
    print(self.lastname,self.firstname)

  def printname2(self):
      print(self.lastname,self.firstname, self.lastname)

class Student(Person):


  def printname3(self):
    print(self.firstname, self.lastname)

  def printname4(self):
      print(self.firstname, self.lastname)

class Girls(Student):


  def printname5(self):
    print(self.firstname, self.lastname)
    print("This is girls class")

  def printname6(self):
      print(self.firstname, self.lastname)
      print("This is girls class")
#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname1()
x.printname2()
b1=Student("Mukund" ,"Biradar")
b1.printname3()
b1.printname4()
b1.printname1()
b1.printname4()
G1=Girls("Shaurya","Biradar")
G1.printname4()
G1.printname3()
G1.printname6()

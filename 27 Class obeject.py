'''Python Classes/Objects
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.

Example :-  Any table is like template and we use object to store data in row wise using object'''

#Create a class named Person, use the __init__() function to assign values for name and age:
class Person:            #Class

  def __init__(self, name, age):        #initiallizing attributes
    self.name = name                    #attribute
    self.age = age                      #attribute


p1 = Person("John", 36)              #object p1 and passing two values
p1.name="arvind"
print(p1.name)                        #print one attibute
print(p1.age)

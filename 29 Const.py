# consturctor

class Person:
    def __init__(self,name,address):
        self.name=name
        self.address=address

#here is the Objects
c1=Person("Mukund","Beijing") # object c1 & "Computer" is your contructor
c2=Person("Uday","USA") # object c2 & "Computer" is your contructor
c3=Person("Hansraj","Dubai") # object c3 & "Computer" is your contructor
c4=Person("Ananad","Pune") # object c4 & "Computer" is your contructor
c5=Person("Rajesh","Banglore") # object c5 & "Computer" is your contructor

# lets print the location of the objects
print(id(c1))
print(id(c2))
print(id(c3))
print(id(c4))
print(id(c5))
# values
print(c1.name,c1.address)
print(c2.name,c2.address)
print(c3.name,c3.address)
print(c4.name,c4.address)
print(c5.name,c5.address)
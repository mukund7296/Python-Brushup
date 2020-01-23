#Constructors are generally used for instantiating an object.
#Syntax of constructor declaration :

def __init__(self):
    pass
    # body of the constructor
"""
Types of constructors :
default constructor :The default constructor is simple constructor which doesn’t accept any arguments.
It’s definition has only one argument which is a reference to the instance being constructed.
parameterized constructor :constructor with parameters is known as parameterized constructor.
The parameterized constructor take its first argument as a reference to the instance being constructed
known as self and the rest of the arguments are provided by the programmer.
"""
class GeekforGeeks:
	geek = ""

	# default constructor
	def __init__(self):
		self.geek = "GeekforGeeks"

	# a method for printing data members
	def print_Geek(self):
		print(self.geek)


# creating object of the class
obj = GeekforGeeks()

# calling the instance method using the object obj
obj.print_Geek()

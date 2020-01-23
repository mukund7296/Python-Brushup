'''
Python Operators

Operators are used to perform operations on variables and values.

Python divides the operators in the following groups:

    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators

'''

print("Python Arithmetic Operators ")
x=120
y=30
print("Addition ",x + y)
print("Subtraction ",x - y)
print("divison ",x / y)
print("Multiplication ",x * y)
print("Floor division ",x // y)
x=10
y=3
print("Modelo reminder",x % y)
print("Power of x ",x ** y)
print("Python Assignment Operators  ")
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 3
print(x)
x=10
x >>= 2
print(x)
print("Python Comparison Operators ")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x in z)

# returns True because z is the same object as x

print(x is y)
print(x not in  y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

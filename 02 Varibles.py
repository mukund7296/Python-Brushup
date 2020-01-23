#Creating Variables

#Variables are containers for storing data values.
x = 5
y = "John"
print(x)
print(y)
# x value got changed
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

x = "John"
print(x)
# is the same as
x = 'John'
print(x)
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Orange"
print(x)
print(y)
print(z)
x = "Python is "
y = "awesome"
z =  x + y
print(z)


x = "awesome"  # global variable

def myfunc():
  x = "fantastic"  # local variblee
  print("Python is " + x)

myfunc()
myfunc()

print("Python is " + x)
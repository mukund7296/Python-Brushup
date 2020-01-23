# Functions in python
def even_odd(x):
    if x%2==0:
        return "This is even number"
    else:
        return "this is odd number"

print(even_odd(12))
print(even_odd(11))


# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# Python program to illustrate
# *kargs for variable number of keyword arguments

def myFun(**kwargs):
	for key, value in kwargs.items():
		print ("%s == %s" %(key, value))

# Driver code
myFun(first ='Geeks', mid ='for', last='Geeks')

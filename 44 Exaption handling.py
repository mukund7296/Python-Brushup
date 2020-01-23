a=20
b=10
try:
    print("Start program execution ")
    c=a/b
    print("Addition :- ",c)
except Exception as e:
    print("we dont divide by zero",e)
finally:

    print("End program execution ")
# a Box is just tag to refereing some locations


a=10
b=10
c=10

print(id(a))
print(id(b))
print(id(c))
a=9
print(id(a))
a=None
print(a)
b=True+True
print(b)
c=False+False
print(c)

c=int(True)
print(c)
c=str(True)
print(c)
c=float(True)
print(c)
c=complex(True)
print(c)

d=list(range(1,11,2))
print(d)
"""Python Iterators
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values."""

mytuple = ("apple", "banana", "cherry")
a = iter(mytuple)

print(next(a))
print(next(a))
print(next(a))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
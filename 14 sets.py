# sets
"""
Set

A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
Example

Create a Set:

"""
thisset = {"apple", "banana", "banana","cherry"}
print(thisset)
thisset.add("orange")

print(thisset)
thisset.remove("banana")

print(thisset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
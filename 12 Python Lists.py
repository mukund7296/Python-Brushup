"""
Python Collections (Arrays)

There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered and unindexed. No duplicate members.
    Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
List

A list is a collection which is ordered and changeable. In Python lists are written with square brackets."""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
#indexing with list
print(thislist[0])
# negative indexing
print(thislist[-1])
# reverse indexing
print(thislist[::-1])


# range of indexing
print(thislist[2:5])

# adding new fruite in list at 2 position
thislist[2]="MMango"
print(thislist)
# removing one item from list
thislist.remove("MMango")
print(thislist)
thislist.append("Kela")
thislist.append("Kela")
print(thislist)
thislist.reverse()
print(thislist)
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# copy of list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


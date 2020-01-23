from array import *

#An array is a data structure that stores values of same data type.
# In Python, this is the main difference between arrays and lists.

import array as arr

numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)
print(numbers_array[2:5])  # 3rd to 5th
print(numbers_array[:-5])  # beginning to 4th
print(numbers_array[5:])  # 6th to end
print(numbers_array[:])  # beginning to end

var1=arr.array('i',[1,2,3,4,5,6,7,8,9])
print(var1[::-1])
print(var1[-1])
print(var1[1])

# diffrent types of data types.
# python have default string.
# if you want " between then sue   'wrap with single quote'
# if you want ' between then use "wrap your string here"
print('Mukund Biradar')
print("Mukund's Biradar Laptops's")
print('Mukund"s" Biradar Laptops')
print('Mukund\'s Biradar Laptops')

# raw data or string we use to r"abcdefgh"
print(r"C:\Users\Mukund\Downloads\navine")
print(r"C:\Users\Mukund\Downloads\navine")

'''Built-in Data Types
In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:
Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	dict
Set Types: 	set, frozenset
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview'''

# python default data type is string
x=''
print(type(x))

x = 5
print(type(x))
x = 5.9
print(type(x))
x = "5"
print(type(x))
x = [1,2,3,4,5,6]
print(type(x))
x = (1,2,3,4,5,6)
print(type(x))
x = {1,2,3,4,5,6}
print(type(x))
x = {1:"mukund",3:"Harish",5:"anand"}
print(type(x))
x = complex(1j)
print(type(x))
x = list(("apple", "banana", "cherry"))
print(type(x))
x = (("apple", "banana", "cherry"))
print(type(x))
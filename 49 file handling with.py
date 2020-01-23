file = open("welcome.txt")

data = file.read()

print(data)

file.close()  # It's important to close the file when you're done with it
with open("welcome.txt") as file: # Use file to refer to the file object

   data = file.read()

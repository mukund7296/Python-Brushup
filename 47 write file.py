# file handling
ob1=open("mukund1.txt","w")
print(ob1.write("Hello boss i am in love with beijing job"))  # stating 9 characters
print(ob1.writelines("\nHello how are you \n i am good bro \n how is oyour family"))


ob1=open("mukund1.txt","a")
print(ob1.write("\nHello boss i am in love with beijing job"))  # stating 9 characters
print(ob1.writelines("\nHello how are you \n i am good bro \n how is oyour family"))

for i in ob1.readline():
    print(i)
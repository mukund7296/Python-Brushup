for i in range(1,6):
    print(i*"* ")
print("# " *20)
for i in range(5,1,-1):
    print(i*"* ")

x=int(input("Enter your number :"))

for i in range(1,x):
    if i>=5:
        break

    print(i,"Candy ")
print("Candy out of stocks")

for i in range(0,100):
    if i%15==0:
        print(i)

for i in range(0,100,3):
    print(i)

for i in range(1,100,2):
    print(i)
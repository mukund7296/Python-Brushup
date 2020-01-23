# how to create class

class Person():
    # how to initialize attributes
    # init method we use to create methods

    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
    def details(self):
        print( "Name :-",self.name,"\nAge :-",self.age,"\nHeight :-",self.height,"\nWeight :-",self.weight)



ob1=Person("Mukund Biradar",33,113,"6.3 feet")  # self value is ob1 now
print(ob1.details())


ob2=Person("Shaurya Biradar",18,23,"2.3 feet")  # self value is ob2 now
print(ob2.details())
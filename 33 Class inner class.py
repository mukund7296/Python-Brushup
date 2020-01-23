class Students:


    def __init__(self,name,rollno):  #constructor
        self.name=name
        self.rollno = rollno
        self.Lap=self.Laptop()

    def show(self):
        print (self.name,self.rollno,self.Lap.show())

    class Laptop:

        def __init__(self):
            self.Name="Mac pro"
            self.Model="I5 mac pro"
            self.Ram=16


        def show(self):
            print(self.Name,self.Model,self.Ram)

s1=Students("Mukund",55)
s2=Students("Shaurya",5)

s1.show()
print("-"*12)
s2.show()
#  _INIT_METHOD

class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print(f"Laptop configuration : =",self.cpu,"\nRam is :-",self.ram)

#objects we passing values in initialized objects
ob1=Computer("Mac book pro","64 Gb")
ob2=Computer("dell Laptop","16 Gb")
ob3=Computer("Sony Vios","32 Gb")
ob4=Computer("Huwai","16 Gb")
ob5=Computer("Hp Laptop","8 Gb")

#printing the object with functions
print(ob1.config())
print(ob2.config())
print(ob3.config())
print(ob4.config())
print(ob5.config())
class Students:
    Education="bachlor"
    School="W3school"
    """ static variable it will change for everyone"""
    def __init__(self,sub1,sub2,sub3,sub4,sub5):  #constructor
        self.sub1=sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4
        self.sub5 = sub5
    def avg(self):
        return (self.sub1+self.sub2+self.sub3+self.sub4+self.sub5)/5

    @classmethod
    def info(self):
        return self.School,self.Education
    @staticmethod
    def educt():
        return "This is awesome"

subject1=Students(90,50,40,55,90)

print(subject1.avg())
#subject marks
print(subject1.sub2)
print(Students.info())
print(Students.educt())
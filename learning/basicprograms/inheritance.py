#creating a parent class
class person:
    def __init__(self,firstname,lastname):
        self.fname=firstname
        self.lname=lastname
    def printname(self):
        print(self.fname, self.lname)
p1=person("Priyanka","Dhatrak")
p1.printname()

#creating child class
class student:
    #if create init function in child class it will not inherit parent class methods and properties
    def __init__(self, fname, lname,year):
        #so to keep inhereting we need to call parent class init using super keyword or class name because child class overrides init function
        super().__init__(fname, lname) #by doing this we have achieved inheritance of parent class and also added init function
        self.passoutyear=year
x=student("Mike","Tyson",2020)
x.printname()
print(x.passoutyear)
#creating a class
class demo:
    x="priyanka" #property(data)
    print(x)
d= demo()   # object creation
d.x

#init function
class person:
    def __init__(self,id,name):
        self.id=id
        self.name=name
p=person(1,"priyanka")

print(p.id)
print(p.name)

class people:
    def __init__(sillyobj,name,age):
        sillyobj.name=name
        sillyobj.age=age
    def myfunc(abc):
        print("Hello My name is "+abc.name)
        print("My age is ",abc.age)
p1=people("Raksha",23)
p1.age=40
p1.myfunc()

class percent:
    pass
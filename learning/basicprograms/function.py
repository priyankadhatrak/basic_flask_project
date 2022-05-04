# function is defined using def keyword
#creating function
from msilib.schema import Complus
from re import X


def myfunc():
    print("hiii")
#calling function
myfunc()

#arguments-1 args
def MYFUNC(fname):
    print(fname,"D.")
MYFUNC("priyanka")
MYFUNC("Sanjay")
MYFUNC("chhaya")

# 2 args
def newfunc(fname,lname):
    print(fname+" "+lname)
newfunc("priyanka","dhatrak")
#u can also give values like and in this case order does not matter
newfunc(fname='Taranjot singh',lname="Saini")
#and in case udk how many args is need we put * before the variable name like func(*colors)
def func(*colors):
    print("my favourite color  is " +colors[4])
func("red","yellow","green","black","white","pastel colors")

#default value
def country(country="India"):
    print("My country is "+country)
country("USA")
country("UK")
country()

#passing list as args
def food(food):
    print(food)
cuisine=["indian","continental","japanese","chinese"]
food(cuisine)

#return function
def add(x):
    return 4+x

print(add(3))
print(add(5))
print(add(4))
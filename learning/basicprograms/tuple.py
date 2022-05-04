#Tuple items are ordered, unchangeable, and allow duplicate values.
#ordered-When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#unchangeable- Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#allow duplicate values- Since tuples are indexed, they can have items with the same value:

mytuple = ("apple", "banana", "cherry")#tuple created
'''print(len(mytuple)) #length of a tuple

#Access Tuple Items
print(mytuple[1])

#Negative Indexing
print(mytuple[-1])

#Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])'''

#Change Tuple Values- to change value we will convert the tuple in a list & then change the value
y=list(mytuple)
y[1]="kiwi"
mytuple=tuple(y)
print(mytuple)

#Add Items
y=list(mytuple)
y.append("orange") #append is used to add elements
mytuple=tuple(y)
print(mytuple)

#Add tuple to a tuple
y=("berry",)
mytuple+= y
print(mytuple)

#remove items
y=list(mytuple)
y.remove("cherry")
mytuple=tuple(y)
print(mytuple)

#unpacking- extracting values back to the variable
fruit=('apple', 'kiwi','orange','berry')
(*green, orange, red)=fruit
print(green)
print(orange)
print(red)
print("\n")

#loops tuple
#for loop
fruit=('apple', 'kiwi','orange','berry')
for x in fruit:
    print(x)
#while loop
fruit=('apple', 'kiwi','orange','berry')
i=0
while(i<len(fruit)):
    print(fruit[i])
    i=i+1

#join tuple 
#go to line 31

#multiply tuple
fruit=('apple', 'kiwi','orange','berry')
basket= fruit*2
print(basket)
tup=(1,2,3,4,5,6,7,8,9,10)
x1=tup.index(7)
print(x1)
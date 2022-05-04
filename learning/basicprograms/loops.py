'''#while loop
x=0
while x<6:
    x+=1
    if x==3:
     #break
      continue
    print(x)
else:
  print("x is not less than 6 anymore")

#for loop
# x is iterating in fruits.
from argparse import BooleanOptionalAction


fruits=["apple","banana","cherry"]
for x in fruits:
  print(x) 

 #String looping
#it loops the given string
for x in "apple":
  print(x)

#break 
# it breaks the iteration of the loop
for x in fruits:
  print(x)
  if x=="banana":
    break

#continue
#it stops the current iteration and continues to the next iteration
for x in fruits:
  if x=="banana":
    continue
  print(x)

#range function
# it has 3 parameters initial point i.e 1, final point i.e 6, and increment i.e 2
#by default initial point is 0 and we are suppose to specify the final point  and by default increment is by 1
# so specifying the final value is compulsory
for x in range(1,16,2): 
  print(x)'''

#nested for
color={"red","yellow","green"}
fruits=["apple","banana","cherry"]
for x in fruits:
  for y in color:
    print(x,y)

#pass keyword
for x in [1,4,8,12,16]:
  pass
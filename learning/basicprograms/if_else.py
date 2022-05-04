#if statement
a=30
b=20
'''if (a<b):
    print("\"b\" is greater")
#elif keyword
elif(a==b):
    print("a & b are equal")
else:
    print("\"a\" is greater")'''
#short hand if
if a>b: print("a greater")
#short hand if else
print("a greater") if a>b else print("b greater")
#nested if
x=95.9
if x>80:
    print("Score: A- grade")
    if x>90:
        print("Score: A+ grade")
    else:
        print("Score: B+ grade")
else:
    print("Score: B- grade")
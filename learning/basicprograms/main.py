#creating a calculator
def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("SELECT ONE:")
print("1.ADDITION.")
print("2.SUBSTRACTION.")
print("3.MULTIPLICATION.")
print("4.DIVISION.")

choice= input("Enter choice(1/2/3/4):")

num1=int(input("enter first number: "))
num2=int(input("enter second number: "))

if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
    print(num1,"-",num2,"=",substract(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("INVALID CHOICE.")
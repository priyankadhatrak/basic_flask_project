from glob import glob
import re
print("our magical calculator.")
print("Type 'quit' to exit\n")

previous=0
run=True

def performMath():
    global previous
    global run
    equation=""
    if previous==0:
        equation= input("enter equation:")
    else:
        equation=input(str(previous))
    
    if equation =='quit':
        run= False
        print("bye bye")
    else:
        equation=re.sub('[a-zA-Z!" ".,:]','[]',equation)

        if previous==0:
          previous=eval(equation)
        else:
            previous=eval(str(previous)+equation)

while run:
    performMath()
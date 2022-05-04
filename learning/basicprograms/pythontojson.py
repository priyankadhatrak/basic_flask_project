#serializing
#python to json
from tkinter import W
import simplejson as json
#dump
y=  {
    "user": {
        "name": "satyam kumar",
        "age": 21,
        "Place": "Patna",
        "Blood group": "O+"
    }
}
with open("employee.json","w") as write:
    n=json.dump(y,write)
    print (n)

#dumps
z= {"emp_name":"Priyanka","email":"priyanka@gmail.com","job_profile":"trainee"}
m=json.dumps(z)
print(z)
import simplejson as json

data={
    "user": 
    {
        "name": "satyam kumar",
        "age": 21,
        "Place": "Patna",
        "Blood group": "O+"
    }
}

with open("employee.json","w") as write:
    json.dump(data,write)
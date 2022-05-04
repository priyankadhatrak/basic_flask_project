import simplejson as json

def write_json(new_data,filename='employee.json'):
    with open(filename,'r+') as file:
        file_data=json.load(file)
        file_data["emp_details"].append(new_data)
        file.seek(0)
        json.dump(file_data,file,indent=4)

y=  {"emp_name":"Anant",
     "email":"anant@gmail.com",
     "job_profile":"trainee"
    }

write_json(y) 
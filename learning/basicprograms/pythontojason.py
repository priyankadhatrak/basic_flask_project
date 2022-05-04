#python to json
import simplejson as json

y=  {"emp_name":"Anant",
     "email":"anant@gmail.com",
     "job_profile":"trainee"
    }
n=json.dumps(y)
print (n)

#json to python
z= '{"emp_name":"Anant","email":"anant@gmail.com","job_profile":"trainee"}'
m=json.loads(z)
print(z)
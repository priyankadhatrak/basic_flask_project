#deserialize
#json to python
import simplejson as json


z= '{"emp_name":"Priyanka","email":"priyanka@gmail.com","job_profile":"trainee"}'
m=json.loads(z)
print(z)

d=open('employee.json')

d=json.load(d)
print(d)
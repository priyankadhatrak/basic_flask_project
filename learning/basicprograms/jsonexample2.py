from unittest import result
import simplejson as json

employee= '{"name": "amy", "id": 777, "department": "IT"}'

result=json.loads(employee)
print(result)
print(type(result))

print(json.dumps(result))
print(type(json.dumps(result)))
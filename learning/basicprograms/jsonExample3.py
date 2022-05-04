#update example
import simplejson as json

x='{"organisation":"vit", "city":"mumbai","country":"India"}'
y={"year":1999}

z=json.loads(x)
z.update(y)

print(json.dumps(z))
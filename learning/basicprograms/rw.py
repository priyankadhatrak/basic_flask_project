import simplejson as json
import os

newfile=open("newfile.txt","w+")
dicti={"name":"priyanka",
       "age":22}
print(type(dicti))#will print the type of dicti
result=json.dumps(dicti)#it will convert the dictionary into string

print(type(result))# it will print the type of dictionary after converting

newfile.write(result) # it will write the data into the given file.

newfile=open("newfile.txt","r")
print(newfile.read())

#newfile=open("example.py","x")
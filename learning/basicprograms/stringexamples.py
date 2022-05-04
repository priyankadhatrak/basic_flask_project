#string in a varable
a=" hello, priyanka"
b='sanjay dhatrak'
print(a,b)

#slicing string
print(a[2:9])
#slicing from the start
print(a[:9])

#slice to the end
print(a[2:])

#Negative Indexing
print(a[-1])

#modify string 
    #upper- all capital
print(a.upper())
    #lower-all small
print(a.lower())
    #strip-removes whitespace at start
print(a.strip())
    #replace
print(a.replace("h","j"))
    #split-splits with a separator given in parameters
print(a.split(","))
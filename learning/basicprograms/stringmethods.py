a=" hello, priyanka"
b='sanjay dhatrak'
#STRING METHODS
#concat
print(a+" "+b)
#format- edits were we put {} 
age=44
name="john"
txt="my name is {} and my age is {}"
print(txt.format(name,age))
time=10
txt1="hello {0} good morning its {1}'O clock"
print(txt1.format(name,time))

#escape character-"\"
#str="We are the so-called "Vikings" from the north." #gives error
s="We are the so-called \"Vikings\" from the north."
print(s)
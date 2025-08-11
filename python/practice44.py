class Demo:
    a = 4

o = Demo()
#print the class attribute because instance attribute is not present
print(o.a)
#Instance attribute is set
o.a = 0
#print the instance attribute because instance attribute is present
print(o.a)
print(Demo.a) #print the class attribute
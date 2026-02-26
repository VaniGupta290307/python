#types of operators __>7
#arithmetic operator
#assignment operator
#comparison
#logical
#biwise
#membership
#identity

a=10
b=20
print(a+b)
print(a==b)
print(a>=b)
print(a<=b)
print(a!=b)
print(a>b)
print(a<b)
a="Upes"
print("U" in a)
print("Z" not in a)
a=10
b=5
print(a&b)
print(a | b)
print(a^b) #x(o)r operator (o)-->0 same bits-->0 different bits-->1
print(~a) #output-3 #beacuse starting bit is 1 so negative number 11
print(a>>2) #right shift operator 
print(a<<2) #left shift operator
x=5
print(x>6 and x<10)
print(x>6 or x<10)
print(not(x>3 and x<10))

a=[1,2,3]
b=[1,2,3]
c=a
print(a is c)
print(a is b)

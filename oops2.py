#del keyword
class Student:
    def __init__(self,name):
        self.name=name
s1=Student("Vani")
del s1
#print(s1) give error as s1 not exist now
class Student:
    def __init__(self,name):
        self.name=name
s1=Student("Vani")
print(s1.name)
del s1.name
# print(s1.name) givess error

#private attributes and methods
class Account:
    def __init__(self,acc_no,passwd):
        self.acc_no=acc_no
        self.__passwd=passwd
    def reset(self):
        print(self.__passwd)
p1=Account("XYZ",123)
print(p1.acc_no)
# print(p1.passwd)
p1.reset()
print(p1.reset())

class Person:
    name="Vani"
    def __hello(self):
        print("hello")
# p1=Person.hello() gives error because it i private
p1=Person
print(p1.name)

class Person:
    __name="anonymous"
    def __hello(self): #__hello is private here in this class but not privae in other class 
        print("hello person")
    def welcome(self):
        self.__hello() # __hello function is not private here
p1=Person()
print(p1.welcome())
# private like attribute 
# private attributes and methodsare meant to be used only within the class  and not accessible from outside the clas


               

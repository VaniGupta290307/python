class car:
    colour="blue"
    brand="mercedes"
c1=car()
print(c1)
print(c1.colour)
print(c1.brand)

#init--> constructor
#all classes have a function called __init__ ,which is always exexuted when the class is innitiated
#self  parameter is a reference to the first object / or first instance of the class  and is used to acess variables that belongs to the class

class Student:
    def __init__(self): #default constructor
        pass
    def __init__(self,fullname,marks):  #parametrised conductor
        self.name=fullname #give name variable known as attributes
        self.marks=marks
        print(self.name)
        print("Adding new student in database")
        print(self) 
s1=Student("karan",100)
print(s1.name)
print(s1.marks)

s2=Student("arjun",99)
print(s2.name)
print(s2.marks)

#class and instance attributes
#class attributes that is common for all objects
#instance/object atributes for specific obbject
class Student:
    college="UPES"
    name="ABC"
    def __init__(self):
        pass
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("welcome students",self.name)
    def get_marks(self):
        return self.marks
s1=Student("Vani",100)
s2=Student("Aditi",98)
print(s1.name) #high preference to instance attribute
print(s1.marks)
print(s1.college)
print(s2.name)
print(s2.marks)
print(s2.college)
print(Student.college)
print(Student.name)

#methods are functions that belong to objects
s1.welcome()
print(s1.get_marks())

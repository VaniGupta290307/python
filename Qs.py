#Create student class that takes name and marks of 3 subjects as argument in constructor, then create a method to print the average 
class Student:
    def __init__(self,name,marks):
               self.name=name
               self.marks=marks
    def average(self):
         sum=0
         for values in self.marks:
              sum=sum+values
         print("average marks is ",sum/3)
s1=Student("Vani",[100,100,100])
s2=Student("Amrit",[100,100,99])
s1.average()
s2.average()

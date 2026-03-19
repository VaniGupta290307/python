#inheritance
class Car:
    colour="black"
    def start(self):
        print("Car started")
    def stop(self):
        print("car stopped")
class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name
car1=ToyotaCar("Innova")
print(car1.name)
print(car1.start())
print(car1.colour)

#Type of inheritance
#single inheritance single parent class and single child class
# multi level inheritance
class Car:
    def start(self):
        print("car started")
    def stop(self):
        print("car stopped")
class Toyota(Car):
    def __init__(self,brand):
        self.brand=brand
class Innova(Toyota):
    def __init__(self,type):
        self.type=type
car1=Innova("electric")
print(car1.type)
car1=Toyota("BMW")
print(car1.brand)
# print(car1.type) this will give error as we have not call function here
print(car1.start())

#Multiple inheritance
class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"
class C(A,B):
    varC="welcome to class C"
c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

#super constructor
class Car:
    def __init__(self,type):
        self.type=type
    def start(self):
        print("car started")
    def stop(self):
        print("car stopped")
class Toyota(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()
car1=Toyota("Innova","Electrical")
print(car1.type)
print(car1.name)
print(car1.start())

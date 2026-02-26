#usinf keyword argument by * --> rightward can use keyword argument
def func1(name,*,age):
    print("My name is",name,"and my age is",age)
func1("vani",age=18)

# to specify positional only argument add, \ after the parameter
def func7(name,/):
    print(name)
func7("Vani")
# func7(name="Vani") gives error because name is positional only argument

def func1(name,/,age):
    print("My name is",name,"and my age is",age)
func1("vani",age=18)

#for positional and keyword argument it would be seperated by comma

#args -->passing many arguments in single variable-->tuple
def func1(*name):
    print("My name is",name)
    for i in name:
        print(i)
func1("vani","rahul","neha")

#kwargs
def func1(**name):
    print("my name is ",name["first_name"],"and last name is ",name["last_name"])
    print(type(name))
func1(first_name="vani",last_name="sharma")

#combining args,kwargs,normal parameter
def func1(name,*like,**subject_marks):
    print("my name is ",name,"my subject marks are",subject_marks["maths"],subject_marks["english"],"and i like",like)
    print(subject_marks)
func1("vani","chocolate","vanilla",maths=90,english=95)

#important -->unpacking
def func1(a,b,c):
    return a+b+c
list1=[2,4,6]
sum=func1(*list1)
print(sum)

def func1(name,age):
    print("My name is",name,"and my age is",age)
student={
    "name":"vani",
    "age":18
}
func1(**student)

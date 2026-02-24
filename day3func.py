#Functions : block of code that runs until it reaches the return statement, after return it stop executing and send the result back
def func1():
    return "this is my favourite topic in pyhton"
message=func1()
print(message)

#If the function does not have a return statement, it return NULL by default
#Function defination cannot be empty,to create a function without any code use pass statement
def func1():
    pass
func1()

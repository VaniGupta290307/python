# Function Arguement-->actual value sent to the function when called
#Function parameters--> variable linked inside paranthesis in functioon defination
def my_function(name="friend"):  #can pass value in parameters also
    print("Hello",name)
my_function()
my_function("vani")

#keyword argument: send argument with key value pair
def func1(animal,name):              #can pass variables in argument
    print("My",animal,"name is",name)
func1(name="tommy",animal="dog")

#positional argument: argument pass according to argument
ef func1(name,age):
    print("My name is",name,"and my age is",age)
func1("vani",18)

#mixing position and keyword arguments
def func2(animal,name,age):
    print("I have a ",age,"year old",animal,"named",name)
func2("dog",age=5,name="Bruno")

#passing list,tuple in function
def func3(fruits):
    for x in fruits:
        print(x)
my_fruits=["apple","banana","cherry"]
func3(my_fruits)


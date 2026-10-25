#Multiple Return Values
#Python allows a function to return multiple values.
def calculate(a,b):
    addition=a+b
    multiplication=a*b
    subtraction=a-b
    return addition,multiplication,subtraction
result=calculate(12,2)
print(result)
#unpack
a,b,c=calculate(12,2)
print(a)
print(b)
print(c)
#default arguments
def greet(name="Guest"):
    print("Hello", name)
greet()
greet('Virat')

#Positional Arguments/Keyword arguments
#Arguments are matched based on their position
#We can explicitly specify the parameter name.
def display(name, age):
    print("Name:", name)
    print("Age:", age)


display("Santhosh", 42)
display(age=42, name="Santhosh")
def student(name, age, course):
    print(name)
    print(age)
    print(course)


student("Santhosh", age=42, course="Python")
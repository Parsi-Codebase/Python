#Keyword-Only Arguments

#Python also supports keyword-only parameters.
def create_user(name, *, age, city):
    print(name)
    print(age)
    print(city)
def create_user(name, *, age, city):
    print(name)
    print(age)
    print(city)
create_user(
    "Santhosh",
    age=42,
    city="Hyderabad"
)
#create_user("Santhosh", 42, "Hyderabad") # incorrect

'''Positional-Only Arguments
Python also supports positional-only parameters using /.'''
def calculate(a, b, /):
    return a + b
calculate(10, 20) 
calculate(a=10, b=20) # incorrect
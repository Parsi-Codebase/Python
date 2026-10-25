# Arbitrary Keyword Arguments, **args or
#Variable-Length Keyword Arguments — **kwargs
# If the number of keyword arguments is unknown, 
# add a double ** before the parameter name
def my_function(**player):
    print('His last name is: '+player['lname'])
my_function(fname='Sachin',lname='Tendulkar')

def display_student(**details):
    print(details)
display_student(
    name="Santhosh",
    age=42,
    course="Python"
)

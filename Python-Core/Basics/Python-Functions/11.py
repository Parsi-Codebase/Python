'''
Function Scope
Variables created inside a function are normally local variables.
'''
def calculate():
    x = 100
calculate()

#print(x) #error

#A variable defined outside a function has global scope.
company = "ABC Technologies"

def display():
    global company # use global keyword to modify the value inside the function
    print(company)
    company="BBC Technologies"

display()
print(company)
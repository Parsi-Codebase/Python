# global variables
x = 'awesome'


def fun():
    print(x)


fun()
x = "awesome"


def myfunc():
    x = "fantastic"  # local variable
    print("Python is " + x)


myfunc()

print("Python is " + x)


def myfunc1():
    global x  # x is having global scope
    x = "fantastic"


myfunc1()

print("Python is " + x)

x = "awesome"

def myfunc2():
  global x
  x = "fantastic"

myfunc2()

print("Python is " + x)
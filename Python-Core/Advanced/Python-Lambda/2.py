def myfunc(n):
    return lambda a:n*a
mydoubler=myfunc(2)
print(mydoubler(10))
print(mydoubler(100))
mytrippler=myfunc(3)
print(mytrippler(11))
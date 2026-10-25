#Tuple Methods
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
print(numbers.index(30))

#Tuple Unpacking
student = ("Ravi", 25, "Python")

name, age, course = student

print(name)
print(age)
print(course)

employee = ("John", 101, "Developer")

name, employee_id, role = employee

print("Name:", name)
print("ID:", employee_id)
print("Role:", role)
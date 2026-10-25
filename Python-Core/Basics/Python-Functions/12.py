# lambda functions
# A lambda is a small anonymous function
square=lambda x:x*x
result=square(5)
print(result)
add=lambda a,b:a+b
print(add(2,3))

students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 60},
    {"name": "C", "marks": 90}
]

students.sort(key=lambda student: student["marks"])

print(students)
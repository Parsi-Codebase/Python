# dictionary methods
student = {
    "id": 101,
    "name": "Ravi",
    "course": "Python"
}

print(student.keys())
print(student.values())
print(student.items())
for key, value in student.items():
    print(key, ":", value)
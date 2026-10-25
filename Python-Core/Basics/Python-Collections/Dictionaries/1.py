student = {
    "id": 101,
    "name": "Ravi",
    "course": "Python"
}
print(student)
print(student["name"])
print(student["course"])
print(student.get("age"))
print(student.get("age", 0)) # return 0 if key is invalid
# adding a new key
student["duration"] = 30
print(student)
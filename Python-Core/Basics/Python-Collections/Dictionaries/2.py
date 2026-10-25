student = {
    "id": 101,
    "name": "Ravi",
    "age": 25
}
#updating value 
student["age"] = 26

print(student)
#Removing key
student.pop("age")
print(student)
student.popitem() # remove the last indexed key-value pair
print(student)
del student["name"]
# clear all key-value pairs
student.clear()
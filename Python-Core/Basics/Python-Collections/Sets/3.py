'''
Set Operations

Sets are especially useful for mathematical set operations.
union
'''
python_students = {"Ravi", "Raj", "Anil", "Priya"}

java_students = {"Raj", "Priya", "John", "Kiran"}
#union
result = python_students | java_students
print(result)
result = python_students.union(java_students)
print(result)
#Intersection
result = python_students & java_students
print(result)
result = python_students.intersection(java_students)
print(result)
#Difference
#Elements present in Python students but not Java students.
result = python_students - java_students
print(result)
#Symmetric Difference
#Elements that exist in either set but not both.
result = python_students ^ java_students
print(result)

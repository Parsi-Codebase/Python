# set demo
python_students = {"Ravi", "Raj", "Anil", "Priya"}

java_students = {"Raj", "Priya", "John", "Kiran"}

print("Python Students:", python_students)
print("Java Students:", java_students)

print("Common Students:",
      python_students.intersection(java_students))

print("All Students:",
      python_students.union(java_students))

print("Only Python:",
      python_students.difference(java_students))
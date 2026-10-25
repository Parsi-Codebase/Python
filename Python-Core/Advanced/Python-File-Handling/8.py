# Write student names into a file
students = ["Alice", "Bob", "Charlie", "David"]

with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

# Read and display names
with open("students.txt", "r") as file:
    for line in file:
        print("Student:", line.strip())

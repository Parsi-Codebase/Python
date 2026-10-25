class Student:
    count = 0  # Class variable to count objects

    def __init__(self, name):
        self.name = name
        Student.count += 1  # increment every time a new student is created

s1 = Student("Alice")
s2 = Student("Bob")
s3 = Student("Charlie")

print("Total Students:", Student.count)

#Class methods can act as alternate constructors — ways to create objects differently.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_string(cls, data_str):
        name, marks = data_str.split("-")
        return cls(name, int(marks))  # creating object from string

# Creating object using normal constructor
s1 = Student("Alice", 85)

# Creating object using class method
s2 = Student.from_string("Bob-90")

print(s1.name, s1.marks)
print(s2.name, s2.marks)

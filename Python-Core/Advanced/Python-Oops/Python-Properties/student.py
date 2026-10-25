class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    @property
    def grade(self):
        return self.__grade   # acts like getter

    @grade.setter
    def grade(self, value):
        if 0 <= value <= 100:
            self.__grade = value
        else:
            print("Invalid grade value!")

stu = Student("Alice", 90)

print(stu.grade)    # instead of stu.get_grade()
stu.grade = 95      # instead of stu.set_grade(95)
print(stu.grade)
stu.grade = 120     # Invalid grade value!

#Normal Getter/Setter Way (Before Properties)
class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade")

stu = Student("Alice", 90)
print(stu.get_grade())   # Access using method
stu.set_grade(95)        # Modify using method

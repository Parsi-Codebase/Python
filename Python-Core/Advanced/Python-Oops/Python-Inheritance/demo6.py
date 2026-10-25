# Hybrid Inheritance
class School:
    def show_school(self):
        print("This is ABC School")

class Student(School):
    def show_student(self):
        print("This is a student")

class Sports:
    def show_sport(self):
        print("Plays Football")

# Hybrid: Player inherits from both Student and Sports
class Player(Student, Sports):
    def show_player(self):
        print("This student is also a player")

p = Player()
p.show_school()   # From School (via Student)
p.show_student()  # From Student
p.show_sport()    # From Sports
p.show_player()   # Own method

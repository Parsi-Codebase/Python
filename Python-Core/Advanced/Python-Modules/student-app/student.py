students = []
def add_student(name, marks):
    student = {
        "name": name,
        "marks": marks
    }
    students.append(student)

def get_students():
    return students
def find_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None
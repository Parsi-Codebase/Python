students = [
    {
        "id": 1,
        "name": "John",
        "age": 21,
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Mary",
        "age": 22,
        "course": "FastAPI"
    }
]


def get_all_students():
    return students


def get_student_by_id(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    return None


def create_student(student):

    new_id = max(
        [s["id"] for s in students],
        default=0
    ) + 1

    new_student = {
        "id": new_id,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }

    students.append(new_student)

    return new_student


def delete_student(student_id: int):

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            return True

    return False
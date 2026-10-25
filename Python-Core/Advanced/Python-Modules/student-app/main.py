from student import add_student, get_students, find_student
from validation import validate_name, validate_marks
from calculator import calculate_grade


def add_student_menu():

    name = input("Enter student name: ")

    if not validate_name(name):
        print("Invalid name")
        return

    marks = float(input("Enter marks: "))

    if not validate_marks(marks):
        print("Invalid marks")
        return

    add_student(name, marks)

    print("Student added successfully")


def display_students():

    students = get_students()

    if not students:
        print("No students found")
        return

    for student in students:

        grade = calculate_grade(student["marks"])

        print(
            f"Name: {student['name']}, "
            f"Marks: {student['marks']}, "
            f"Grade: {grade}"
        )


def search_student():

    name = input("Enter student name: ")

    student = find_student(name)

    if student is None:
        print("Student not found")
    else:

        grade = calculate_grade(student["marks"])

        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Grade:", grade)


def main():

    while True:

        print("\n===== Student Management =====")

        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student_menu()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("Application terminated")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
class InvalidAgeError(Exception):
    pass


class InvalidMarksError(Exception):
    pass


def register_student():

    try:
        print("===== Student Registration =====")

        name = input("Enter student name: ")

        if not name.strip():
            raise ValueError("Student name cannot be empty")

        age = int(input("Enter age: "))

        if age < 18:
            raise InvalidAgeError(
                "Student must be at least 18 years old"
            )

        marks = float(input("Enter marks: "))

        if marks < 0 or marks > 100:
            raise InvalidMarksError(
                "Marks must be between 0 and 100"
            )

    except ValueError as ex:

        print("Input Error:", ex)

    except InvalidAgeError as ex:

        print("Age Error:", ex)

    except InvalidMarksError as ex:

        print("Marks Error:", ex)

    except Exception as ex:

        print("Unexpected Error:", ex)

    else:

        print("\nStudent registered successfully!")
        print("Name  :", name)
        print("Age   :", age)
        print("Marks :", marks)

    finally:

        print("\nRegistration process completed.")


register_student()
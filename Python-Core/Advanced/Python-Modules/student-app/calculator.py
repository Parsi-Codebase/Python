def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)
def calculate_grade(marks):

    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    return "F"
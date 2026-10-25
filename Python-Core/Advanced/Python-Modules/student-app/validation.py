def validate_name(name):
    if not name.strip():
        return False
    return True
def validate_marks(marks):
    return 0 <= marks <= 100
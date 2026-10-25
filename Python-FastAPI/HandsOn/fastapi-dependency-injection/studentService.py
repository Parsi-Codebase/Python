class StudentService:
    def __init__(self,repository):
        self.repository=repository
    def get_students(self):
        return self.repository.get_all()
    def get_student(self,student_id:int):
        return self.repository.get_by_id(student_id)
        
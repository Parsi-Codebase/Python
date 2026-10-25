class StudentRepository:
    def __init__(self):
        self.students=[
            {'id':1,'name':'sara','course':'python'},
            {'id':2,'name':'meena','course':'dotnet'},
            {'id':3,'name':'kiran','course':'python'},
        ]
    def get_all(self):
        return self.students
    def get_by_id(self,student_id:int):
        for student in self.students:
            if student['id']==student_id:
                return student
            return None
    
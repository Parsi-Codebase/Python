#You can access and modify class variables using a class method.
class Employee:
    company_name = "TechCorp"

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

e1 = Employee()
e2 = Employee()

print(Employee.company_name)  # TechCorp
Employee.change_company("NextGenSoft")
print(e1.company_name)        # NextGenSoft
print(e2.company_name)        # NextGenSoft

#🧠 cls refers to the class itself — just like self refers to the object.
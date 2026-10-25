class Employee:
    company_name = "TechCorp"   # class variable

    def __init__(self, name, salary):
        self.name = name        # instance variable
        self.salary = salary

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name   # modify class variable

# Create two employees
e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

print(Employee.company_name)  # TechCorp

# Change company name using class method
Employee.change_company("NextGenSoft")

print(e1.company_name)  # NextGenSoft
print(e2.company_name)  # NextGenSoft

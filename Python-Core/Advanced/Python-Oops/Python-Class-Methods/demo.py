# Demo on Instance, Class, and Static Methods
class Demo:
    company = "PythonSoft"

    def __init__(self, name):
        self.name = name

    def show(self):  # Instance method
        print(f"Employee: {self.name}, Company: {self.company}")

    @classmethod
    def change_company(cls, new_name):  # Class method
        cls.company = new_name

    @staticmethod
    def info():  # Static method
        # not accessable instance and class variables
        print("This is a PythonSoft Employee class")

# Using all three
d1 = Demo("John")
d1.show()

Demo.change_company("NextGenSoft")
d1.show()

Demo.info()

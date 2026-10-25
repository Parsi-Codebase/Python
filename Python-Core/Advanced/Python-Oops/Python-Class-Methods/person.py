class Person:
    def __init__(self, name, age):
     self.name = name
     self.age = age
    def greet(self):
     print("Hello, my name is " + self.name)
    def get_info(self): # method that accesses object properties:
     return f"{self.name} is {self.age} years old"
    def celebrate_birthday(self): #method that changes a property value:
        self.age += 1
        print(f"Happy birthday! You are now {self.age}")
p1 = Person("Tobias", 28)
p1.greet()
print(p1.get_info())
p1.celebrate_birthday()
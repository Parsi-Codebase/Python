#Using super() to call parent methods
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # Call parent constructor
        self.breed = breed

    def display(self):
        print(f"{self.name} is a {self.breed}")

dog = Dog("Buddy", "Golden Retriever")
dog.display()

# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound")

# Child Class inherits from Animal
class Dog(Animal):
    def speak(self):  # Overriding parent method
        print(f"{self.name} says Woof!")

# Create object of child class
dog = Dog("Buddy")
dog.speak()   # Output: Buddy says Woof!

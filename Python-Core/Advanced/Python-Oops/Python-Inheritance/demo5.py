#Hierarchical Inheritance
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Create objects
d = Dog()
c = Cat()

d.speak()
c.speak()

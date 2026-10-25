class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"
dog=Dog()
cat=Cat()
print(dog.sound())
print(cat.sound())
# Polymorphism in action
for animal in (Dog(), Cat()):
    print(animal.sound())
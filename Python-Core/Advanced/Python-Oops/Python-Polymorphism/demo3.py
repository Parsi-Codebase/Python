#Polymorphism with Inheritance (Method Overriding)
class Bird:
    def fly(self):
        return "Most birds can fly"

class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly"

bird = Bird()
penguin = Penguin()

print(bird.fly())      # Output: Most birds can fly
print(penguin.fly())   # Output: Penguins cannot fly
#The same method fly() has different behaviors depending on the class.
#Polymorphism with Functions and Objects
class Duck:
    def swim(self):
        print("Duck swims in the pond")

class Fish:
    def swim(self):
        print("Fish swims in the sea")

def make_it_swim(animal):
    animal.swim()  # No matter what 'animal' is, as long as it has 'swim'

duck = Duck()
fish = Fish()

make_it_swim(duck)
make_it_swim(fish)

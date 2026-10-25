class Father:
    def skills(self):
        print("Father: Gardening, Programming")

class Mother:
    def skills(self):
        print("Mother: Cooking, Painting")

class Child(Father, Mother):
    def skills(self):
        super().skills()
        print("Child: Dancing, Singing")

obj = Child()
obj.skills()
#uses Method Resolution Order - MRO

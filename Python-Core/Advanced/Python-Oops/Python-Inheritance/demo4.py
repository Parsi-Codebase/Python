# Multilevel Inheritance
class Grandfather:
    def show(self):
        print("Grandfather: Family Head")

class Father(Grandfather):   # inherits Grandfather
    def show(self):
        super().show()
        print("Father: Next Generation")

class Son(Father):   # inherits Father
    def show(self):
        super().show()
        print("Son: Youngest Generation")

obj = Son()
obj.show()
'''
Grandfather: Family Head
Father: Next Generation
Son: Youngest Generation
''' 

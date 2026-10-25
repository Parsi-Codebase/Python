#Read-Only Property
# If you only define a getter (no setter),
# the property becomes read-only.
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def area(self):
        return 3.14 * (self.__radius ** 2)

circle = Circle(5)
print(circle.area)   # 78.5
circle.area = 100    # ❌ Error: can't set attribute

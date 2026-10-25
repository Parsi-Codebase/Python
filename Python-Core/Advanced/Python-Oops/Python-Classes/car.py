class Car:
    wheels = 4  # Class variable (shared)

    def __init__(self, brand, color):
        self.brand = brand  # Instance variable
        self.color = color  # Instance variable

# Create two car objects
car1 = Car("Toyota", "Red")
car2 = Car("Tesla", "Black")

print("Car1:", car1.brand, car1.color, "Wheels:", car1.wheels)
print("Car2:", car2.brand, car2.color, "Wheels:", car2.wheels)
car1.wheels = 6        # modifies only car1's copy
Car.wheels = 5         # modifies class variable for all objects

print(car1.wheels)     # 6 (instance-specific)
print(car2.wheels)     # 5 (from class)
print(Car.wheels)      # 5

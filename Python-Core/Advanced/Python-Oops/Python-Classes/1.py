class Car:
    # constructor: to initialize the object
    def __init__(self,brand,model,year):
        self.brand=brand #attribute
        self.model=model #attribute
        self.year=year   #attribute
    #method: to define the behavior
    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine started!!")
    def display_info(self):
        print(f"Car: {self.brand},Model: {self.model},Year: {self.year}")
# Creating objects
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Tesla", "Model S", 2023)

# Accessing attributes
print(car1.brand)  # Toyota
print(car2.model)  # Model S

# Calling methods
car1.start_engine()
car2.display_info()


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()  # Create inner class object

    def show(self):
        print(f"Car: {self.brand}, Model: {self.model}")
        self.engine.show_engine()  # calling inner class method

    class Engine:
        def __init__(self):
            self.horsepower = 200

        def show_engine(self):
            print(f"Engine Power: {self.horsepower} HP")
car1 = Car("Tesla", "Model S")
car1.show()
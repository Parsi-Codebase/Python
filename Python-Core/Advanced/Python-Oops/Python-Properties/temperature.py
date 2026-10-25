class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            print("Error: Temperature below absolute zero!")
        else:
            self.__celsius = value

    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32

temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0
temp.celsius = -300     # Error: Temperature below absolute zero!

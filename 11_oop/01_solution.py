# Basic Class and Object: Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def getInfo(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)

my_car = Car('Tata', 'NexonEv')
# my_car.getInfo()


# Inheritance: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        # super().brand = brand
        # super().model = model
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def getElectricInfo(self):
        print(f"{self.brand}\n{self.model}\n{self.battery_size}")

my_electric_car = ElectricCar('tesla', 'model s', '65kwh')
my_electric_car.getElectricInfo()
my_electric_car.getInfo()
print('Brand:', my_electric_car.brand)
print('Model:', my_electric_car.model)
print('battery_size:', my_electric_car.battery_size)
# Encapsulation: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand        # __brand makes brand attribute private
        self.model = model
    
    def getInfo(self):
        print(f"Brand: {self.__brand} Model: {self.model}")
    
    def get_brand(self):        # getter method for private attributes
        return self.__brand


my_car = Car('Mahindra', 'XUV 700')
my_car.getInfo()
my_car_brand = my_car.get_brand()
print(f"Brand: {my_car_brand}")
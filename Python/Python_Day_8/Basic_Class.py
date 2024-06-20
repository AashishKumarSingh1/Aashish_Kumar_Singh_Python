#Blueprint 

class car:

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def print_car_attributes(self):
        print(self.brand+" " +self.model)
        return None
    
class Electric_car(car):

    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize=batterySize
        

my_car=car("CarBrand","CarModel") # my_car is an instance of class car!
print(my_car.brand)
print(my_car.model)
print(my_car.print_car_attributes())

my_new_car=Electric_car("newCar","newModel","newBatterySize")
print(my_new_car.batterySize,my_new_car.brand,my_new_car.model)
print(my_new_car.print_car_attributes())

    
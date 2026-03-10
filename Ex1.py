class Car:
    def move(self):
        return "Driving on the road."
    
class Airplane:
    def move(self):
        return "Flying through the sky."
    
def start_journey(vehicle):
    print(vehicle.move())

car = Car()
plane = Airplane()

start_journey(car)
start_journey(plane)
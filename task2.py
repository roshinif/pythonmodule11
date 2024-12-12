class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance
        return self.travelled_distance

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, capacity, current_speed=0, travelled_distance=0):
        super().__init__(registration_number, maximum_speed)
        self.current_speed = 50
        self.capacity = capacity

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, volume, current_speed=0, travelled_distance=0):
        super().__init__(registration_number, maximum_speed)
        self.current_speed = 60
        self.volume = volume


car1 = ElectricCar('ABC-15', '180km/h', 52.5)
car2 = GasolineCar('ACD-123', '165km/h', 32.3)

car1.drive(3)
car2.drive(3)
print(f"{car1.travelled_distance}km")
print(f"{car2.travelled_distance}km")

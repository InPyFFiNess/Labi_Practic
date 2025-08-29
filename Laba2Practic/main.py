class Vihicle:
    brand = None
    model = None
    year = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"Brand of Car: {self.brand}")
        print(f"Model of Car: {self.model}")
        print(f"Year: {self.year}")

    
class Car(Vihicle):
    fuel_type = None
    max_speed = 0
    engine_capacity = 0
    rotation_speed = 0

    def __init__(self, brand, model, year, fuel_type, max_speed, engine_capacity, rotation_speed):
        super(Car, self).__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.max_speed = max_speed
        self.engine_capacity = engine_capacity
        self.rotation_speed = rotation_speed

    def info(self):
        print(f"Brand of Car: {self.brand}")
        print(f"Model of Car: {self.model}")
        print(f"Year: {self.year}")
        print(f"Fuel type = {self.fuel_type}")
        print(f"Max speed = {self.max_speed}")
        print(f"Engine capacity = {self.engine_capacity}")
        print(f"Rotation speed = {self.rotation_speed}")

    def engine_power_calc(self):
        power = self.engine_capacity * self.rotation_speed / 7025
        return power
    
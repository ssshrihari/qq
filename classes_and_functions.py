class Vehicle:
    def __init__(self, number_of_tyres, engine_type, body_type,transmission):
        self.number_of_tyres = number_of_tyres
        self.engine_type = engine_type
        self.body_type = body_type
        self.transmission=transmission

    def engine_start(self):
        print(f"{self.engine_type}Engine start")

    def engine_stop(self):
        print(f"{self.engine_type}Engine stopped")
        

    def drive(self):
        print(f"Vehicle is running in {self.transmission} transmission")


class Car(Vehicle):
    def __init__(self, air_condition, air_bags, name):
        super().__init__(4, "4 cylinder", "aluminium", "6 transmission")
        self.name = name
        self.air_condition = air_condition


class Truck(Vehicle):
    def __init__(self,air_condition, air_bags):
        super().__init__(8, "12 cylinder", "Bronze", "7 transmission")
        self.air_condition = air_condition


class Bike(Vehicle):
    def __init__(self, stand_type):
        super().__init__(2, "2 cylinder", "gold", "5 transmission")
        self.stand_type = stand_type


if __name__ == '__main__':
    car1 = Car(True, 4)


class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
class CarBody:
    def __init__(self, body_type, number_doors):
        self.body_type = body_type
        self.number_doors = number_doors
class Wheel:
    def __init__(self, diameter, type_rubber):
        self.diameter = diameter
        self.type_rubber = type_rubber
class Car:
    def __init__(self, horsepower, fuel_type, body_type, number_doors, diameter, type_rubber):
        self.engine = Engine(horsepower, fuel_type)
        self.car_body = CarBody(body_type, number_doors)
        self.wheel = Wheel(diameter, type_rubber)
    def display_engine_info(self):
        print(f"Максимальная мощность (в лошадиных силах): {self.engine.horsepower} л.с.\n"
              f"Тип топлива: {self.engine.fuel_type}")
    def display_car_body_info(self):
        print(f"Тип кузова: {self.car_body.body_type}\n"
              f"Количество дверей: {self.car_body.number_doors}")
    def display_wheel_info(self):
        print(f"Диаметр колес: {self.wheel.diameter} дюймов\n"
              f"Тип резины: {self.wheel.type_rubber}")

print("Автомобиль №1:")
car = Car(200, "Petrol", "Sedan", 5, 16, "Winter")
car.display_engine_info()
car.display_car_body_info()
car.display_wheel_info()
print("\nАвтомобиль №2:")
car2 = Car(155, "Diesel fuel", "Hatchback", 3, 18, "Summer")
car2.display_engine_info()
car2.display_car_body_info()
car2.display_wheel_info()
print("\nАвтомобиль №3:")
car3 = Car(350, "Electricity", "Off-road vehicle", 5, 21, "Summer")
car3.display_engine_info()
car3.display_car_body_info()
car3.display_wheel_info()
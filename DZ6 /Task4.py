# Task4 Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
from random import randint

class Car():
    def __init__(self, speed, color, name, is_police = True):
        self.speed = speed * randint(0,20)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Car {self.name} is moving"

    def stop(self):
        if self.speed == 0:
            print(f"Car {self.name}  is not moving")
        else:
            print('Velocity != 0')

    def turn(self, direction):
        print(f"Car goes to the {direction}")

    def show_speed(self):
        print(f"Current velocity = {self.speed}")

class TownCar(Car):
    # унаследованные атрибуты
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Current velocity of the town-car = {self.speed}")
        if self.speed > 60:
            print(f"{self.speed} - Overspeed!")

class WorkCar(Car):
    # унаследованные атрибуты
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Current velocity of the work-car = {self.speed}")
        if self.speed > 40:
            print(f"{self.speed} - Overspeed!")

class SportCar(Car):
    # все как в родительском классе
    pass

class PoliceCar(Car):
    # унаследованные атрибуты
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if bool(self.is_police) == True:
            print(f"It is a police car {self.name}")
        else:
            print(f"It is not a police car {self.name}")


towncar = TownCar(5,'red','KIA', False)
workcar = WorkCar(7,'green','BMW', False)
sportcar = SportCar(20,'blue','Porsche', False)
policecar = PoliceCar(5,'white','Volvo', True)
##
print(towncar.show_speed())
print(towncar.go())
print(towncar.stop())
print(towncar.turn('left'))
##
print(workcar.show_speed())
print(workcar.go())
print(workcar.stop())
print(workcar.turn('left'))
##
print(sportcar.show_speed())
print(sportcar.go())
print(sportcar.stop())
print(sportcar.turn('right'))
##
print(policecar.show_speed())
print(policecar.go())
print(policecar.stop())
print(policecar.turn('left'))
print(policecar.police())

"""
Реализуйте базовый класс Car.

у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы:
go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print('Vehicle starts.')

    def stop(self):
        print('Vehicle stops.')

    def turn(self, direction):
        print(f"Vehicle turns {direction}")

    def show_speed(self):
        print(f'Speed is {self.speed} km/hour')


class TownCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        speed_limit = 60
        if self.speed <= speed_limit:
            print(f'Speed is {self.speed} km/hour')
        else:
            print(f'Speed is {self.speed} km/hour. Speed limit is {speed_limit} km/hour.')


class SportCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        speed_limit = 40
        if self.speed <= speed_limit:
            print(f'Speed is {self.speed} km/hour')
        else:
            print(f'Speed is {self.speed}. Speed limit is {speed_limit} km/hour.')


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


town = TownCar('Nissan', 'white', 70)
sport = SportCar('Porsche', 'black', 200)
work = WorkCar('Tesla', 'blue', 60)
police = PoliceCar('Ford', 'white', 90)


def show_speed(self):
    speed_limit = 60
    if self.speed <= speed_limit:
        print(f'Speed is {self.speed} km/hour')
    else:
        print(f'Speed is {self.speed} km/hour. Speed limit is {speed_limit} km/hour.')


def drive(car=town):
    print(f'This is {car.name} in {car.color} color.')
    car.go()
    car.show_speed()
    car.turn('left')
    car.show_speed()
    if car.is_police:
        print(f"{car.name} is a police car")
    else:
        car.stop()


drive(town)
print('\n \n')
drive(sport)
print('\n \n')
drive(work)
print('\n \n')
drive(police)

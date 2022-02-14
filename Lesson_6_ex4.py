class Car:

    is_police = False

    def __init__(self, color="белый", name="noname", speed=0.0):
        self.color = color
        self.name = name
        self.speed = speed

    def go(self):
        print(f"{self.name} начал движение")

    def stop(self):
        print(f"{self.name} остановился")

    def turn(self, direction):
        print(f"{self.name} едет {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.name} {self.speed} км\ч")


class TownCar(Car):
    def show_speed(self):
        print(
            f"Текущая скорость {self.name} {self.speed} км\ч" if self.speed <= 60 else f"Скорость автомобиля {self.name} превышена!")


class WorkCar(Car):
    def show_speed(self):
        print(
            f"Текущая скорость {self.name} {self.speed} км\ч" if self.speed <= 40 else f"Скорость автомобиля {self.name} превышена!")


class PoliceCar(Car):
    is_police = True


police = PoliceCar("черный", "Reno Logan", 70)
police.go()
police.show_speed()
police.turn("вправо")
police.stop()
print()

truck = WorkCar("красный", "MAN", 90)
truck.go()
truck.turn("влево")
truck.show_speed()
truck.stop()
print()

t_car = TownCar("желтый", "BMV X6", 40)
t_car.go()
t_car.turn("прямо")
t_car.show_speed()
t_car.stop()

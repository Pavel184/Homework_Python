# Pavel Krupenya
# Cars
from random import randrange
class Car:
    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = bool(is_police)
    def go(self):
        print(f"{self.name} is moving")
    def stop(self):
        print(f"{self.name} is stopped")
    def turn(self):
        self.direction = randrange(1, 3)
        if self.direction == 1:
            print(f"{self.name} made a left turn")
        else:
            print(f"{self.name} made a right turn")
    def show_speed(self):
        print(f"{self.name} speed is {self.speed}")
    def police(self):
        if self.is_police == True:
            print(f"{self.name} from police department\n")
        else:
            print(f"{self.name} is not from police department\n")


class TownCar(Car):
    def __init__(self, speed, colour, name, is_police):
        super().__init__(speed, colour, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} drive with overspeed!")
        else:
            print(f"{self.name} speed is {self.speed}")

class SportCar(Car):
    def __init__(self, speed, colour, name, is_police):
        super().__init__(speed, colour, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, colour, name, is_police):
        super().__init__(speed, colour, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            print("Overspeed!")
        else:
            print(f"Current speed is {self.speed}")

class PoliceCar(Car):
    def __init__(self, speed, colour, name, is_police):
        super().__init__(speed, colour, name, is_police)

sport_car = SportCar(200, "Red", "Speedy", False)
sport_car.go()
sport_car.turn()
sport_car.show_speed()
sport_car.stop()
sport_car.police()

town_car = TownCar(61, "White", "Sam", False)
town_car.go()
town_car.turn()
town_car.show_speed()
town_car.stop()
town_car.police()

work_car = WorkCar(39, "Blue", "Bob", False)
work_car.go()
work_car.turn()
work_car.show_speed()
work_car.stop()
work_car.police()

police_car = PoliceCar(120, "Red", "Polly", True)
police_car.go()
police_car.turn()
police_car.show_speed()
police_car.stop()
police_car.police()

input("\nPress Enter for exit")
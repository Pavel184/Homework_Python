# Pavel Krupenya
# Road mass
class Road:
    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width
    def calc(self):
        mass = self._lenght * self._width * 25 * 0.05
        print(f"mass of the road is {self._lenght} m * {self._width} m * 25 kg * 0.05 m = {mass} t ")
road = Road(100, 20)
road.calc()
input("\nPress Enter for exit")
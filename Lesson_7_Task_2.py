# Pavel Krupenya
# Textil
from abc import ABC, abstractmethod
class Textil:
    def __init__(self, v, h):
        self.v = v
        self.h = h



    @property
    def get_sq_full(self):
        self.sq_full = (self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)
        return f'{self.sq_full}'



class Coat(Textil):
    def __init__(self, v):
        self.v = v
        self.square_c = v / 6.5 + 0.5

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'


class Jacket(Textil):
    def __init__(self, h):
        self.h = h
        self.square_j = h * 2 + 0.3

    def __str__(self):
        return f'Площадь на костюм {self.square_j}'

coat = Coat(10)
jacket = Jacket(5)
print(coat)
print(jacket)
print(Textil.sq_full)

# Pavel Krupenya
# Complex numbers V2.0
class Compl_num:
    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        # Complex number z = x + y*j, j - imaginary unit

    def __add__(self, other):
        return f"z = {self.x + other.x} + {self.y + other.y} * j"

    def __mul__(self, other):
        return f"z = {self.x * other.x - self.y * other.y} + {self.y * other.x + self.x * other.y} * j"

    def __str__(self):
        return f"z = {self.x} + {self.y} * j"


z_1 = Compl_num(1, 7)
z_2 = Compl_num(2, 1)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
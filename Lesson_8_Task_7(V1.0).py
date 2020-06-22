# Pavel Krupenya
# Complex numbers V1.0
class Compl_num:
    def __init__(self, z):
        self.z = z

    def __add__(self, other):
        return f"z_1 + z_2 = {self.z + other.z}"

    def __mul__(self, other):
        return f"z_1 * z_2 = {self.z * other.z}"

    def __str__(self):
        return f"z = {self.z}"

z_1 = Compl_num(1+7j)
z_2 = Compl_num(2 + 1j)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)

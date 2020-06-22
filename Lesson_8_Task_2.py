# Pavel Krupenya
# Exception(division by zero)
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    a = int(input("This program calculate A / B\nPlease enter 'A': "))
    b = int(input("Please enter 'B': "))
    if b == 0:
        raise OwnError("'B' must be not a zero!")
    c = a / b
except ValueError:
    print("It is not a number(s)!")
except OwnError as err:
    print(err)
else:
    print(f"A / B = {c}")
input("\nPress Enter for exit")
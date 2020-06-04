# Pavel Krupenya
# Sum function
def my_func(x, y):
    try:
        if float(x) <= 0 or int(y) >= 0:
            print("Error, 'x' must be a real number and > 0 and 'y' must be an integer and < 0")
            return
        return float(x) ** int(y)
    except ValueError:
        print("'x' must be a number and 'y' must be an integer")
print(my_func(input("Please enter x(must be a real number > 0): "), input("Please enter y(must be negative integer): ")))
input("\n Press Enter for exit")
# Pavel Krupenya
# Sum function
def my_func(a, b, c):
    try:
        return float(a) + float(b) + float(c) - min(float(a), float(b), float(c))
    except ValueError:
        print("You entered not a number")
print(my_func(input("Please enter a: "), input("Please enter b: "), input("Please enter c: ")))
input("\n Press Enter for exit")
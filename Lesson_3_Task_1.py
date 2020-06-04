# Pavel Krupenya
# Division function
def divFunc(a, b):
    try:
        return round((float(a) / float(b)), 2)
    except ZeroDivisionError:
        print("The divisor must not be zero")
    except ValueError:
        print("You entered not a number(s)")
print(divFunc(input("Please enter dividend: "), input("Please enter divisor: ")))
input("\n Press Enter for exit")
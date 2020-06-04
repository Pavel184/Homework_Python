# Pavel Krupenya
# String sum

summ = 0
while True:
    string = input("Please enter sting of numbers separated by spaces or enter 'q' to exit: ")
    for el in string.split():
        if el == "q":
            break
        try:
            summ += float(el)
        except ValueError:
            print(f"Element number '{el}' is not a number. Result will consist only a sum of the numbers")
            continue
    if el == "q":
        break
    print(summ)
print(summ)
input("\nPress Enter for exit")

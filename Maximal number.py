# Pavel Krupenya
# Max number
num = int(input("Enter a positive integer: "))
num_max1 = 0
while num != 0:
    num_max2 = num % 10
    num //= 10
    if num_max2 == 9:
        num_max1 = num_max2
        break
    elif num_max2 > num_max1:
        num_max1 = num_max2
print("Max number is: ", num_max1)
input("\nPress any button to exit")
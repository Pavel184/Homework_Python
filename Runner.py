# Pavel Krupenya
# Runner
distance = float(input("Please enter the result of first day in km: "))
target = float(input("Please enter the target distance of the day in km: "))
counter = 1
print(distance)
while distance < target:
    distance = distance * 1.1
    counter += 1
print(f"You will reach the target in {counter} day(s)")
input("\nPress any button to exit")
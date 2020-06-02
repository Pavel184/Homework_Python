# Pavel Krupenya
# Calendar
calendar = ["", "winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter"]
monthNum = "some value to define variable"
while True:
    monthNum = input("\nPlease enter month number(from 1 to 12) or press enter to exit: ")
    if monthNum == "":
        break
    elif int(monthNum) > 12 or int(monthNum) < 1:
        continue
    else:
        print(f"Season: {calendar[int(monthNum)]}")

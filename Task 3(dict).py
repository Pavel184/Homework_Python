# Pavel Krupenya
# Calendar
calendar = {1: "winter", 2: "winter", 12: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer", 7: "summer", 8: "summer", 9: "autumn", 10: "autumn", 11: "autumn"}
while True:
    monthNum = input("\nPlease enter month number(from 1 to 12) or press enter to exit: ")
    if monthNum == "":
        break
    elif int(monthNum) > 12 or int(monthNum) < 1:
        continue
    else:
        print(calendar.get(int(monthNum)))




# Pavel Krupenya
# Salary calculation

from sys import argv
script_name, tbh, hour_rate, bonus = argv
try:
    print(f"Working time: {tbh} \nHour rate: {hour_rate} \nBonus amount: {bonus} \nYour salary is: {float(tbh) * float(hour_rate) + float(bonus)}")
except ValueError:
    print("Error. You entered not a number")

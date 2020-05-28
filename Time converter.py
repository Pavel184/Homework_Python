# Pavel Krupenya
# Time converter

seconds_amount = int(input("Please enter amount of seconds: "))
hours = seconds_amount // 3600
minutes = seconds_amount // 60 % 60
seconds = seconds_amount % 60
print(f"{seconds_amount} seconds are equal to: {hours} : {minutes} : {seconds} ")
input("\nPress any button to exit")
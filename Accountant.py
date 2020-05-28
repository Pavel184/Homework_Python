# Pavel Krupenya
# Accountant
income = float(input("Please enter amount of income: "))
expenses = float(input("Please enter amount of expenses: "))
profit = income - expenses
if profit == 0:
    print("Your profit is 0")
elif profit < 0:
    print("Your loss is ", profit)
else:
    profitability = profit / income
    print(f"Your profit is {profit} , profitability is {profitability}")
    manpower = int(input("How many people work in your Company: "))
    pers_prof = profit / manpower
    print("Profit per person is: ", pers_prof)
input("\nPress any button to exit")

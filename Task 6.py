# Pavel Krupenya
# Products data
n = 0
data = []
count = int(input("Please enter how many products you need to enter: "))
while n < count:
    n += 1
    product = (n, {"name": input("Name: "), "price": input("Price: "), "qty": input("Qty: "), "units": input("Units: ")})
    data.append(product)
    print(product)
print(data)
input("\n Press Enter for exit")
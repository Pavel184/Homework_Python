# Pavel Krupenya
# Factorial
import math
def fact(n):
    yield math.factorial(n)
count = 1
n = int(input("Please input 'n' to calculate factorials from 1! to n!: "))
while count <= n:
    for el in fact(count):
        print(f"{count}! = {el}")
    count += 1
input("\nPress Enter for exit")
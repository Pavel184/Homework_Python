# Pavel Krupenya
# count & cycle
from itertools import count, cycle
el = 10
my_list = []
for el in count(1):
    if el > 50:
        break
    else:
        my_list.append(el)
print(my_list)
с = 0
for el in cycle(my_list):
    if с >= 50:
        break
    print(el)
    с += 1
input("\nPress Enter for exit")


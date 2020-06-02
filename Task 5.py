# Pavel Krupenya
# Rating
list = [9, 6, 6, 6, 5, 4, 3, 3, 1]
num = int(input("Please enter a integer: "))
for el in list:
    if num > el:

        list.insert(list.index(el) + list.count(el) - 1, num)
        break
    elif num == 1:
        list.append(num)
        break
print(list)
input("\n Press Enter for exit")
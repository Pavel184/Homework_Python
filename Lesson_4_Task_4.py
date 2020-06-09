# Pavel Krupenya
# Repeat filter
my_list = input("Please enter some numbers separated by space: ").split()
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)
input("\nPress Enter for exit")

# Pavel Krupenya
# List generator
try:
    my_list = input("Please enter some numbers separated by space: ").split()
    new_list = [el for num, el in enumerate(my_list[1:], 1) if float(el) > float(my_list[num - 1])]
    print(new_list)
    input("\n Press Enter for exit")
except ValueError:
    print("Error!")
    input("\nPress Enter for exit")

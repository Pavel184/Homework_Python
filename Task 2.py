# Pavel Krupenya
# List exchange
list_cont = list(input("Please enter content for list or press Enter to see the list content: "))
result_list_1 = list()
result_list_2 = list()
result_list_3 = list()
for el in range(1, len(list_cont) + 1, 2):
    result_list_1.append(el)
for el in range(2, len(list_cont) + 1, 2):
    result_list_2.append(el)
while True:
    result_list_3.append(result_list_2.pop(0))
    result_list_3.append(result_list_1.pop(0))
    if len(result_list_1) == 0:
        break
    if len(result_list_2) == 0:
        result_list_3.append(result_list_1.pop(0))
        break
print(result_list_3)
input("\nPress Enter to exit")
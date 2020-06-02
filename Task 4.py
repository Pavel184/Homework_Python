# Pavel Krupenya
# String
string = input("Please input some words: ")
for ind, el in enumerate(string.split(), 1):
    print(ind, el[0:10])
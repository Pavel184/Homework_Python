# Pavel Krupenya
# Exception
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
list = []
new_list = []
while True:
    try:
        el = input("Please enter a number(s) or 'q' for exit: ")
        if el == "q" or el == "Q":
            break
        elif el.isdigit():
            list.append(int(el))
            print(list)
            continue
        else:
           raise OwnError("You entered not/not only a number(s)")
    except OwnError as err:
        print(err)
print(list)
input("\nPress Enter for exit")
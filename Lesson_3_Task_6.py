# Pavel Krupenya
# String sum
def int_funct():
    while True:
        word = input("\nPlease enter a word in small letters or 'q' to exit: ")
        if word == "q":
            break
        elif word == word.lower():
            print(word.title())
        else:
            print("\nYou entered capital letters, please try again or enter 'q' for exit: ")
    return
print(int_funct())


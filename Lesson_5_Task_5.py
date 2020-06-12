# Pavel Krupenya
# Summation
def summ():
    try:
        with open("my_file.txt", "w+", encoding="utf8") as f_obj:
            line = input("Please enter some numbers separated by spaces: ")
            f_obj.writelines(line)
            my_list = line.split()
            print(sum(map(int, my_list)))
    except IOError:
        print("I/O Error")
    except ValueError:
        print("You entered not a number")
summ()
input("\nPress Enter for exit")

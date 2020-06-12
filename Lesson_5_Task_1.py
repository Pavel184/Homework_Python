# Pavel Krupenya
# Create text file
out_f = open("test_file.txt", "w+")
str_list = []
while True:
    str_list = input("Please enter some words separated by spaces or press Enter to stop: ")
    if str_list == "":
        break
    out_f.writelines(str_list + '\n')
out_f.seek(0)
print(out_f.readlines())
out_f.close()
input("\nPress Enter for exit")
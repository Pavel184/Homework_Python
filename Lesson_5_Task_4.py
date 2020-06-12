# Pavel Krupenya
# Translator
dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new = []
with open("text_4.txt", "r", encoding="utf8") as f_obj:
    for el in f_obj:
        el = el.split(' ', 1)
        new.append(dict[el[0]] + '  ' + el[1])
with open("text_4_new.txt", "r+", encoding="utf8") as f_obj_2:
    f_obj_2.writelines(new)
    print(new)
input("\nPress Enter for exit")
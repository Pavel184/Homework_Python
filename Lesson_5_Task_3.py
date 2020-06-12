# Pavel Krupenya
# Salary
with open('text_3.txt', 'r', encoding="utf8") as f_obj:
    salary = []
    lowSalary = []
    my_list = f_obj.read().split('\n')
    for el in my_list:
        el = el.split()
        if float(el[1]) < 20000:
           lowSalary.append(el[0])
        salary.append(el[1])
print(f'Salary less than 20000 {lowSalary}, Average salary {sum(map(float, salary)) / len(salary)}')
input("\nPress Enter for exit")


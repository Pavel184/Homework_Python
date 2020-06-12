# Pavel Krupenya
# Accounting
import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open("text_7.txt", "r", encoding="utf8") as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f"Average profit - {prof_aver:.2f}")
    else:
        print(f"No profit")
    pr = {'Average profit': round(prof_aver)}
    profit.update(pr)
    print(f'Profit per Company - {profit}')

with open('text_77.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f"Created .json file with following content: \n "
          f" {js_str}")

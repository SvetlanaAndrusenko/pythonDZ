# Task7 Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма
# собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить
# её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}]. Итоговый список сохранить в виде
# json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

spisok = []
dict_profit = {}
dict_loss = {}
#dict_average = {}
aver_profit = {}
comp_profit = 0
quantity_profit = 0

with open("file7.txt","r") as f_obj:
    lines_read = f_obj.readlines()
    for line in lines_read:
        l = line.split()
        company, form, proceeds, costs = l[0], l[1], l[2], l[3]
        profit = float(proceeds) - float(costs)
        if profit > 0:
            dict_profit.update({company: profit})
            print(f"Company {company} has profit {profit}")
            comp_profit += profit
            quantity_profit += 1
        else:
            dict_loss.update({company: profit})
            print(f"Company {company} has loss {profit}")

aver_profit.update({"average_profit": round(comp_profit/quantity_profit, 3)})
spisok = [dict_profit, dict_loss, aver_profit]

with open("spisok_task7.json","w") as json_task7:
    json.dump(spisok, json_task7)




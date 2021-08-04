# Task3 Создать текстовый файл (не программно). Построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад
# менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины
# дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open("file3.txt") as f_obj:
    salary = 0
    stroka = 0
    content = f_obj.read().split('\n')
    for line in content:
        line = line.split()
        #stroka += 1
        if (float(line[1]) <= 20000):
            print(f"{line[0]} has salary {line[1]} which is less than 20000")

        salary += float(line[1])

    #print(f"Average amount of employee's salary:{round(salary/stroka,3)}")
    print(f"Average amount of employee's salary:{round(salary / len(content), 3)}")

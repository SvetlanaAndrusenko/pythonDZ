# Task1 Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо использовать
# формулу: (выработка в часах * ставка в час) + премия. Для выполнения
# расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv
# проверяем длину argv
if len(argv) < 4:
    raise SystemExit(-1)

def sal(a, b, c):
    salary = (float(a) * float(b)) + int(c)
    return f"Employee's salary: {salary}"

script_name, hours, rate, reward = argv[0], argv[1], argv[2], argv[3]

print("The name of script:", script_name)
print("Work in hours:", hours)
print("Rate per hour:", rate)
print("Reward:", reward)

print(sal(hours, rate, reward))


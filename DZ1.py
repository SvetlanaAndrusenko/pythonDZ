#DZ1 Andrusenko Svetlana Leonidovna

# Task1 Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.
"""
a = 5
b = 10.78
c = 'Hello'
d = 800

list_a = [a,b,c]
list_a.append(d)

print(a)
print(b)
print(c)
print(a,b,c)
print(list_a)
print('Hello' in list_a)

zapros1 = input('Write number 1:')
print(float(zapros1))
zapros2 = input('Write number 2:')
print(float(zapros2))
zapros3 = input('Write string 1:')
print(zapros3)
zapros4 = input('Write string 2:')
print(zapros4)
"""
# Task2 Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
time = int(input('Enter the time in seconds:'))
hours = time//3600
minutes = (time % 3600)//60
seconds = time - hours*3600 - minutes*60
print(hours)
print(minutes)
print(seconds)
result = f"{hours}чч:{minutes}мм:{seconds}cc"
print(result)
proverka = hours*3600+minutes*60+seconds
print(proverka)
"""
# Task3 Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
n = float(input('Enter the number n ='))
n1 = n
n2 = n*10 + n
n3 = n*100 + n*10 +n
number = n1 + n2 + n3
print(number)
"""
# Task4 Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
"""
input_num = int(input('Enter the number:'))

i = 0
a = -1
if (type(input_num) == int and input_num > 0):
    while input_num > 10:
        b = input_num % 10
        i += 1
        input_num = input_num//10
        if b > a:
            a = b
    print(a)
else:
    print('Enter a positive integer')
#print(i)
"""
# Task5 Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
vf = float(input('Enter the proceeds:'))
izf = float(input('Enter the costs:'))

if vf > izf:
    print('The company has a profit')
    rent = (vf-izf)/vf
    people = int(input('Number of employees:'))
    profit_person = (vf-izf)/people
    print("%.2f" % rent)
    print("%.2f" % profit_person)
else:
    print('The company has a loss')
"""
# Task6 Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
# на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров
# a и b и выводить одно натуральное число — номер дня.
"""
a = float(input('The result on the first day:'))
b = float(input('The final result:'))
i = 1

while a < b:
    i = i + 1
    a = a + a * 0.1

print(i)
res = f"On the {i}th day he achieved the result - no more than {b} km"
print(res)
"""




# Task7 Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться
# объект-генератор. Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа. В цикле нужно выводить только
# первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например,
# факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from math import factorial
from itertools import count

def fact():
    for el in count(1):
        yield factorial(el)

n = int(input('Enter the number'))
g = fact()

i = 1
for el in g:
    if i > n:
        break
    else:
        print(f"{el}")
        i += 1

print(f"Check the code:{factorial(n)}")
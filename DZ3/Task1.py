# Task1 Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def divide(a,b):
    if b == 0:
        return 'Error'
    else:
        return a/b

c = float(input('Enter 1 number:'))
d = float(input('Enter 2 number:'))

print(divide(c,d))
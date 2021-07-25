# Task3 Реализовать функцию my_func(), которая принимает три
# позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a,b,c):
    if (a + b > a + c and a + b > b + c):
        return a + b
    elif (c + b > a + c and c + b > b + a):
        return c + b
    elif (a + c > b + c and a + c > a + b):
        return a + c
    else:
        return 'Enter different numbers'

print(f'{my_func(float(input("Enter 1 number:")),float(input("Enter 2 number:")),float(input("Enter 3 number:")))}')





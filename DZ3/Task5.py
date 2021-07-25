# Task5 Программа запрашивает у пользователя строку чисел,
# разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def function():
    s_first = 0
    s_total = 0
    zapusk = True
    while zapusk == True:
        line = input('Enter the line of numbers or enter Q for break:')
        numbers = line.split()
        for i in range(len(numbers)):
            if numbers[i] == 'Q':
                zapusk = False
                print('The code is finished')
                break
            else:
                numbers[i] = float(numbers[i])
                s_first = s_first + numbers[i]
        s_total = s_total + s_first
        print(f'At first, the sum:{s_first}, in the end:{s_total}')
#print(function(input('Enter the line of numbers:')))
function()


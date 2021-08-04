# Task5 Создать (программно) текстовый файл, записать в него
# программно набор чисел, разделённых пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить её на экран.
from random import randint

s = 0
with open("file5.txt", "w+") as f_obj:
    #line = input('Enter the line of numbers:')
    #f_obj.write(line)
        for i in range(randint(2, 10)):
            f_obj.write(f"{randint(0, 5)} ")

with open("file5.txt", "r") as f_obj:
    split_line = f_obj.read().split()
    print(f"{split_line}")
    for number in split_line:
         s += int(number)
    print(s)

# Task1 Создать программный файл в текстовом формате, записать
# в него построчно данные, вводимые пользователем. Об окончании ввода
# данных будет свидетельствовать пустая строка.

with open("file1.txt", "w") as f_obj:
    line = input('Enter the line:\n')
    while line:
        f_obj.write(f"{line}\n")
        line = input('Enter another the line:\n')
        if not line:
            break
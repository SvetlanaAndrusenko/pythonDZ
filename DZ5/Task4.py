# Task4 Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict_translate = {'One': 'Один', 'Two': 'Два', 'Three':'Три', 'Four': 'Четыре'}

with open("file4.txt","r") as file4:
    with open("newfile4.txt","w") as newfile4:
        for line in file4:
            line = line.split()
            if line[0] in dict_translate:
                change = dict_translate[line[0]]
                newfile4.writelines(f"{change} {line[1]} {line[2]}\n")



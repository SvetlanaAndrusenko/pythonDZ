# Task2 Создать текстовый файл (не программно), сохранить в нём
# несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open("file2.txt") as f_obj:
    stroka = 0
    content = f_obj.read().split('\n')
    for line in content:
        print(line)
        stroka += 1
        words = len(line.split())
        print(f"line №{stroka} - {words} words")
    print(f"The number of lines in file: {len(content)}")


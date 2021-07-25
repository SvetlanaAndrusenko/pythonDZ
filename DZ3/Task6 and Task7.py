# Task 6 and 7 Реализовать функцию int_func(), принимающую слово
# из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать
# строка из слов, разделенных пробелом. Каждое слово состоит из латинских
# букв в нижнем регистре. Сделать вывод исходной строки, но каждое
# слово должно начинаться с заглавной буквы. Необходимо использовать
# написанную ранее функцию int_func().

"""
def int_func(t):
        return t.title()

print(int_func(input('Enter the line:')))
"""
def int_func(t):
    sentence = t.split()
    text = []
    for i in sentence:
        word = str(i)
        word_up = word[:1].upper()
        word_final = word_up + word[1:]
        text.append(word_final)
    return text

print(int_func(input('Enter the line:')))
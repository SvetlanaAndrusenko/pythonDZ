# Task2 Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

spisok = []
leng = int(input('Enter the length of the list:'))

for i in range(leng):
    a = input('Enter the element of list:')
    spisok.append(a)

print(spisok)

if leng % 2 == 0:
    i = 0
    while i < leng:
        change = spisok[i]
        spisok[i] = spisok[i+1]
        spisok[i+1] = change
        i += 2
else:
    i = 0
    while i < (leng - 1):
        change = spisok[i]
        spisok[i] = spisok[i + 1]
        spisok[i + 1] = change
        i += 2

print(spisok)


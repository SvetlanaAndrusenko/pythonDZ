# Task1 Реализовать класс Matrix (матрица). Обеспечить перегрузку
# конструктора класса (метод __init__()), который должен принимать
# данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода
# матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц). Результатом сложения
# должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый
# элемент первой строки первой матрицы складываем с первым элементом
# первой строки второй матрицы и т.д.

from random import randint

class Matrix():
    def __init__(self, component):
        self.component = component

    def __str__(self):
        m = ""
        for i in range(len(self.component)):
            for j in range(len(self.component[i])):
                m += f" {self.component[i][j]} "
            m += "\n"
        return m

    def __add__(self, other):
        component = [[self.component[i][j] + other.component[i][j]
                      for j in range(len(self.component[i]))]
                     for i in range(len(self.component))]
        return Matrix(component)


m1 = Matrix([[randint(0, 5) for i in range(3)] for j in range(3)])
m2 = Matrix([[randint(0, 5) for k in range(3)] for n in range(3)])
print(m1)
print(m2)
print(m1+m2)


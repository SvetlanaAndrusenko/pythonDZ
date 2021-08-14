# Task3 Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение
# (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления
# должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме
# ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества
# ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между
# \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
# ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
# вернет строку: *****\n*****\n*****.

class Cell():
    def __init__(self, number):
        self.number = number #количество клеток

#методы перегрузки арифметических операторов
    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if (self.number - other.number) > 0:
            return Cell(self.number - other.number)
        else:
            print('The difference is less than 0')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(round(self.number//other.number))

    def make_order(self, num_row): # количество ячеек в ряду = 5 для второй и 12 для первой
        s = ''
        for i in range(self.number//num_row):
            s += '*' * num_row + '\n'
        s += '*' * (self.number % num_row) + '\n'
        return s

cell_1 = Cell(50)
cell_2 = Cell(12)
print((cell_1 + cell_2).number)
print((cell_1 - cell_2).number)
print((cell_1 * cell_2).number)
print((cell_1 / cell_2).number)
print(cell_1.make_order(12))
print(cell_2.make_order(5))

# Task7 Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumbers():
    def __init__(self, re, im):
        self.re = re
        self.im = im * 1j

    def __str__(self):
        return f"{self.re} + {self.im}"

    def __add__(self, other):
        return f"{self.re + other.re} + {self.im + other.im}"

    def __mul__(self, other):
        return f"{(self.re + self.im) * (other.re + other.im)}"

num1 = ComplexNumbers(2, 3)
num2 = ComplexNumbers(1, 2)
print(num1.__str__())
print(num2.__str__())
print(num1 + num2)
print(num1 * num2)

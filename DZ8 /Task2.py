# Task2 Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
# качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyClass(Exception):

    @staticmethod
    def divide(a, b):
        try:
            res = a/b
            return res
        except ZeroDivisionError:
            return f"You can not divide by 0!"

print(MyClass.divide(3, 0))


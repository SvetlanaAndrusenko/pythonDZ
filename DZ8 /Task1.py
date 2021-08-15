# Task1 Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data():
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"The data: {self.data}"

    @classmethod
    def class_method(cls, data):
        cl_m_res = []
        for i in data.split('-'):
            cl_m_res.append(int(i))
        return cl_m_res

    @staticmethod
    def stat_method(data):
        list = data.split('-')
        if (int(list[0]) > 0 and int(list[0]) <= 31) and (int(list[1]) > 0 and int(list[1]) <= 12) and (int(list[2]) > 0):
            return f"The data: {data}"
        else:
            return f"Enter the right data"

data = Data('01-11-2001')
print(data.__str__())
print(data.class_method('28-01-2017'))
print(Data.stat_method('56-05-2014'))



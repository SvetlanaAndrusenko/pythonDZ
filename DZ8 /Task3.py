# Task3 Создайте собственный класс-исключение, который должен проверять содержимое списка
# на наличие только чисел. Проверить работу исключения на реальном примере. Необходимо
# запрашивать у пользователя данные и заполнять список. Класс-исключение должен контролировать
# типы данных элементов списка.

class MyClass(Exception):
    def __init__(self, *args):
        self.list = []

    def check(self):
        #new_list = []
        while True:
            try:
                value = input("Enter the value: ")
                if value == 'stop':
                    break
                if not value.isdigit():
                    raise NotNumber(value)
                self.list.append(int(value))
                print(f"The List: {self.list}")
            except:
                print("Enter the number")

num = MyClass()
print(num.check())

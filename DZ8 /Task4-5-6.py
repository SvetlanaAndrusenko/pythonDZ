# Task4 Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым
# для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# Task5 Продолжить работу над первым заданием. Разработать методы,
# отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.
# Task6 Продолжить работу над вторым заданием. Реализуйте механизм валидации
# вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.
class Storage():
    def __init__(self):
        self.dict = {}

    def receive(self, name):
        self.dict.update({'equipment': name})

    def transfer(self, name):
        if name in self.dict:
            self.dict.pop(name)

class Equipment():
    def __init__(self, name, price, year, quantity):
        self.name = name
        self.price = price
        self.year = year
        self.quantity = quantity

class Printer(Equipment):
    def __init__(self, name, price, year, quantity):
        super().__init__(name, price, year, quantity)

class Scanner(Equipment):
    def __init__(self, name, price, year, quantity):
        super().__init__(name, price, year, quantity)

class Copier(Equipment):
    def __init__(self, name, price, year, quantity):
        super().__init__(name, price, year, quantity)

store = Storage()
scanner = Scanner('Scanner1', 4500, 2017, 5)
store.receive('scanner')
printer = Printer('Printer1', 5600, 2019, 3)
store.receive('printer')
copier = Copier('Copier', 7990, 2020, 6)
store.receive('copier')
print(store.dict)

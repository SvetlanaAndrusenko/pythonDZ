# Task3 Реализовать базовый класс Worker (работник).
# ● определить атрибуты: name, surname, position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker;
# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        # атрибуты (income защищенный)
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    # методы
    def get_full_name(self):
        return f"Worker: {self.name} {self.surname}"

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")

# экземпляр
person = Position('Дмитрий', 'Баринов', 'Ассистент', 30000, 5600)
# проверка значений атрибутов
print(f"Full information: {person.name}, {person.surname}, {person.position}, {person._income}")
# вызов методов
print(f"{person.get_full_name()}")
print(f"Total income: {person.get_total_income()}")
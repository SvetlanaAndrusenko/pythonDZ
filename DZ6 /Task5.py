# Task5  Реализовать класс Stationery (канцелярская принадлежность).
# ● определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

class Stationery():
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Start drawing')

class Pen(Stationery):
    def draw(self):
        print(f"You use pen for {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"You use pencil for {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"You use handle for {self.title}")

pen = Pen('picture 1')
pencil = Pencil('picture 2')
handle = Handle('picture 3')
# переопределение метода
print(pen.draw())
print(pencil.draw())
print(handle.draw())
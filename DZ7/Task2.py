# Task2 Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное
# название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды
# существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(): #абстрактный класс (для основного)
    @abstractmethod
    def calculation(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def calculation(self):
        print(f"The amount of fabric for the coat: {self.v/6.5 + 0.5}")

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def calculation(self):
        print(f"The amount of fabric for the coat: {2 * self.h + 0.3}")

class Full(Clothes):
    def __init__(self, v, h):
        self.h = h
        self.v = v
    @property
    def calculation(self):
        print(f"Fabric size for coat and suit: {(self.v/6.5 + 0.5) + (2 * self.h + 0.3)}")


coat = Coat(130)
suit = Suit(150)
full = Full(130, 150)
print(coat.calculation)
print(suit.calculation)
print(full.calculation)



"""
# не использовался абстракный класс
class Clothes():
    def __init__(self,v,h):
        self.v = v
        self.h = h

    #для пальто
    def coat(self):
        return f"For the coat: {self.v/6.5 + 0.5}"
    #для костюма
    def suit(self):
        return f"For the suit: {2 * self.h + 0.3}"
    #используем декоратор @property
    @property
    def full(self):
        return f"Fabric size for coat and suit: {(self.v/6.5 + 0.5) + (2 * self.h + 0.3)}"

fabric = Clothes(130,150)
print(fabric.coat())
print(fabric.suit())
print(fabric.full)
"""
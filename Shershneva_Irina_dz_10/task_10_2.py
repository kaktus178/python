"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
классы для основных классов проекта и проверить работу декоратора @property.
"""

from abc import ABC, abstractmethod


class FabricCalculation(ABC):
    def __init__(self, parameters):
        self.parameters = parameters

    @abstractmethod
    def calculate(self):
        pass


class Coat(FabricCalculation):
    @property
    def calculate(self):
        coat = self.parameters / 6.5 + 0.5
        return coat


class Suit(FabricCalculation):
    @property
    def calculate(self):
        suit = 2 * self.parameters + 0.3
        return suit


my_coat = Coat(44)
my_suit = Suit(170)
res = my_coat.calculate+my_suit.calculate

print(f'Fabric consumption per coat {my_coat.calculate:.2f}')
print(f'Fabric consumption per suit {my_suit.calculate:.2f}')
print(f'Total fabric consumption: {res:.2f}')

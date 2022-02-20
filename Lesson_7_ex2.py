# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.¶
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

# импорт библиотек
from abc import ABC, abstractmethod


# объявим абстрактный класс Clothes
class Clothes(ABC):
    common_mat = 0  # атрибут класса - показывает общее количество материала

    @abstractmethod
    def get_material(self):  # абстрактный метод, возвращающий кол-во мат-ла для экземпляра класса
        pass

    @property
    @abstractmethod
    def get_name(self):  # абстрактное свойство, устанавливающее название модели
        pass


# класс пальто
class Coat(Clothes):

    def __init__(self, name):                                      # конструктор класса
        self.__name = name

    @property
    def get_name(self):                                            # реализация геттера свойства name
        return self.__name

    @get_name.setter                                               # реализация сеттера свойства name
    def get_name(self, name):
        self.__name = name

    def get_material(self, size):                                  # реализация метода абстрактного класса для класса Пальто
        Clothes.common_mat += round(size / 6.5 + 0.5, 2)           # изменение статического атрибута родительского класса
        return f"Количество материала для модели {self.__name}" \
               f" - {round(size / 6.5 + 0.5, 2)} пог.м"            # возвращаем значение для экзепляра класса


class Suit(Clothes):

    def __init__(self, name):
        self.__name = name

    def get_material(self, height):
        Clothes.common_mat += round(2 * height + 0.3, 2)
        return f"Количество материала для модели {self.__name}" \
               f" - {round(2 * height + 0.3, 2)} пог.м"

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def get_name(self, name):
        self.__name = name


coat1 = Coat("Честерфилд")
coat2 = Coat("Ольстер")
suit1 = Suit("Тройка")
suit2 = Suit("Фрак")
print(coat1.get_material(50))
print(coat2.get_material(56))
print(suit1.get_material(1.6))
print(suit2.get_material(1.75))
print(f"Общее количество материала: {Clothes.common_mat} пог.м.")

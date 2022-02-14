# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);¶
# проверить работу примера на реальных данных:
# создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров.

# определим класс Worker
class Worker:
    # атрибуты
    _income = {"wage": 0.0, "bonus": 0.0}      # доход
    name = ""                                  # имя
    surname = ""                               # фамилия
    position = "разнорабочий"                  # должность

    def __init__(self, wage, bonus):           # конструктор класса с двумя параметрами
        self._income["wage"] = float(wage)     # инициализация переменной _income
        self._income["bonus"] = float(bonus)


# определим класс Position с родительским классом Worker
class Position(Worker):

    # методы класса
    def get_full_name(self):                                                # возвращает полное имя
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(f"Общий доход {sum(t for t in self._income.values())} руб.")  # возвращает доход


# первый рабочий
emp_1 = Position(25000, 6000)
emp_1.name = "Петя"
emp_1.surname = "Иванов"
emp_1.position = "генеральный директор"
emp_1.get_full_name()
print(emp_1.position)
emp_1.get_total_income()

# второй рабочий
print("\n")
emp_2 = Position(23000, 7000)
emp_2.name = "Александр"
emp_2.surname = "Пушкин"
emp_2.get_full_name()
print(emp_2.position)
emp_2.get_total_income()

# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31 32 3 5 32 3 5 8 3
# 37 43 2 4 6 8 3 7 1
# 51 86 -1 64 -8
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
from random import randrange as rand

# объявим класс Matrix
class Matrix:
    # переопределим конструктор
    def __init__(self, data_matrix):
        self.__data = data_matrix                                   # данные матрицы
        self.columns = 0                                            # кол-во столбцов
        self.rows = 0                                               # кол-во строк
        index = 0                                                   # индекс для прохода в цикле
        max_row = len(max(data_matrix, key=len))                    # самая длинная строка в матрице
        self.max_data_number = int(max(max(self.__data, key=max)))  # максимальное число в матрице
        self.min_data_number = int(min(min(data_matrix, key=min)))  # минимальное число в матрице


        # проходим циклом по всем элементам
        for r in self.__data:
            if len(self.__data[index]) < max_row:                                 # если текущая строка матрицы короче максимальной,
                for n in range(max_row - len(self.__data[index])):                # дополняем её недостающими случайными значениями
                    self.__data[index].append(rand(self.min_data_number,          # из диапазона значений матрицы
                                                   self.max_data_number))
            index += 1
        self.rows = len(self.__data)   # инициализируем переменные: количество строк
        self.columns = max_row         # количество столбцов

    # переопределим метод __str__
    def __str__(self):
        str_align = "{:{fill}{align}{width}}"  # определим шаблон форматирования строки
        string = ""
        for r in self.__data:                  # применим шаблон к каждому элементу матрицы
            for num in r:
                string += str_align.format(f'{num} ', fill='0', align='>', width=len(str(self.max_data_number))+1)
            string += "\n"
        return string

    # переопределим оператор "=="
    def __eq__(self, other):                                          # если кол-во строк и столбцов обеих матриц равно
        return True if other.rows == self.rows\
                       and other.columns == self.columns else False   # вернем True, в противном случае - False

    def __add__(self, other):
        temp = list()                                                   # переменная типа list() - список списков
        row = list()                                                    # объявим переменную для хранения значений рядов
        if self == other:                                               # если складываемые матрицы одного размера
            for r in range(self.rows):
                for n in range(self.columns):
                    row.append(other.__data[r][n] + self.__data[r][n])  # добавляем сумму n-х индексов складываемых матриц
                temp.append(row.copy())                                 # добавляем полученный ряд в новую матрицу
                row.clear()                                             # очищаем значения
            return Matrix(temp)                                         # возвращаем новую матрицу
        else:
            print(f"У складываемых матриц"
                  f" должно быть одинаковое количество столбцов и строк")
            return None  # если матрицы не одинакового размера, возвращаем None


data = ([8, 9, 23, 45, 67, 34, 56, 8000], [3, 4, 98], [700, 5, 7, 9], [23, 76, 435, 90567], [23, 76, 435])
data1 = ([12, 4, 98], [700, 5, 7, 9895], [67, 9, 23, 4587, 67, 34, 56, 987], [23, 76], [23, 76])
data3 = ([12, 4, 98], [700, 5, 7, 9], [67, 9, 23, 45, 67, 34, 56, 987], [23, 76], [23, 76])
A = Matrix(data)
B = Matrix(data1)
C = Matrix(data3)
D = Matrix(([1, 1, 1], [2], [3]))
E = Matrix(([0, 2, 0], [4], [5]))
print(f"Матрица A\n{A}")
print(f"Матрица B\n{B}")
print(f"Матрица C\n{C}")
print(f"Сложение матриц: A + B + C\n{A + B + C}")
print(f"Матрица D\n{D}")
print(f"Матрица E\n{E}")
print(f"Сложение матриц: D + E\n{D + E}")
print(f"Сложение матриц: C + D\n{C + D}")



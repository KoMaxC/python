# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

# объявим функцию my_func с тремя аргументами
def my_func(arg_1, arg_2, arg_3):
    arg_1 = float(arg_1) if str(arg_1).isdigit() or type(arg_1) != str else len(arg_1)  # проверяем входящие параметры
    arg_2 = float(arg_2) if str(arg_2).isdigit() or type(arg_2) != str else len(
        arg_2)                                                                          # если это числа, преобразуем их в тип float
    arg_3 = float(arg_3) if str(arg_3).isdigit() or type(arg_3) != str else float(
        len(arg_3))                                                                     # если строка - сравнивать будем длину строки

    if arg_1 > arg_2:
        arg_1, arg_2 = arg_2, arg_1  # сравниваем значения операндов и меняем их местами
    if arg_2 > arg_3:                # если текущее значение меньше следующего
        arg_2, arg_3 = arg_3, arg_2
    if arg_1 > arg_2:
        arg_1, arg_2 = arg_2, arg_1

    print(f"Суммма двух наибольших аргументов {arg_2} и {arg_3}: {arg_2 + arg_3}")


my_func(3, "абракадабра", 1)

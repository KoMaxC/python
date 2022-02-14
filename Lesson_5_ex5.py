# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import random as rand                                               # импортируем модуль random
file_path = "gen_numbers.txt"                                                   # путь к файлу
count = int(input("Введите количество чисел..."))                               # запрос на ввод от пользователя
with open(file_path, "w") as gen_numbers:                                       # открываем файл для записи
    print(*([round(rand()*100, 2) for i in range(count)]), file=gen_numbers)    # генерируем набор случайных чисел в количестве count
with open(file_path, "r") as gen_numbers:                                       # открываем файл для чтения
    print(round(sum([float(i) for i in gen_numbers.read().split()]), 3))        # считываем данные, приводим к типу float, находим сумму и выводим на монитор

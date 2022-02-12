# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

# импортируем функцию reduce() из библиотеки functools
from functools import reduce

# сформируем список с четными числами
gen_list = [i for i in range(100, 1001) if i % 2 == 0]

# применяем лямбда-выражение в функции reduce(), перемножая элементы списка
mult_all = reduce(lambda x, y: x*y, gen_list)

# выводим результат
print(f"{mult_all}")

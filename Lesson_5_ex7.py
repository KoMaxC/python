# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).¶
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

# импорт библиотеки для работы с json-файлами
import json

firms_list = list()    # названия фирм
firms_dict = dict()    # итоговая информация о фирмах
avg_dict = dict()      # словарь со средней прибылью
profit_list = list()   # прибыли\убытки
revenue_list = list()  # выручка
costs_list = list()    # затраты
final_list = list()    # итоговый список
average_profit = 0.0   # среднее значение прибыли

with open("firms_info.txt", "r", encoding="utf8") as firms_info:            # открываем файл для чтения
    for line in firms_info:                                                 # считываем построчно и преобразуем в список
        firms_list.append(line.split()[0])                                  # заполняем список с названиями
        revenue_list.append(float(line.split()[2]))                         # ...выручка
        costs_list.append(float(line.split()[3]))                           #... затраты
        profit_list.append((float(line.split()[2])-\
                            float(line.split()[3])))                        #... прибыли\убытки

average_profit = (sum([p for p in profit_list if p > 0])\
                  / len([p for p in profit_list if p > 0]))                 # вычисляем среднее значение прибыли без учета убыточных фирм
firms_dict = {key: value for key, value in zip(firms_list, profit_list)}    # заполняем словарь итоговыми данными
avg_dict = {"average_profit":average_profit}                                # ...со средним значением
final_list = [firms_dict, avg_dict]                                         # формируем итоговый список
print(final_list)                                                           # выводим на экран
with open("firms_info.json", "w") as data_file:                             # создаем файл json
    json.dump(final_list, data_file)                                        # записываем в него результат

# coding: utf-8


# Подключение модулей
import ex24
# или
from ex24 import counties

print ex24.counties == counties

# Взаимодействие черех интерфейс
print ex24.get_country_by_index(143)
# или напрямую
print counties[143]


# Упражнения:
#
# 1. Разберитемь с примером, напишите комментарий, над каждой строкой
#
# 2. Какие достоинства и недостатки использования интерфейсов
#    к данным? (get_country_by_index, get_index_by_country)
#

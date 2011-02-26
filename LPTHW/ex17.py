# coding: utf-8

# Копирование файлов

from sys import argv

# exists принимает один параметр с путем
# к файлу или директории
# Возвращает True, если файл/директория сущаствуют
# иначе False
from os.path import exists

script, from_file, to_file = argv

# Как отурыть файл и считать из него данные в одну строку?
infile = open(from_file)
indata = infile.read()

# len() - встроенная функция, для подсчёта длины последовательности
print "Размер файла %s: %s байт" % (from_file, len(indata))

print "Файл %s для записи уже существует? %s" % (to_file, exists(to_file))

print "Нажмите ENTER чтобы записать данные, или CTRL-C для отмены"
raw_input('?')

outfile = open(to_file, 'w')
outfile.write(indata)

print "Данные скопированы из файла %s в файл %s" % (from_file, to_file)

infile.close()
outfile.close()

# Упражения:
#
# 1. Разберитесь, как работает конструкция from ... import
#
# 2. Зачем нужно закрывать outfile?
#

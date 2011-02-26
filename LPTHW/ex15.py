# coding: utf-8

# Чтение текстовых файлов

from sys import argv

script_name, file_name = argv

# посмотрите в документацию
# клчевые слова: open, file
txt_file = open(file_name)

print "Вот содержимое файла %s:" % file_name
print txt_file.read()

print "Введите назвавние файла:"
file_name = raw_input('> ')

print "Вот содержимое файла %s:\n%s" % (
    file_name,
    open(file_name).read(), # что делает эта строка?
)

# Упражнения:
#
# 1. Избавтесь от raw_input, добавьте второй файл параметром
#
# 2. Почему у открытого файла (объект txt_file) не вызывается
#    метод .close()? Когда нужно вызывать .close()?
#


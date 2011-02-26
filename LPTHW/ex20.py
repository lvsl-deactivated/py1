# coding: utf-8

# Функции и файлы

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0) # перевести указатель текущей позиции в файле на начало

def print_line(line_no, f):
    print line_no, f.readline()

f = open(input_file)

print "Давайте сначала выведем всё содержимое файла"

print_all(f)


print "Переводит текущую позицию в файле на начало"
rewind(f)

print "Выводим первые трми строки файла"

current_line = 1
print_line(current_line, f)

current_line = current_line + 1
print_line(current_line, f)

current_line = current_line + 1
print_line(current_line, f)

# Упражнения:
#
# 1. Найтиде в документации описание метода seek.
#
# 2. Разберитесь, как работает конструкция "+="
#    измените пример используя эту конструкцию
#

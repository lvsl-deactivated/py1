# coding: utf-8

# Чтение и запись в файлы

# Основные функции для работы в файлами:
#
# close()    - закрыть файл
# read()     - считать содержимое всего файла в строку
# readline() - считать одну строку текста
# truncate() - удалить всё содержимое файла
# write(s)   - записать строку s в файдё

from sys import argv

script_name, file_name = argv

print "Сейчас файл %s будет удалён!" % file_name

print "Если вы этого не хотите, нажмите CTRL-C (^C)."
print "Чтобы удалить файл нажмите ENTER"

raw_input("?")

print "Файл открывается..."
target = open(file_name, 'w')

print "Обрезаем файл..."
target.truncate()

print "Введите текст который будет записан в файл."

txt1 = raw_input("line1> ")
txt2 = raw_input("line2> ")
txt3 = raw_input("line3> ")

target.write(txt1)
target.write("\n")

target.write(txt2)
target.write("\n")

target.write(txt3)
target.write("\n")

print "Данные записаны, закрывем файл"
target.close()

# Упражнения:
#
# 1. Сделайте всю запись в файл, одним вызовом .write()
#
# 2. Что означает параметр 'w' в вызове open?
#    Какие ещё бывают параметры?
#

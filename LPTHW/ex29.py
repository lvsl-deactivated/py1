# coding: utf-8

# Конструкция if

people = 10
cats = 20
dogs = 30

if people < cats:
    print "Кошки!"

if people < dogs:
    print "Собаки!"

people += 30

if people > cats and people > dogs:
    print people, cats, dogs
    print "OK!"

# Упражнения:
#
# 1. Всегда ли необходимы отступы после if?
#    Что будет если убрать отступы?
#

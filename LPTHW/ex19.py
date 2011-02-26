# coding: utf-8

# Функции и переменные

# паретрами в функции могут выступать любые
# выражения, но не конструкции!

def mix_stuff(drink1, drink2, result):
    print "%s + %s = %s" % (drink1, drink2, result)

beer = "Пиво"
vodka = "Водка"
cogniac = "Коньяк"
cola = "Кола"
martini  = "Мартини"
juice = "Сок"

good  = "Хорошо"
bad = "Плохо"
sad  = "Грустно"

mix_stuff(beer, vodka, bad)
mix_stuff(vodka, juice, good)
mix_stuff(cogniac, vodka, bad)
mix_stuff(cogniac, cola, good)
mix_stuff(martini, beer, bad)
mix_stuff(martini, juice, good)

mix_stuff("молоко", "cолёные " + "огурцы", "Очень " + sad)

# Упражнения:
#
# 1. Напишите две функции mix_good_stuff и mix_bad_stuff
#    каждая должна принимать два аргумента, и вызывать mix_stuff
#

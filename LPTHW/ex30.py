# coding: utf-8

# Конструкция if/elif.../else

def check(people, cats, dogs):
    if people > cats and people > dogs:
        result = "OK!"
    elif people > cats:
        result = "Собаки!"
    elif people > dogs:
        result = "Кошки!"
    else:
        result = "Кошки и Собаки!"

    return result


print check(10,20,30)
print check(20,20,30)
print check(30,20,30)
print check(40,20,30)

# Упражнения:
#
# 1. Перепишите функцию check() без использования elif.
#    Как проще?
#    Подсказка: Используйте вложенные if/else
#

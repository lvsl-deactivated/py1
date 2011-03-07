# coding: utf-8

# Функции могут возвращать значения.
# Чтобы вернуть значение из функции
# конструкцию `return <выражение>`

def add(a, b):
    print  "ADDING %s + %s" % (a, b)
    return a + b

def subtract(a,b):
    print "SUBTRACTING: %s - %s" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING: %s * %s" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING: %s / %s" % (a, b)
    return a / b

def pi():
    print "GETTING THE VALUE OF A π"
    return 3.14159265

def e():
    print "GETTING THE VALUE OF A e"
    return 2.71828182

result = divide(multiply(pi(), e()),
                subtract(add(pi(), e()), e()))

print result

# Упражнения:
#
# 1. Разбейте вычисление result на несколько этапов так,
#    чтобы на каждом этапе было не больше одного вызова функции
#
# 2. Что вернёт вынкция add(), если строку return a + b заменить на a + b?
#    Почему возвращается именно такое значение?
#

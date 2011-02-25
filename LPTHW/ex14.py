# coding: utf-8

from sys import argv

script_name, user = argv
prompt = '> '

print "Привет %s! Я %s" % (user, script_name)
print "Вы любите программировать?"
like_it = raw_input(prompt)

print "Где вы живёте?"
lives = raw_input(prompt)

print "Какой у вас компьютер?"
computer = raw_input(prompt)

print """
Итак %r, вы отвечаете %r.
Я знаю, где вы живете: %r
и какой у вас компьютер: %r.
\t -- как мило!
""" % (user, like_it, lives, computer)

# Упражения:
#
# 1. Найдите какой-нибудь текст, и вынесите имена
#    персонажей из этого текста в переменные.
#    Спросите пользователя, хоччет ло он изменить имена
#    перед тем как вывести текст
#

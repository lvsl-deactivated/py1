# coding: utf-8

#
# Простейший пример GAE приложения
#

import os
import sys

# CGI сохраняет запрос в переменных окружения
params_dict = os.environ

# CGI ответ, это данные выданные программой в stdout
print 'Content-Type: text/html'


# Если это POST запрос то его содержимое в stdin
print '<pre>'
print sys.stdin.read()
print '</pre>'

print '<ul>'
for k,v in params_dict.items():
    print '<li></b>%s</b>:%s</li>' % (k,v)
print '</ul>'

# вот и всё!

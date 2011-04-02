# coding: utf-8

#
# Пример использования встроенноой в GAE
# билблиотеки для разработки: webapp
#

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

# Класс обработчий запросов
class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('<h1>Hello webapp!</h1>')

# Какой обработчик на какой урл вызывается
app = webapp.WSGIApplication(
  [('/.*', MainPage)],
  debug=True,
)

def main():
  run_wsgi_app(app)

if __name__ == "__main__":
  main()

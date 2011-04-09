# coding: utf-8

# Пример использование сервиса Google Accounts

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class MainPage(webapp.RequestHandler):
    def get(self):
        # получаем текущего пользователя
        user = users.get_current_user()

        html = ['<html><head><title>Google Accounts Test</title></head><body>']
        if not user:
            # получаем ссылку для входа
            login_url = users.create_login_url(self.request.path)
            html.append('<h1>Я вас не знаю!</h1>'
                        '<a href="%s">Залогиньтесь плиз!</a>' % login_url)
        else:
            # получаем ссылку для выхода
            logout_url = users.create_logout_url(self.request.path)
            html.append('<h1>Здарова %s!</h1>'
                        '<a href="%s">Разлогинется можно тут!</a>' % (
                        user.email(), logout_url))

        html.append('</body></html>')

        # отдаем страничку
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'

        self.response.out.write(''.join(html))


app = webapp.WSGIApplication([('/.*', MainPage)], debug=True)


def main():
    run_wsgi_app(app)


if __name__ == "__main__":
    main()

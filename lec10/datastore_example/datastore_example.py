# coding: utf-8

# Пример использование сервиса Google Datastore

import os.path
import logging

from google.appengine.api import users
from google.appengine.api import memcache

from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp.util import run_wsgi_app
# В этот раз мы будеим пользоваться шаблонами
from google.appengine.ext.webapp import template


TMPL_ROOT = os.path.join(os.path.dirname(__file__),
                         'templates')

# Описане ORM модели
class UserPrefs(db.Model):
    '''\
    Настройки пользователя
    '''
    tz_offset = db.IntegerProperty(default=0)
    user = db.UserProperty(auto_current_user_add=True)

    def cache_set(self):
        k = self.key().name()
        ns = self.key().kind()
        logging.info("Saving %s in namespace  %s" % (k, ns))

        memcache.set(k, self, namespace=ns)

    def put(self):
        self.cache_set()
        db.Model.put(self)


# Функции для работы с моделями
def get_userprefs(user_id=None):
    '''\
    Получает и возвращает объект UserPrefs по user_id,
    если объект не найден, то он будет создaн.
    Если пользователь не найден возвращается None
    '''
    if not user_id:
        user = users.get_current_user()
        if not user:
            return None
        user_id = user.user_id()

    # сначала ищем в кеше
    userprefs = memcache.get(user_id, namespace='UserPrefs')
    if not userprefs:
        logging.info("Cache miss for %s" % user_id)
        # ищем объект пользователя
        key = db.Key.from_path('UserPrefs', user_id)
        userprefs = db.get(key)
        if not userprefs:
            userprefs = UserPrefs(key_name=user_id)
        else:
            userprefs.cache_set() # сохнаняем в кеше
    else:
        logging.info("Cache hit for %s" % user_id)

    return userprefs

def build_ctx(request):
    '''\
    Вспомогательная функция для построения конекста
    '''
    # получаем текущего пользователя
    user = users.get_current_user()

    # контекст для шаблона
    ctx = {}

    ctx['user'] = user
    if not user:
        # получаем ссылку для входа
        lurl = users.create_login_url(request.path)
        ctx['is_logged_in'] = False
    else:
        # получаем ссылку для выхода
        lurl = users.create_logout_url(request.path)
        ctx['is_logged_in'] = True

    ctx['lurl'] = lurl

    return ctx


class MainPage(webapp.RequestHandler):
    '''\
    Главная страница
    '''
    def get(self):
        ctx = build_ctx(self.request)
        prefs = get_userprefs()
        if prefs:
            ctx['tz_offset'] = prefs.tz_offset
        else:
            ctx['tz_offset'] = '???'
        tmpl = template.render(os.path.join(TMPL_ROOT, 'main.html'), ctx)
        self.response.out.write(tmpl)


class SavePrefs(webapp.RequestHandler):
    '''\
    Страница сохранения настроек пользователя
    '''
    def get(self):
        user = users.get_current_user()
        if not user:
            return self.redirect(users.create_login_url(self.request.path))
        userprefs = get_userprefs()
        ctx = build_ctx(self.request)
        ctx['tz_offset'] = userprefs.tz_offset
        tmpl = template.render(os.path.join(TMPL_ROOT, 'prefs.html'), ctx)
        self.response.out.write(tmpl)

    def post(self):
        user = users.get_current_user()
        if not user:
            return self.redirect(users.create_login_url(self.request.path))
        userprefs = get_userprefs()

        try:
            tz_offset = int(self.request.get('tz_offset'))
            userprefs.tz_offset = tz_offset
            userprefs.put() # не забываем сохранить данные
        except ValueError:
            pass

        self.redirect('/')


app = webapp.WSGIApplication(
    [
        ('/', MainPage),
        ('/prefs', SavePrefs),
    ],
    debug=True)


def main():
    run_wsgi_app(app)


if __name__ == "__main__":
    main()

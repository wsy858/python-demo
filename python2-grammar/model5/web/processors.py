#-*- coding: utf-8 -*-
"""

Created on 2016年12月9日
@author: evan wang
"""
import web

urls = (
    '/', 'Index',
    '/login', 'Login',
    '/logout', 'Logout',
)

class Index:

    def GET(self):
        return '<html>Hello %s <a href="/logout">Logout</a></html>' \
            % web.ctx.username


class Login:

    def GET(self):
        return """
        <html>
        <form action="" method="post">
            <input type="text" name="username">
            <input type="submit" value="Login">
        </form>
        </html>
        """

    def POST(self):
        # only set cookie if user login succeeds
        name = web.input(username=None).username
        if name:
            web.setcookie('username', name)
        raise web.seeother('/')


class Logout:

    def GET(self):
        web.setcookie('username', '', expires=-1)
        raise web.seeother('/login')


# Auth Processor
def auth_app_processor(handle):
    path = web.ctx.path
    web.ctx.username = name = web.cookies(username=None).username
    if not name and path != '/login':
        raise web.seeother('/login')
    return handle()


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.add_processor(auth_app_processor)
    app.run()
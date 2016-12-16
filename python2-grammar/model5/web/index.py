# -*- coding: utf-8 -*-
"""
web.py demo
Created on 2016年11月23日
@author: evan
"""
import web

render = web.template.render('templates/')
urls = ('/', 'index')


class index:
    def GET(self, name):
        return render.hh(name)


# def GET1(self):
#         # return 'hello world!'
#         # hh是模板文件名， name是参数
#         i = web.input(name=None)
#         return render.hh(i.name)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

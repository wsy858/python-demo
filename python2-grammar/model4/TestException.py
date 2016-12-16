# -*- coding: utf-8 -*-
"""
Created on 2016年10月17日
异常处理
@author: evan
"""

'''
try:
    .... 
except Exception, e:
    ....
打开不存在的文件，抛出IOError异常 
'''
try:
    f = open('abc.txt', 'r')
    f.write('new text')
    f.close()
    print 'over'
except IOError, e:
    print 'io error', e
except NameError, e:
    print 'name error', e
print '\n'

'''
如果try语句块中发生异常，则跳转到except模块
如果try语句块中不发生异常，则跳转到else模块
try:
    .... 
except Exception, e:
    ....
else:
    ....    
'''
try:
    f = open('abc.txt', 'r')
    f.close()
    print 'aaa'
except Exception, e:
    print 'bbb'
else:
    print 'ccc'
print '\n'

'''
finally: 最终一定执行

try:
    ....
finally:
    ....   

'''
try:
    f = open('b.txt', 'r')
    print isinstance(f, file)
    print int(f.read())
except Exception, e:
    print e
else:
    print 'else---'
finally:
    #     if 'f' in locals().keys() :
    #         f.close()
    print 'close'
    try:
        f.close()
    except NameError, e:
        print e
print '\n'

'''
with语句, 主动清理资源
'''
import os

try:
    with open('a.txt') as f:
        for line in f.readlines():
            print line
        f.seek(-5, os.SEEK_SET)
except IOError, e:
    print e
    print 'f is closed : ', f.closed

'''
raise语句： 主动抛出异常
'''
# raise NameError('HiThere')
try:
    raise NameError('HiThere')
except NameError:
    print 'An exception flew by!'

'''
自定义异常
'''


class MyError(Exception):
    def __init__(self, error_info):
        self.error_info = error_info

    def __str__(self, *args, **kwargs):
        return repr(self.error_info)


try:
    raise MyError('user defined error----')
except MyError, msg:
    print msg

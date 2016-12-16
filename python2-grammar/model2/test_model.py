# -*- coding:utf-8 -*-
"""
Created on 2016年10月11日
模块和包
@author: evan
"""

# 引入3.0中的除法，得到浮点数
from __future__ import division
from __future__ import unicode_literals

'''
导入模块
import 语句    
    import module1[, module2[,... moduleN]
From…import 语句          
    from modname import name1[, name2[, ... nameN]]
From…import* 语句
    from modname import *
'''
import import_model

print import_model.xx(4)

# from import_model import *
# print xx(4);

# import os
# print os.path.isdir(r'C:\Windows\data')
# print os.path.isfile(r'C:\Windows\data\test.txt')

# from os import path
# print path.isdir(r'C:\Windows\data')
# print path.isfile(r'C:\Windows\data\test.txt')

from os.path import isdir, isfile

print isdir(r'C:\Windows\data')
print isfile(r'C:\Windows\data\test.txt')

'''
动态导入模块
Python 2.6/2.7提供了json 模块，但Python 2.5以及更早版本没有json模块，
不过可以安装一个simplejson模块，这两个模块提供的函数签名和功能都一模一样。
'''
try:
    import json
except ImportError:
    import simplejson as json

print json.dumps({'python': 2.7})
print json.JSONEncoder().encode({'name': ['evan']})

'''
Python的新版本会引入新的功能，但是，实际上这些功能在上一个老版本中就已经存在了。
要“试用”某一新的特性，就可以通过导入__future__模块的某些功能来实现。
'''
# python 2.7中整数除法得到整数，通过from __future__ import division引入3.0中除法得到浮点数结果
print  5 / 3
# 在Python 3.x中，字符串统一为unicode，不需要加前缀 u
s = 'am I an unicode?'
print isinstance(s, unicode)

'''
dir()函数
dir()函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
'''
import math

print dir(math)

'''
globals()和locals()函数
根据调用地方的不同，globals()和locals()函数可被用来返回全局和局部命名空间里的名字。
如果在函数内部调用locals()，返回的是所有能在该函数里访问的命名。
如果在函数内部调用globals()，返回的是所有在该函数里能访问的全局名字。
两个函数的返回类型都是字典。所以名字们能用keys()函数摘取。
'''


def test():
    aaa = 1111
    print '\n-------------globals() --------------'
    for key in globals().keys():
        print key, ': ', globals()[key]
    print '\n-------------locals() --------------'
    for key in locals().keys():
        print key, ': ', locals()[key]


test()

'''
reload()函数
当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
因此，如果你想重新执行模块里顶层部分的代码，可以用reload()函数。该函数会重新导入之前导入过的模块。语法如下：
reload(module_name)
'''
reload(import_model)

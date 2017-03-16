# -*- coding=utf-8 -*-
"""
Created on 2016年10月19日
字符串练习
@author: evan
"""
# from __future__ import unicode_literals

ss = r'''
                     ,
               ._  \/, ,|_
               -\| \|;|,'_
               `_\|\|;/-.
                `_\|/._
               ,'__   __`.
              / /_ | | _\ \
             / ((o)| |(o)) \
             |  `--/ \--'  |
       ,--.   `.   '-'   ,'
      (O..O)    `.uuuuu,'
       \==/     _|nnnnn|_
      .'||`. ,-' \_____/ `-.
       _||,-'      | |      `.
      (__)  _,-.   ; |   .'.  `
      (___)'   |__/___\__|  \(__)
      (__)     :::::::::::  (___)
        ||    :::::::::::::  (__)
        ||    :::::::::::::
             __|   | | _ |__
            (_(_(_,' '._)_)_)
'''
print ss

print '去除字符串首尾空格'
ff = ' kk ll'
print ff.strip()


# 字符串拼接
host = '127.0.0.1'
port = 27017
# url = host + ":" + port  # TypeError: cannot concatenate 'str' and 'int' objects
url = host + ":" + str(port)
print url





# print '\'xxx\' is unicode?', isinstance('xxx', unicode)
# print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
# print '\'xxx\' is str?', isinstance('xxx', str)
# print 'b\'xxx\' is str?', isinstance(b'xxx', str)
# print type('ccc')

# -*- coding=utf-8 -*-
"""
Created on 2016年10月19日
字符串练习
@author: evan
"""
# from __future__ import unicode_literals

print '去除字符串首尾空格'
ff = ' kk ll'
print ff.strip()


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
            https://api.wallstreetcn.com/v2/livenews/realtime?channelId=2&callback=jQuery21308337887406185882_1489559162026&min_updated=1489559627&_=1489559162175
            2017/3/15 14:33:47  2017/3/15 14:26:2
'''
print  ss


tt = {'info': u'\u5bfc\u6f14: \u90ed\u5728\u5bb9 Jae-young Kwak\xa0\xa0\xa0\u4e3b\u6f14: \u5b59\u827a\u73cd Ye-jin Son / \u66f9\u627f\u4f51 Seung-woo...',
      'quote': u'\u743c\u7476\u963f\u59e8\u5728\u97e9\u56fd\u7684\u6df1\u523b\u7248\u3002',
      'rank': u'249',
      'star': u'8.2',
      'title': u'\u5047\u5982\u7231\u6709\u5929\u610f\xa0/\xa0\ud074\ub798\uc2dd'}
print type(tt)
print type(dict(tt))

# print '\'xxx\' is unicode?', isinstance('xxx', unicode)
# print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
# print '\'xxx\' is str?', isinstance('xxx', str)
# print 'b\'xxx\' is str?', isinstance(b'xxx', str)
# print type('ccc')

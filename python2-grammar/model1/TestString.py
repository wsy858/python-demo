# -*- coding=utf-8 -*-
"""
Created on 2016年10月19日
字符串练习
@author: evan
"""
# from __future__ import unicode_literals
import re

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

sss = """select leader_uid,leader_name,friend_uid uid,friend_nick_name name,binding_time join_time,'团员好友' as type
          from t_biz_planner_group_member gm 
          left join t_biz_planner_friend_binding f on gm.uid=f.uid
          left join t_dfs g on g.id = f.id
          inner join t_fff j on j.id = f.id
          join dddd d
"""

# print sss.strip().replace(r"left join", 'WANGSY LEFT NIOJ').replace(r"inner join", "WANGSY INNER NIOJ").replace(r"join", "WANGSY NIOJ")
sss = re.sub(r"left[\s]+join", 'WANGSY LEFT NIOJ', sss, count=0, flags=re.I)
sss = re.sub(r"inner[\s]+join", 'WANGSY LEFT NIOJ', sss, count=0, flags=re.I)
sss = re.sub(r"[\s]+join", ' WANGSY NIOJ', sss, count=0, flags=re.I)
print sss
# print re.sub(r'(left) (join)', r'\2 \1', sss)


print re.sub(r"(where|None)", " ", "SELECT * FROM t_DATA_INFO a WHERE None ", count=0, flags=re.I)
print u"xxxx wan222 jjj wang".index("wang")

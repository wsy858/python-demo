# -*- coding: UTF-8 -*-
"""
Created on 2016年10月9日
时间模块
@author: evan
"""

# 引入time模块
import time

# 获取时间戳
ticks = time.time()
print '当前时间戳: ', ticks

# 返回时间元组
localtime = time.localtime()
print '当前时间元组：', localtime

# 格式化日期成2016-03-20 11:45:39形式
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
tuple_time = time.strptime(a, "%a %b %d %H:%M:%S %Y")
print time.mktime(tuple_time)


'''
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''

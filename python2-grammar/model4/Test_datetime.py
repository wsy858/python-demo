# -*- coding: UTF-8 -*-
import datetime

# 显示当天
today = datetime.date.today()
print today

# 时间差值
timedelta = datetime.timedelta(days=1)
yesterday = today - timedelta
# 显示昨天
print yesterday

cur = datetime.datetime.today()
# 显示最近5个小时的日期
for i in range(5):
    timedelta = datetime.timedelta(hours=(i + 1))
    print cur - timedelta

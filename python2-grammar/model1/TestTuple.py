# -*- coding: utf-8 -*-
"""
Created on 2016年10月12日
元组
Python的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
@author: evan
"""

# 1、创建元组
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"

# 2、访问元组，使用索引下标
s = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'augest', 'september')
print s[0]
print s[-1]
print s[1:3]
print s[3:]
print s[-2:]
print s[:10:2]

# 3、符号操作， 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100;
# 创建一个新的元组
tup3 = tup1 + tup2
print tup3
print tup3 * 3

# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tup = ('physics', 'chemistry', 1997, 2000);
print tup
del tup
print "After deleting tup : "
print tup
s = 1, 2

# -*- coding: utf-8 -*-
"""
Created on 2016年10月12日
字典
@author: evan
"""
'''
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中,格式如下所示：
d = {key1 : value1, key2 : value2 }
字典注意事项：
1）字典的key不重复，不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2）字典的key必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
'''
# 1、创建dict
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    66: 66,
    'Lisa': 88
}

# 2、访问字典里的值
print d['Adam']
print d['Lisa']
print d[66]
# 如果key不存在则访问报错, 如下所示：
# print d['Alis']
# 解决办法1，使用in判断key是否存在
if 'Alis' in d:
    print d['Alis']
# 或者使用has_key函数
if d.has_key('Lisa'):
    print 'd[Lisa] ', d['Lisa']

# 解决办法2，使用get方法获取，如果key不存在则返回None
print d.get('Alis')

# 3、 更新字典元素, 使用赋值语句, 如果key不存在则添加，如果key存在则更新value
d['Alis'] = 86
d['Lisa'] = 99
print d

# 4、删除字典元素, 使用del语句
del d['Alis']
print d
# d.clear() #清空元素
# print d
# del d  # 删除字典


# 5、遍历字典, 先遍历得到每个key，然后通过key取到value
for key in d:
    print key, ' : ', d[key]
# 直接遍历出key和value
for k, v in d.iteritems():
    print k, ' : ', v

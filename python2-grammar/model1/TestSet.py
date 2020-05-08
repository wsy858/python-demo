# -*- coding: utf-8 -*-
"""
Created on 2016年10月12日
set集
set持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。
@author: evan
"""

# 1、创建set, 创建 set 的方式是调用 set()并传入一个 list
# 可以简写成s = {1, 2, 3, 4}
s = set([1, 2, 3, 4])
print s
# 不可以添加重复元素
s.add(4)
s.add(5)
print s

# 删除元素
s.remove(5)
# 删除元素如果元素不存在将报错
# s.remove(6)
if 6 in s:
    s.remove(6)

# 2、 由于set存储的是无序集合，所以我们没法通过索引来访问。可以判断某个元素是否在集中
print 1 in s
print 6 in s

# 3、遍历set
for name in s:
    print name

print list(s)

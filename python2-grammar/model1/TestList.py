# -*- encoding=utf-8 -*-
"""
Created on 2016年9月30日
列表
@author: evan
"""
# 1、使用下标索引来访问列表中的值
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7];
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1]
print "list2[-1]: ", list2[-1], list2[-3]

# 2、使用append()方法来添加列表项
list2.append(8)
print list2[len(list2) - 1]

# 3、通过索引下标更新列表元素
list2[7] = 88
print list2[7]

# 4、使用 del 语句来删除列表的的元素
print list2
del list2[7]
print list2

# 5、Python列表脚本操作符
print 'len  ', len([1, 2, 3])
print '[] + []  ', [1, 2, 3] + [4, 5, 6]
print '[] * n  ', [1, 2, 3] * 4
print '3 in [1, 2, 3] ', 3 in [1, 2, 3]

# 6、列表截取(切片)
L = range(1, 101)
print 'L[1:3] ', L[1:3]
print 'L[88:] ', L[88:]  # 从88开始到结束，省略冒号后面的。
print 'L[:10] ', L[:10]  # 从第一个数到第10个数，省略冒号前面的，注意索引是0-9。
print 'L[2::3] ', L[2::3]  # 3的倍数。
print 'L[4:50:5] ', L[4:50:5]  # 不大于50的5的倍数。
print 'L[-10:] ', L[-10:]  # 最后10个数；
print 'L[-56::5] ', L[-46::5]  # 最后10个5的倍数。

# 7、列表生成式， 1*2 , 3*4 ,5*6 .... 99*100
print [x * (x + 1) for x in range(1, 100, 2)]

# 列表生成式示例
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}


def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    else:
        return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)


tds = [generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'


# 请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
def toUppers(L):
    return [x.upper() for x in L if isinstance(x, str)]


print toUppers(['Hello', 'world', 101])

print [x * 100 + y * 10 + z for x in range(1, 10) for y in range(0, 10) for z in range(0, 10) if x == z]

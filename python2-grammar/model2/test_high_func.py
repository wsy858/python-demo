# -*- encoding=utf-8 -*-
"""
Created on 2016年10月8日
高阶函数
@author: evan
"""
from math import sqrt


def add(x, y, f):
    return f(x) + f(y)


print add(25, 9, sqrt)

'''
map函数
map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。

假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，请利用map()函数，
把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list：
输入：['adam', 'LISA', 'barT']
输出：['Adam', 'Lisa', 'Bart']
'''


def format_name(s):
    return s[0].upper() + s[1:].lower()


print map(format_name, ['adam', 'LISA', 'barT'])

'''
reduce函数
reduce()函数也是Python内置的一个高阶函数,
reduce()函数接收的参数和 map()类似，一个函数 f，一个list，但行为和 map()不同，
reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。

Python内置了求和函数sum()，但没有求积的函数，请利用recude()来求积：
输入：[2, 4, 5, 7, 12]
输出：2*4*5*7*12的结果
'''


def prod(x, y):
    return x * y


print reduce(prod, [2, 4, 5, 7, 12])

'''
filter函数
filter()函数是 Python 内置的另一个有用的高阶函数，
filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，
filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。

请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''


def is_sqr(x):
    r = int(sqrt(x))
    return r * r == x


print filter(is_sqr, range(1, 101))

'''
sorted()函数，可以自定义排序函数
sorted()函数可对list进行排序,如sorted([36, 5, 12, 9, 21])返回，[5, 9, 12, 21, 36]
sorted()也是一个高阶函数，它可以接收一个比较函数来实现自定义排序，比较函数的定义是，传入两个待比较的元素 x, y，
如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。
 
 对字符串排序时，有时候忽略大小写排序更符合习惯。请利用sorted()高阶函数，实现忽略大小写排序的算法。
输入：['bob', 'about', 'Zoo', 'Credit']
输出：['about', 'bob', 'Credit', 'Zoo']
'''


def cmp_ignore_case(s1, s2):
    x = s1.lower()
    y = s2.lower()
    if x > y:
        return 1
    if x < y:
        return -1
    return 0


print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

'''
返回函数
请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
'''


def calc_prod(lst):
    def lazy_f():
        def f(x, y):
            return x * y

        return reduce(f, lst)

    return lazy_f


f = calc_prod([1, 2, 3, 4])
print f()

'''
函数闭包
像这种内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。
闭包的特点是返回的函数还引用了外层函数的局部变量，所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。

返回闭包不能引用循环变量，请改写count()函数，让它正确返回能计算1x1、2x2、3x3的函数。
'''


def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j

            return g

        r = f(i)
        fs.append(r)
    return fs


f1, f2, f3 = count()
print f1(), f2(), f3()

'''
匿名函数
匿名函数 lambda x: x * x 实际上就是：
def f(x):
    return x * x
关键字lambda 表示匿名函数，冒号前面的 x表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不写return，返回值就是该表达式的结果。

利用匿名函数简化以下代码：
def is_not_empty(s):
    return s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
'''
print filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])
print (lambda x: x * x)(10)


# 打印某个数的阶乘

def factorial(n):
    print reduce(lambda x, y: x * y, range(1, n + 1))


factorial(5)

'''
函数装饰器
不改变原函数的代码，添加新的功能。如打印日志
'''


def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()'
        return f(x)

    return fn


@log
def fact(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


# 如下两句等价于在函数factorial上面添加@log
# f_new = log(fact)
# print f_new(10)

print fact(10)
print '\n'

''' 
打印函数执行时间
'''
import time


def performance(f):
    def fn(*args, **kw):  # 第一个参数接收任意个参数到元组，第二个参数接收任意个关键字参数到字典
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print 'call ', f.__name__, '() in ', (t2 - t1)
        return r

    return fn


@performance
def testperformance(x):
    return x * x


print testperformance(10)

'''
偏函数
当一个函数有很多参数时，调用者就需要提供多个参数。如果减少参数个数，就可以简化调用者的负担。
functools.partial就是帮助我们创建一个偏函数的。
'''

import functools

sorted_ignore_case = functools.partial(sorted, cmp=lambda x, y: cmp(x.upper(), y.upper()))
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])

# -*- coding: utf-8 -*-
"""
Created on 2016年10月14日
定制类
@author: evan
"""
from __future__ import division

'''
__str__() 返回对象字符串的形式
因为 Python 定义了__str__()和__repr__()两种方法，__str__()用于显示给用户，而__repr__()用于显示给开发人员。
'''


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)

    __repr__ = __str__


print '__str__ ***************************'
p = Person("张三", 28)
print p
print '\n'

'''
__cmp__ 定制对象的比较
编写Student的 __cmp__ 方法，让它按照分数从高到底排序，分数相同的按名字排序。
'''


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        if self.score == s.score:
            return cmp(self.name, s.name)
        return cmp(self.score, s.score)


print '__cmp__ ***************************'
L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print sorted(L)
print '\n'

'''
__len__ 定制返回对象长度
斐波那契数列是由 0, 1, 1, 2, 3, 5, 8...构成。
请编写一个Fib类，Fib(10)表示数列的前10个元素，print Fib(10) 可以打印出数列的前 10 个元素，len(Fib(10))可以正确返回数列的个数10。
'''


class Fib(object):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        a, b, s = 0, 1, []
        i = 0
        while i < self.num:
            s.append(a)
            a, b = b, a + b
            i += 1
        return s.__str__()

    def __len__(self):
        return self.num

    def __iter__(self):
        return self


print '__len__ ***************************'
f = Fib(10)
print f
print len(f)
print '\n'

'''
__iter__  将一个类的实例变成一个可迭代的对象
'''


class Fib2(object):
    def __init__(self, num):
        self.a, self.b = 0, 1  # 初始化两个计数器a， b
        self.num = num
        self.f = []

    def __iter__(self):
        return self  # 实例本身就是迭代对象， 故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.f.__len__() >= self.num:  # 退出循环的条件
            raise StopIteration()
        self.f.append(self.a)
        return self.a  # 返回下一个值


print '__iter__ ***************************'
for n in Fib2(10):
    print n
print '\n'

'''
__call__  将一个类的实例变成一个可调用的对象
'''


class Fib3(object):
    def __call__(self, n):
        a, b, L = 0, 1, []
        for i in range(n):
            L.append(a)
            a, b = b, a + b
        return L


print '__call__ ***************************'
f = Fib3()
print f(10)
# 通过callable()函数， 我们就可以判断一个对象是否是“可调用”对象。
print callable(Fib3())
print '\n'

'''
__int__   对象转为int, 使用//符号 
__float__ 对象转为float, 使用/符号，文件头导入 from __future__ import division
'''


class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return self.p / self.q


print '__int__ ***************************'
print int(Rational(7, 2))
print float(Rational(1, 3))
print '\n'

'''
属性的get和set方法装饰 
第一个score(self)是get方法，用@property装饰，
第二个score(self, score)是set方法，用@score.setter装饰，@score.setter是前一个@property装饰后的副产品。
'''


class Student2(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    @property
    def grade(self):
        if self.score >= 80:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


print 'get set ***************************'
s = Student2('Bob', 59)
print s.grade  # 对score赋值实际调用的是 set方法。

s.score = 60
print s.grade

s.score = 99
print s.grade
print '\n'

'''
由于Python是动态语言，任何实例在运行期都可以动态地添加属性。
__slots__ 是指一个类允许的属性列表, 则添加的属性只能属于这个元组里面的值。
__slots__定义的属性仅对当前类起作用， 对继承的子类是不起作用的
除非在子类中也定义__slots__， 这样， 子类允许定义的属性就是自身的__slots__加上父类的__slots__
'''


class Student3(object):
    # 指定允许的属性列表
    __slots__ = ('name', 'gender', 'score')

    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score


print '__slots__ ***************************'
s = Student3('李四', 'male', 88)
s.score = 88
print s.score
# s.grade = 'A' #不能在动态添加属性
# print s.grade       
print '\n'


'''
__getattr__ 当调用不存在的属性时， 比如score， Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
'''
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

print '__getattr__ ***************************'
print Chain('/aaa').status.user.timeline.list.bb

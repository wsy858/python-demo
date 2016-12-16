# -*- coding: utf-8 -*-
"""
Created on 2016年10月12日
类
@author: evan
"""

'''
定义一个person类
'''
class Person(object):
    # 构造方法
    def __init__(self, name, gender, birth, **kw):
        print '调用Person的构造方法'
        self.name = name
        self.gender = gender
        self.birth = birth
        for k, v in kw.iteritems():
            setattr(self, k, v)

    def getAttrName(self):
        return self.name

    def setAttrName(self, name):
        self.name = name

    # 重新object的__str__()方法
    def __str__(self, *args, **kwargs):
        return 'name: %s, gender: %s, birth: %s' % (self.name, self.gender, self.birth)


# xiaoming = Person()
# xiaohong = Person()
# print xiaoming
# print xiaohong
# print xiaoming == xiaohong

help(Person)
xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')
print xiaoming.name
print xiaoming.job
print xiaoming
print '\n'


# Teacher类集成自Person
class Teacher(Person):
    def __init__(self, name, gender, birth, course):
        # 子类中不会自动调用父类中的构造方法，需要手动调用
        super(Teacher, self).__init__(name, gender, birth)
        print '调用Teacher的构造方法'
        self.course = course


t = Teacher('Alice', 'Female', 25, 'English')
print t.name
print t.getAttrName()
print t.course

print dir(Person)
print dir(Teacher)

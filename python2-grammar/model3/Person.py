# -*- coding: utf-8 -*-
"""
Created on 2016年10月12日
类
@author: evan
"""
from types import MethodType

'''
定义一个person类
'''


class Person(object):
    # 构造方法
    def __init__(self, name, gender, birth, **kw):
        print '调用Person的构造方法'
        self.__name = name  # __开头为私有属性
        self.gender = gender
        self.birth = birth
        for k, v in kw.iteritems():
            setattr(self, k, v)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # 重新object的__str__()方法
    def __str__(self, *args, **kwargs):
        return 'name: %s, gender: %s, birth: %s' % (self.__name, self.gender, self.birth)


# Teacher类集成自Person
class Teacher(Person):
    def __init__(self, name, gender, birth, course):
        # 子类中不会自动调用父类中的构造方法，需要手动调用
        super(Teacher, self).__init__(name, gender, birth)
        print '调用Teacher的构造方法'
        self.course = course


if __name__ == "__main__":
    help(Person)
    p = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')
    print p.get_name()
    print p.job
    print p
    print '\n'

    t = Teacher('Alice', 'Female', 25, 'English')
    print 't.__getattribute__(\'gender\'): ', t.__getattribute__('gender')
    print 'hasattr(obj, \'gender\'): ', hasattr(t, 'gender')
    # 第三个参数为默认值，不存在gender属性则返回Male，不加默认值如不存在则报错
    print 'getattr(obj, \'gender\'): ', getattr(t, 'gender', 'Male')
    print 't.get_name(): ', t.get_name()
    print 't.get_name(): ', t.course
    print 't.set_name(\'fff\'): ', t.set_name('fff')

    print 't is instance od Person: ', isinstance(t, Person)
    print 't is instance od Teacher: ', isinstance(t, Teacher)
    print 't is instance od object: ', isinstance(t, object)

    print '给类绑定新的方法'


    def set_course(self, course):
        self.course = course
    Teacher.set_course = MethodType(set_course, None, Teacher)
    t.set_course(250)
    print t.course

    print dir(Person)
    print dir(Teacher)
